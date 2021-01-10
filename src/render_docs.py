import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
from time import time
from PIL import Image
import markdown

import global_constants
import utils as utils
import unsinkable_sam
from polar_fox import git_info

# !! this is done differently in iron horse, with registered fetched from iron_horse module
from rosters import registered_rosters

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()
metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

docs_src = os.path.join(currentdir, "src", "docs_templates")

# palette = utils.dos_palette_to_rgb()


class DocHelper(object):
    # dirty class to help do some doc formatting

    def get_ships_by_subclass(self, ships):
        # first find all the subclasses + their vehicles
        ships_by_subclass = {}
        for ship in ships:
            subclass = type(ship)
            if subclass in ships_by_subclass:
                ships_by_subclass[subclass].append(ship)
            else:
                ships_by_subclass[subclass] = [ship]
        # reformat to a list we can then sort so order is consistent
        result = [
            {
                "name": i.__name__,
                "doc": i.__doc__,
                "class_obj": subclass,
                "ships": ships_by_subclass[i],
            }
            for i in ships_by_subclass
        ]
        return sorted(result, key=lambda subclass: subclass["name"])

    def get_roster_name(self, index):
        return base_lang_strings.get("STR_PARAM_ROSTER_OPTION_" + str(index), "")

    def get_roster_by_id(self, roster_id, registered_rosters):
        for roster in registered_rosters:
            if roster.id == roster_id:
                return roster
        # default result
        return None

    def fetch_prop(self, result, prop_name, value):
        result["ship"][prop_name] = value
        result["subclass_props"].append(prop_name)
        return result

    def unpack_name_suffix(self, name_suffix_as_string_name):
        try:
            return base_lang_strings[name_suffix_as_string_name]
        except:
            # no good solution currently for
            # 1. names for roles that are consistent, but ship model name suffixes change (Collier vs. Mini Bulker)
            # 2. no ship in scope
            # probably need a separate set of strings for the role?  Parent types?
            utils.echo_message("Can't return name suffix for " + name_suffix_as_string_name)
            return "CABBAGE"

    def unpack_name_string(self, ship):
        return ship._name + " " + self.unpack_name_suffix(ship.name_suffix_as_string_name)

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for ship in subclass["ships"]:
            result = {"ship": {}, "subclass_props": []}

            result = self.fetch_prop(result, "Ship Name", self.unpack_name_string(ship))
            result = self.fetch_prop(result, "Subtype", ship.subtype)
            result = self.fetch_prop(
                result, "Extra Info", base_lang_strings[ship.get_str_type_info()]
            )
            result = self.fetch_prop(result, "Speed Laden", int(ship.speed))
            result = self.fetch_prop(result, "Intro Date", ship.intro_date)
            result = self.fetch_prop(result, "Vehicle Life", ship.vehicle_life)
            result = self.fetch_prop(result, "Capacity", ship.default_capacity)
            result = self.fetch_prop(result, "Buy Cost", ship.buy_cost)
            result = self.fetch_prop(result, "Running Cost", ship.running_cost)
            result = self.fetch_prop(result, "Loading Speed", ship.loading_speed)

            props_to_print[ship] = result["ship"]
            props_to_print[subclass["name"]] = result["subclass_props"]

        return props_to_print

    def get_base_numeric_id(self, vehicle):
        return vehicle.numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]

    def ships_as_tech_tree(self, ships):
        # !! does not handle roster at time of writing
        # structure
        #    |- role_group
        #       |- base_id (role)
        #          |- generation
        #             |- ship
        # if there's no ship matching a combination of keys in the tree, there will be a None entry for that node in the tree, to ease walking the tree
        result = {}
        # much nested loops
        for role_group in global_constants.role_group_mapping:
            role_branches = {}
            for role in global_constants.role_group_mapping[role_group]:
                role_branches[role] = {}
                # hard-coded for now, move to global constants another day
                for subtype in ["A", "B", "C", "D", "E", "F"]:
                    subtype_branch = {}
                    # walk the generations, providing default None objects
                    for gen in range(
                        1,
                        len(
                            self.get_roster_by_id(
                                "default", unsinkable_sam.registered_rosters
                            ).intro_dates["DEFAULT"]
                        )
                        + 1,
                    ):
                        subtype_branch[gen] = None
                    # get the ships matching this role
                    for ship in ships:
                        if ship.base_id == role and ship.subtype == subtype:
                            subtype_branch[ship.gen] = ship
                    # to prevent empty rows in tech tree, only include the subtype_branch if it contains actual ships
                    if set(subtype_branch.values()) != {None}:
                        role_branches[role][subtype] = subtype_branch
            result[role_group] = role_branches
        return result


