import os.path

currentdir = os.curdir

from PIL import Image, ImageDraw

import polar_fox
from polar_fox.graphics_units import (
    SimpleRecolour,
    AppendToSpritesheet,
    AddCargoLabel,
    AddBuyMenuSprite,
    ProcessingUnit,
)
import polar_fox.pixa as pixa
from polar_fox.pixa import Spritesheet, PieceCargoSprites
from gestalt_graphics import graphics_constants

DOS_PALETTE = Image.open("palette_key.png").palette

"""
Pipelines can be dedicated to a single task such as simple recolouring
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type
As of Jan 2018 there is just one complex pipeline for ships, which handles hull compositing + optional cargo provision
"""


class Pipeline(object):
    def __init__(self, name):
        # this should be sparse, don't store any ship info in Pipelines, pass at render time
        self.name = name

    @property
    def vehicle_source_input_path(self):
        # convenience method to get the ship source input image
        # I considered having this return the Image, not just the path, but it's not saving much, and is less obvious what it does when used
        return os.path.join(
            currentdir, "src", "graphics", "ships", self.ship.id + ".png"
        )

    def process_buy_menu_sprite(self, spritesheet):
        # this function is passed (uncalled) into the pipeline, and then called at render time
        # this is so that it has the processed spritesheet available, which is essential for creating buy menu sprites
        # n.b if buy menu sprite processing has conditions by vehicle type, could pass a dedicated function for each type of processing

        # spriteset templates will add 10px left and right padding to buy menu sprite to prevent cramped appearance in buy menu
        # note that this means
        # 1. we can't just use the default <- view of the ship, we provide a separate buy menu sprite
        # 2. we add a blue bounding box to draw into, with the extra padding
        # 2. the ship is drawn 10px inset from the left edge of bounding box

        draw_bounding_box = ImageDraw.Draw(spritesheet.sprites)
        draw_bounding_box.rectangle(
            [970, 10, 970 + 148, 10 + 48], fill=0, outline=None, width=0
        )
        crop_box_src = (
            630,
            10,
            630 + self.ship.buy_menu_width,
            10 + 48,
        )
        crop_box_dest = (
            980,
            10,
            980 + self.ship.buy_menu_width,
            10 + 48,
        )
        custom_buy_menu_sprite = spritesheet.sprites.copy().crop(crop_box_src)
        spritesheet.sprites.paste(custom_buy_menu_sprite, crop_box_dest)
        # increment x offset for pasting in next vehicle
        return spritesheet

    def render_common(self, ship, input_image, units):
        # expects to be passed a PIL Image object
        # units is a list of objects, with their config data already baked in (don't have to pass anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        output_path = os.path.join(
            currentdir, "generated", "graphics", ship.id + ".png"
        )
        spritesheet = pixa.make_spritesheet_from_image(input_image, DOS_PALETTE)

        for unit in units:
            spritesheet = unit.render(spritesheet)
        # I don't normally leave commented-out code behind, but I'm bored of looking in the PIL docs for how to show the image during compile
        # spritesheet.sprites.show()
        spritesheet.save(output_path)

    def render(self, ship):
        raise NotImplementedError("Implement me in %s" % repr(self))


class PassThroughPipeline(Pipeline):
    def __init__(self):
        # this should be sparse, don't store any ship info in Pipelines, pass at render time
        super().__init__("pass_through_pipeline")

    def render(self, ship, global_constants):
        input_image = Image.open(self.vehicle_source_input_path)
        units = []
        self.render_common(ship, input_image, units)
        input_image.close()


