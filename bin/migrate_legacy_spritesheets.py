import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path
import shutil

import unsinkable_sam
import global_constants
from PIL import Image, ImageDraw

spriterow_height = 100
DOS_PALETTE = Image.open("palette_key.png").palette

input_graphics_dir = os.path.join("src", "graphics")
output_graphics_dir = os.path.join("src", "graphics", "migrated")

col_insertion_points = (
    [20, 0],
    [60, 0],
    [190, 0],
    [330, 0],
    [460, 0],
    [500, 0],
    [630, 0],
    [770, 0],
)

def get_legacy_bounding_boxes(y=0):
    return [
        (20, y, 28, 89),
        (60, y, 113, 66),
        (186, y, 128, 48),
        (318, y, 113, 66),
        (444, y, 28, 89),
        (484, y, 113, 66),
        (610, y, 128, 48),
        (742, y, 113, 66),
    ]


def recomp_legacy_spriterows(row_count, spriterow, migrated_spritesheet):
    base_template_spritesheet = Image.open(
        os.path.join("src", "graphics", "base_spritesheet.png")
    )
    migrated_spriterow = base_template_spritesheet.crop((0, 10, 900, 120))
    # we only want the first row to show blue bounding box for buy menu, so draw white rectangle over it for other rows
    for col_count, vertexes in enumerate(get_legacy_bounding_boxes()):
        crop_box = (
            vertexes[0],
            vertexes[1],
            vertexes[0] + vertexes[2],
            vertexes[1] + vertexes[3],
        )
        sprite = spriterow.crop(crop_box)
        # sprite.show()
        # don't paste if the sprite only contains blue or white
        only_blue_and_white = True
        for colour in list(sprite.getdata()):
            if colour > 0 and colour < 255:
                only_blue_and_white = False
        if not only_blue_and_white:
            col_insert_loc = col_insertion_points[col_count]
            migrated_spriterow.paste(sprite, (col_insert_loc[0], col_insert_loc[1]))
    row_insert_loc = (0, 10 + row_count * spriterow_height)
    migrated_spritesheet.paste(migrated_spriterow, row_insert_loc)
    return migrated_spritesheet


def migrate_spritesheet(rows_with_valid_content):
    new_height = 10 + spriterow_height * len(rows_with_valid_content) + 500
    migrated_spritesheet = Image.new("P", (1200, new_height), 255)
    migrated_spritesheet.putpalette(DOS_PALETTE)
    for row_count, spriterow in enumerate(rows_with_valid_content):
        migrated_spritesheet = recomp_legacy_spriterows(
            row_count, spriterow, migrated_spritesheet
        )
    return migrated_spritesheet


def detect_spriterows_with_content(subdir, filename):
    legacy_spritesheet = Image.open(os.path.join(input_graphics_dir, subdir, filename))
    base_y = 10
    rows_with_valid_content = []
    while base_y + spriterow_height < legacy_spritesheet.size[1]:
        crop_box = (0, base_y, legacy_spritesheet.size[0], base_y + spriterow_height)
        test_row = legacy_spritesheet.crop(crop_box)
        base_y += spriterow_height

        only_blue_and_white = True
        for colour in list(test_row.getdata()):
            if colour > 0 and colour < 255:
                only_blue_and_white = False
        if not only_blue_and_white:
            # row contains _some_ colours other than white and blue, now check if it contains any blue, or if it's just leftover parts from drawing
            if min(list(test_row.getdata())) > 0:
                # there is no blue, this is just leftover parts, so show this image so it can be cleaned up manually
                #test_row.show()
                print(filename, "contains some orphaned / leftover / junk pixels")
            else:
                rows_with_valid_content.append(test_row)
    return rows_with_valid_content


def main():
    unsinkable_sam.main()
    if os.path.exists(output_graphics_dir):
        shutil.rmtree(output_graphics_dir)
    os.mkdir(output_graphics_dir)

    ship_filenames = []
    ships = unsinkable_sam.get_ships_in_buy_menu_order()
    for ship in ships:
        for i in range(2):
            filename = os.path.join(ship.id + ".png")
            if os.path.isfile(os.path.join(input_graphics_dir, 'ships', filename)):
                ship_filenames.append(filename)
    ship_filenames.sort()

    for filename in ship_filenames:
        output_path = os.path.join(output_graphics_dir, filename)
        rows_with_valid_content = detect_spriterows_with_content('ships', filename)
        migrated_spritesheet = migrate_spritesheet(rows_with_valid_content)
        migrated_spritesheet.save(output_path)

    print("Migrated ships count:", len(ship_filenames))

    hull_filenames = []
    hulls = unsinkable_sam.registered_hulls
    print(hulls)
    for hull in hulls.values():
        for i in range(2):
            filename = os.path.join(hull.spritesheet_name + ".png")
            if os.path.isfile(os.path.join(input_graphics_dir, 'hulls', filename)):
                hull_filenames.append(filename)
    hull_filenames.sort()

    for filename in hull_filenames:
        output_path = os.path.join(output_graphics_dir, filename)
        rows_with_valid_content = detect_spriterows_with_content('hulls', filename)
        migrated_spritesheet = migrate_spritesheet(rows_with_valid_content)
        migrated_spritesheet.save(output_path)

    print("Migrated hulls count:", len(hull_filenames))

if __name__ == "__main__":
    main()