def render_docs(
    doc_list,
    file_type,
    docs_output_path,
    ships,
    use_markdown=False,
    source_is_repo_root=False,
):
    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(doc_path, format="text")

    for doc_name in doc_list:
        template = docs_templates[
            doc_name + ".pt"
        ]  # .pt is the conventional extension for chameleon page templates
        doc = template(
            ships=ships,
            registered_rosters=registered_rosters,
            global_constants=global_constants,
            makefile_args=makefile_args,
            git_info=git_info,
            base_lang_strings=base_lang_strings,
            metadata=metadata,
            utils=utils,
            doc_helper=DocHelper(),
            doc_name=doc_name,
        )
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates["markdown_wrapper.pt"]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                global_constants=global_constants,
                makefile_args=makefile_args,
                git_info=git_info,
                metadata=metadata,
                utils=utils,
                doc_helper=DocHelper(),
                doc_name=doc_name,
            )
        if file_type == "html":
            subdir = "html"
        else:
            subdir = ""
        # save the results of templating
        doc_file = codecs.open(
            os.path.join(docs_output_path, subdir, doc_name + "." + file_type),
            "w",
            "utf8",
        )
        doc_file.write(doc)
        doc_file.close()


def render_docs_vehicle_details(ship, docs_output_path, ships):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates["vehicle_details.pt"]
    doc_name = ship.id
    doc = template(
        ship=ship,
        ships=ships,
        global_constants=global_constants,
        registered_rosters=unsinkable_sam.registered_rosters,
        makefile_args=makefile_args,
        git_info=git_info,
        base_lang_strings=base_lang_strings,
        metadata=metadata,
        utils=utils,
        doc_helper=DocHelper(),
        doc_name=doc_name,
    )
    doc_file = codecs.open(
        os.path.join(docs_output_path, "html", doc_name + ".html"), "w", "utf8"
    )
    doc_file.write(doc)
    doc_file.close()


def render_docs_images(docs_output_path, ships):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    vehicle_graphics_src = os.path.join(currentdir, "generated", "graphics")
    buy_menu_bb = global_constants.spritesheet_bounding_boxes[6]
    for ship in ships:
        vehicle_spritesheet = Image.open(
            os.path.join(vehicle_graphics_src, ship.id + ".png")
        )
        processed_vehicle_image = vehicle_spritesheet.crop(
            box=(
                buy_menu_bb[0],
                10
                + global_constants.spritesheet_bounding_boxes[2][2]
                - global_constants.docs_ship_image_height,
                buy_menu_bb[0] + ship.buy_menu_width,
                10 + global_constants.spritesheet_bounding_boxes[2][2],
            )
        )
        # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
        processed_vehicle_image = processed_vehicle_image.resize(
            (
                4 * ship.buy_menu_width,
                4 * global_constants.buy_menu_sprite_height,
            ),
            resample=Image.NEAREST,
        )

        output_path = os.path.join(
            currentdir,
            "docs",
            "html",
            "static",
            "img",
            ship.id + ".png",
            # ship.id + "_" + colour_name + ".png",
        )
        processed_vehicle_image.save(output_path, optimize=True, transparency=0)


def main():
    print("[RENDER DOCS] render_docs.py")
    start = time()
    unsinkable_sam.main()

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir
    )
    if not os.path.exists(chameleon_cache_path):
        os.mkdir(chameleon_cache_path)
    os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

    docs_output_path = os.path.join(currentdir, "docs")
    if os.path.exists(docs_output_path):
        shutil.rmtree(docs_output_path)
    os.mkdir(docs_output_path)

    shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)

    static_dir_src = os.path.join(docs_src, "html", "static")
    static_dir_dst = os.path.join(docs_output_path, "html", "static")
    shutil.copytree(static_dir_src, static_dir_dst)

    ships = unsinkable_sam.get_ships_in_buy_menu_order()
    # default sort for docs is by ship intro date
    ships = sorted(ships, key=lambda ship: ship.intro_date)

    dates = sorted([i.intro_date for i in ships])
    metadata["dates"] = (dates[0], dates[-1])

    # render standard docs from a list
    html_docs = [
        "ships",
        "code_reference",
        "get_started",
        "translations",
        "tech_tree_table_blue",
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]

    render_docs(html_docs, "html", docs_output_path, ships)
    render_docs(txt_docs, "txt", docs_output_path, ships)
    render_docs(
        license_docs,
        "txt",
        docs_output_path,
        ships,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, "txt", docs_output_path, ships)
    render_docs(markdown_docs, "html", docs_output_path, ships, use_markdown=True)

    # render vehicle details
    for ship in ships:
        render_docs_vehicle_details(ship, docs_output_path, ships)

    # process images for use in docs
    render_docs_images(docs_output_path, ships)
    # eh, how long does this take anyway?
    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