class ExtendSpriterowsForCompositedCargosPipeline(Pipeline):
    """ "
    Extends a cargo carrier spritesheet with variations on cargo colours.
    Quite convoluted as it handles multiple classes of cargo (bulk, piece etc)
    """

    def __init__(self):
        # this should be sparse, don't store any ship info in Pipelines, pass at render time
        # initing things here is proven to have unexpected results, as the processor will be shared across multiple vehicles
        super().__init__("extend_spriterows_for_composited_cargos_pipeline")

    def extend_base_image_to_3_rows_with_waterline_masked_per_load_state(
        self,
        base_image,
        deck_recolour_map=None,
        house_recolour_map=None,
        house_make_safe_recolour_map=None,
    ):
        # This composites the ship from:
        # - the ship base image (this contains the detail for the specific ship such as wheelhouse, holds etc)
        # - a standard hull image, including a waterline mask for each of 'loading' and 'loaded' states
        # And returns 3 rows, masked at the waterline for each of 3 load states
        # !! the naming of _base, _image, result_ etc is bad here, confusing, known issue - Oct 2020
        crop_box_hull_1 = (
            0,
            10,
            self.sprites_max_x_extent,
            10 + graphics_constants.spriterow_height,
        )
        crop_box_hull_2 = (
            0,
            10 + graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            10 + (2 * graphics_constants.spriterow_height),
        )
        crop_box_hull_3 = (
            0,
            10 + (2 * graphics_constants.spriterow_height),
            self.sprites_max_x_extent,
            10 + (3 * graphics_constants.spriterow_height),
        )

        crop_box_ship_base = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )

        # the ship image has false colour pixels for the hull, to aid drawing; remove these by converting to white, also convert any blue to white
        ship_base = base_image.point(
            lambda i: 255 if (i in range(178, 192) or i == 0) else i
        )
        """
        foo = graphics_constants.hull_recolour_CC1
        recolour_table = ProcessingUnit().make_recolour_table(foo)
        ship_base = ship_base.point(recolour_table)
        """
        # create a mask so that we paste only the ship pixels over the hull (no blue pixels)
        ship_mask = ship_base.copy()
        ship_mask = ship_mask.point(lambda i: 0 if i == 255 else 255).convert(
            "1"
        )  # the inversion here of blue and white looks a bit odd, but potato / potato

        hull_base = Image.open(self.hull_input_path)
        # hull_base uses false colour pixels for establishing correct dimensions; make these blue
        hull_image = (
            hull_base.copy()
            .crop(crop_box_hull_1)
            .point(lambda i: 0 if (i in range(215, 227) or i == 244) else i)
        )

        # directly recolour for deck, house and hull adjustments, which can be defined per ship
        # *not* for cargo-specific hull recoloring, pass cargo_recolour_maps to GestaltGraphicsSimpleColourRemaps for that case
        # Order
        # 1. house recolour map tends to use the dark red range as magic colour because it's nice to draw in
        #    but dark red may also be a destination for deck recolour, so first force the house magic red to use the spare (non-hull) purple range
        # 2. deck recolour, as it recolours arbitrary ranges, and has a chance of colliding with house and hull destination colours
        # 3. house (tends to use magic colour)
        # 4. hull (tends to use magic colour)
        recolour_maps = [
            graphics_constants.house_make_magic_red_safe_recolour_map,
            self.ship.gestalt_graphics.deck_recolour_map,
            self.ship.gestalt_graphics.house_recolour_map,
            self.ship.gestalt_graphics.hull_recolour_map,
        ]
        for recolour_map in recolour_maps:
            if recolour_map is not None:
                recolour_table = ProcessingUnit().make_recolour_table(recolour_map)
                hull_image = hull_image.point(recolour_table)
                ship_base = ship_base.point(recolour_table)
        """
        if self.ship.id == "tanker_ship_gen_3F":
            hull_image.show()
        """
        # no hull mask used for first load state (row 1), so only need to create 2 hull mask images
        waterline_mask_row_2 = (
            hull_base.copy()
            .crop(crop_box_hull_2)
            .point(lambda i: 0 if i == 226 else 255)
            .convert("1")
        )
        waterline_mask_row_3 = (
            hull_base.copy()
            .crop(crop_box_hull_3)
            .point(lambda i: 0 if i == 226 else 255)
            .convert("1")
        )

        hull_image.paste(ship_base, crop_box_ship_base, ship_mask)

        # 3 different load states to composite into result image so 3 different crop boxes to make the rows
        crop_box_comp_dest_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_2 = (
            0,
            graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_3 = (
            0,
            2 * graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            3 * graphics_constants.spriterow_height,
        )

        result_image = Image.new(
            "P", (self.sprites_max_x_extent, 3 * graphics_constants.spriterow_height)
        )
        result_image.putpalette(DOS_PALETTE)
        # by design, no mask needed for first load state
        result_image.paste(hull_image, crop_box_comp_dest_1)
        result_image.paste(hull_image, crop_box_comp_dest_2, waterline_mask_row_2)
        result_image.paste(hull_image, crop_box_comp_dest_3, waterline_mask_row_3)

        hull_base.close()
        return result_image

    def add_generic_spriterow(self):
        crop_box = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )
        vehicle_generic_spriterow_input_image = self.vehicle_base_image.crop(crop_box)
        # vehicle_generic_spriterow_input_image.show() # comment in to see the image when debugging
        vehicle_generic_spriterow_input_as_spritesheet = (
            pixa.make_spritesheet_from_image(
                vehicle_generic_spriterow_input_image, DOS_PALETTE
            )
        )
        self.units.append(
            AppendToSpritesheet(
                vehicle_generic_spriterow_input_as_spritesheet, crop_box
            )
        )
        self.units.append(
            AddCargoLabel(
                label="EMPTY",
                x_offset=self.sprites_max_x_extent + 5,
                y_offset=-1 * graphics_constants.spriterow_height,
            )
        )

    def add_livery_only_spriterows(self):
        # this might be extensible for containers when needed, using simple conditionals
        # or because containers include random options it might need reworking,
        # to be more similar to piece cargo handling, but using recolour not actual sprites
        vehicle_livery_row_image_as_spritesheet = pixa.make_spritesheet_from_image(
            self.vehicle_base_image, DOS_PALETTE
        )

        for label, recolour_map in self.ship.gestalt_graphics.cargo_recolour_maps:
            crop_box_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                3 * graphics_constants.spriterow_height,
            )
            self.units.append(
                AppendToSpritesheet(
                    vehicle_livery_row_image_as_spritesheet, crop_box_dest
                )
            )
            self.units.append(SimpleRecolour(recolour_map))
            self.units.append(
                AddCargoLabel(
                    label=label,
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * graphics_constants.spriterow_height,
                )
            )

    def add_bulk_cargo_spriterows(self):
        cargo_group_row_height = 2 * graphics_constants.spriterow_height
        crop_box_source = (
            0,
            self.base_offset,
            self.sprites_max_x_extent,
            self.base_offset + cargo_group_row_height,
        )
        vehicle_bulk_cargo_image = self.vehicle_source_image.copy().crop(
            crop_box_source
        )
        vehicle_bulk_cargo_image = vehicle_bulk_cargo_image.point(
            lambda i: 255 if (i in range(178, 192) or i == 0) else i
        )
        vehicle_bulk_cargo_mask = (
            vehicle_bulk_cargo_image.copy()
            .point(lambda i: 255 if i == 255 else 0)
            .convert("1")
        )

        vehicle_base_image = self.vehicle_base_image.copy().crop(
            (0, 100, self.sprites_max_x_extent, 300)
        )

        vehicle_bulk_cargo_image.paste(
            vehicle_base_image, None, vehicle_bulk_cargo_mask
        )

        # if self.ship.id == "freighter_ship_gen_3E":
        # vehicle_bulk_cargo_image.show()

        vehicle_bulk_cargo_input_as_spritesheet = pixa.make_spritesheet_from_image(
            vehicle_bulk_cargo_image, DOS_PALETTE
        )
        crop_box_dest = (0, 0, self.sprites_max_x_extent, cargo_group_row_height)
        for label, recolour_map in polar_fox.constants.bulk_cargo_recolour_maps:
            self.units.append(
                AppendToSpritesheet(
                    vehicle_bulk_cargo_input_as_spritesheet, crop_box_dest
                )
            )
            self.units.append(SimpleRecolour(recolour_map))
            self.units.append(
                AddCargoLabel(
                    label=label,
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * cargo_group_row_height,
                )
            )

    def add_piece_cargo_spriterows(self):
        cargo_group_output_row_height = 2 * graphics_constants.spriterow_height

        # Overview
        # 2 spriterows for the vehicle loading / loaded states, with pink loc points for cargo
        # a mask row for the vehicle, with pink mask area, which is converted to black and white mask image
        # an overlay for the vehicle, created from the vehicle empty state spriterow, and comped with the mask after each cargo has been placed
        # there is a case not handled, where long cargo sprites will cabbed vehicles in / direction with cab at N end, hard to solve
        crop_box_vehicle_cargo_loc_row = (
            0,
            self.base_offset,
            self.sprites_max_x_extent,
            self.base_offset + graphics_constants.spriterow_height,
        )
        vehicle_cargo_loc_image = self.vehicle_source_image.copy().crop(
            crop_box_vehicle_cargo_loc_row
        )
        # get the loc points
        loc_points = [
            pixel for pixel in pixa.pixascan(vehicle_cargo_loc_image) if pixel[2] == 226
        ]
        # two cargo rows needed, so extend the loc points list
        loc_points.extend(
            [
                (pixel[0], pixel[1] + graphics_constants.spriterow_height, pixel[2])
                for pixel in loc_points
            ]
        )
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])

        crop_box_mask = (
            0,
            self.base_offset + graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            self.base_offset + (2 * graphics_constants.spriterow_height),
        )
        vehicle_base_image = self.vehicle_base_image.copy().crop(
            (0, 100, self.sprites_max_x_extent, 300)
        )
        vehicle_mask_base_image = (
            self.vehicle_source_image.copy()
            .crop(crop_box_mask)
            .point(lambda i: 255 if i == 226 else 0)
            .convert("1")
        )
        vehicle_mask = Image.new(
            "1", (self.sprites_max_x_extent, cargo_group_output_row_height)
        )
        crop_box_mask_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            0 + graphics_constants.spriterow_height,
        )
        crop_box_mask_2 = (
            0,
            0 + graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            0 + (2 * graphics_constants.spriterow_height),
        )

        vehicle_mask.paste(vehicle_mask_base_image, crop_box_mask_1)
        vehicle_mask.paste(vehicle_mask_base_image, crop_box_mask_2)
        # vehicle_mask.show()

        crop_box_comp_dest_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )
        vehicle_cargo_rows_image = Image.new(
            "P", (self.sprites_max_x_extent, cargo_group_output_row_height)
        )
        vehicle_cargo_rows_image.putpalette(DOS_PALETTE)
        # paste empty states in for the cargo rows (base image = empty state)
        vehicle_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_1)
        # vehicle_cargo_rows_image.show()
        crop_box_dest = (0, 0, self.sprites_max_x_extent, cargo_group_output_row_height)

        piece_cargo_sprites = PieceCargoSprites(
            polar_fox_constants=polar_fox.constants,
            polar_fox_graphics_path=os.path.join("src", "polar_fox", "graphics"),
        )

        for cargo_filename in polar_fox.constants.piece_vehicle_type_to_sprites_maps[
            self.ship.gestalt_graphics.piece_type
        ]:

            cargo_sprites = piece_cargo_sprites.get_cargo_sprites_all_angles_for_length(
                cargo_filename, self.ship.cargo_length
            )

            vehicle_comped_image = vehicle_cargo_rows_image.copy()
            for pixel in loc_points:
                angle_num = 0
                for counter, bbox in enumerate(
                    self.global_constants.spritesheet_bounding_boxes
                ):
                    if pixel[0] >= bbox[0]:
                        angle_num = counter
                # clamp angle_num to 4, cargo sprites are symmetrical, only 4 angles provided
                if angle_num > 3:
                    angle_num = angle_num % 4
                cargo_sprite_num = angle_num
                # loaded sprites are the second block of 4 in the cargo sprites list
                if pixel[1] >= graphics_constants.spriterow_height:
                    cargo_sprite_num = cargo_sprite_num + 4
                cargo_width = cargo_sprites[cargo_sprite_num][0].size[0]
                cargo_height = cargo_sprites[cargo_sprite_num][0].size[1]
                # the +1s for height adjust the crop box to include the loc point
                # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
                cargo_bounding_box = (
                    pixel[0],
                    pixel[1] - cargo_height + 1,
                    pixel[0] + cargo_width,
                    pixel[1] + 1,
                )
                vehicle_comped_image.paste(
                    cargo_sprites[cargo_sprite_num][0],
                    cargo_bounding_box,
                    cargo_sprites[cargo_sprite_num][1],
                )
                # if self.ship.id == 'universal_freighter_D' and cargo_filename == 'barrels_silver':
                # cargo_sprites[cargo_sprite_num][0].show()
            # vehicle overlay with mask - overlays any areas where cargo shouldn't show
            vehicle_comped_image.paste(
                vehicle_base_image, crop_box_comp_dest_1, vehicle_mask
            )
            # if self.ship.id == 'universal_freighter_D':
            # vehicle_comped_image.show()
            vehicle_comped_image_as_spritesheet = pixa.make_spritesheet_from_image(
                vehicle_comped_image, DOS_PALETTE
            )
            self.units.append(
                AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_dest)
            )
            self.units.append(
                AddCargoLabel(
                    label=cargo_filename,
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * cargo_group_output_row_height,
                )
            )

    def render(self, ship, global_constants):
        self.hull_input_path = os.path.join(
            currentdir, "src", "graphics", "hulls", ship.hull_spritesheet_name + ".png"
        )
        self.units = []
        self.global_constants = global_constants
        self.ship = ship
        self.sprites_max_x_extent = self.global_constants.sprites_max_x_extent

        self.vehicle_source_image = Image.open(self.vehicle_source_input_path)

        crop_box_source = (
            0,
            10,
            self.sprites_max_x_extent,
            10 + graphics_constants.spriterow_height,
        )
        # create a base vehicle image by comping in hull, with empty / loading / loaded hull states
        self.vehicle_base_image = (
            self.extend_base_image_to_3_rows_with_waterline_masked_per_load_state(
                self.vehicle_source_image.copy().crop(crop_box_source)
            )
        )
        # the cumulative_input_spriterow_count updates per processed group of spriterows, and is key to making this work
        cumulative_input_spriterow_count = 0
        for vehicle_counter, vehicle_rows in enumerate(ship.get_spriterow_counts()):
            self.cur_vehicle_empty_row_offset = (
                10
                + cumulative_input_spriterow_count * graphics_constants.spriterow_height
            )
            for spriterow_data in vehicle_rows:
                spriterow_type = spriterow_data[0]
                self.base_offset = 10 + (
                    graphics_constants.spriterow_height
                    * cumulative_input_spriterow_count
                )
                if (
                    spriterow_type == "always_use_same_spriterow"
                    or spriterow_type == "empty"
                ):
                    input_spriterow_count = 1
                    self.add_generic_spriterow()
                elif spriterow_type == "livery_only":
                    input_spriterow_count = 1
                    self.add_livery_only_spriterows()
                elif spriterow_type == "bulk_cargo":
                    input_spriterow_count = 2
                    self.add_bulk_cargo_spriterows()
                elif spriterow_type == "piece_cargo":
                    input_spriterow_count = 2
                    self.add_piece_cargo_spriterows()
                cumulative_input_spriterow_count += input_spriterow_count

        self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        # for this pipeline, input_image is just blank white 10px high image, to which the vehicle sprites are then appended
        input_image = Image.new("P", (graphics_constants.spritesheet_width, 10), 255)
        input_image.putpalette(DOS_PALETTE)
        self.render_common(ship, input_image, self.units)
        self.vehicle_source_image.close()


def get_pipeline(pipeline_name):
    # return a pipeline by name;
    # add pipelines here when creating new ones
    for pipeline in [
        PassThroughPipeline(),
        ExtendSpriterowsForCompositedCargosPipeline(),
    ]:
        if pipeline_name == pipeline.name:
            return pipeline
    raise Exception("Pipeline not found: " + pipeline_name)  # should never get to here


def main():
    print("yeah, pipelines.main() does nothing")


if __name__ == "__main__":
    main()
