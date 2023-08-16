import os.path
import tomllib

currentdir = os.curdir

import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import (
    unwrap_nml_string_declaration as unwrap_nml_string_declaration,
)


def get_makefile_args(sys):
    # get args passed by makefile
    if len(sys.argv) > 1:
        makefile_args = {
            "num_pool_workers": int(sys.argv[1]),
            "roster": sys.argv[2],
            "suppress_cargo_sprites": True if sys.argv[3] == "True" else False,
        }
    else:
        # provide any essential defaults here
        makefile_args = {}
    return makefile_args


def get_docs_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(git_info.get_tag_exact_match())
    result.append("index.html")
    return "/".join(result)


def get_lang_data(lang, ships):
    global_pragma = {}
    lang_strings = {}
    with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
        lang_source = tomllib.load(fp)

    for node_name, node_value in lang_source.items():
        if node_name == "GLOBAL_PRAGMA":
            # explicit handling of global pragma items
            global_pragma["grflangid"] = node_value["grflangid"]
            global_pragma["plural"] = node_value["plural"]
            if node_value.get("gender", False):
                global_pragma["gender"] = node_value["gender"]
            if node_value.get("case", False):
                global_pragma["case"] = node_value["case"]
        else:
            # this assumes only one roster, no string over-rides, but check Iron Horse if multi-roster support is needed
            lang_strings[node_name] = node_value["base"]

    for ship in ships:
        if ship._name is not None:
            lang_strings["STR_NAME_" + ship.id.upper()] = ship._name + " {STRING}"

    return {"global_pragma": global_pragma, "lang_strings": lang_strings}


def unpack_colour(colour_name, cc_to_remap):
    # seems utils is the best place to keep this, but eh
    if "COLOUR_" in colour_name:
        # assume it's a default CC name constant
        if cc_to_remap == 1:
            return "palette_2cc(" + colour_name + ", company_colour2)"
        if cc_to_remap == 2:
            return "palette_2cc(company_colour1, " + colour_name + ")"
    else:
        # assume custom colour
        colour_name_offset = 2 * list(
            global_constants.custom_ship_recolour_sprite_maps.keys()
        ).index(colour_name)
        remap_index = colour_name_offset + cc_to_remap - 1
        # return an nml fragment: custom_ship_recolour_sprites + index into recolour sprite + [company_colour1 or company_colour2]
        return (
            "custom_ship_recolour_sprites + "
            + str(16 * remap_index)
            + " + company_colour"
            + str(1 if cc_to_remap == 2 else 2)
        )
