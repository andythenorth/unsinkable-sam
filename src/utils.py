import os.path
import global_constants
import codecs  # used for writing files - more unicode friendly than standard open() module
from polar_fox import git_info


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


def unescape_chameleon_output(escaped_nml):
    # first drop as much whitespace as we sensibly can
    # in tests, this doesn't make the compile any faster at all, but it reduced firs.nml (v3.0.4) from 326k lines to 226k lines,
    escaped_nml = "\n".join(
        [x for x in escaped_nml.split("\n") if x.strip(" \t\n\r") != ""]
    )
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = ">".join(escaped_nml.split("&gt;"))
    escaped_nml = "<".join(escaped_nml.split("&lt;"))
    escaped_nml = "&".join(escaped_nml.split("&amp;"))
    return escaped_nml


def parse_base_lang():
    # expose base lang strings to python - for reuse in docs
    base_lang_file = codecs.open(
        os.path.join("src", "lang", "english.lng"), "r", "utf8"
    )
    text = base_lang_file.readlines()
    # this is fragile, playing one line python is silly :)
    strings = dict(
        (line.split(":", 1)[0].strip(), line.split(":", 1)[1].strip())
        for line in text
        if ":" in line
    )
    return strings


def echo_message(message):
    # use to raise messages from templates to standard out (can't print directly from template render)
    # magically wraps these messages in ANSI colour to make them visible - they are only intended for noticeable messages, not general output
    print("\033[33m" + message + "\033[0m")


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
