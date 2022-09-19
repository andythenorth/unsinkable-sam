import os.path
import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import unwrap_nml_string_declaration as unwrap_nml_string_declaration


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


def parse_base_lang():
    # expose base lang strings to python - for reuse in docs
    with open(
        os.path.join("src", "lang", "english.lng"), "r", encoding="utf8"
    ) as base_lang_file:
        strings = {}
        for line in base_lang_file:
            if ":" in line:
                strings[line.split(":", 1)[0].strip()] = line.split(":", 1)[1].strip()
        return strings


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
