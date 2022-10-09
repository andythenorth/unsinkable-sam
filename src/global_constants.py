# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

grfid = r"\55\53\53\33"

metadata = {
    "dev_thread_url": "https://www.tt-forums.net/viewtopic.php?f=26&t=75762",
    "repo_url": "https://github.com/andythenorth/unsinkable-sam",
    "docs_url": "https://grf.farm/unsinkable-sam",
}

buy_menu_sort_order_ships = [
    "pax_fast_loading",
    "pax_luxury",
    "mail_ship",
    "utility_hovercraft",
    "freighter_ship",
    "merchandise_freighter_ship",
    "freighter_barge",
    "cargo_liner",
    "bulk_ship",
    "scrap_carrier_ship",
    "bulk_barge",
    "tanker_ship",
    "tanker_barge",
    "cryo_tanker",
    "livestock_carrier",
    "edibles_tanker",
    "reefer",
    "trawler",
]

# generalised mapping of base_id to role groups
# order is significant, of both dict and base_id lists
role_group_mapping = {
    "pax": ["pax_fast_loading", "pax_luxury"],
    "mail_utility": ["mail_ship"],
    "dry_cargo": [
        "freighter_ship",
        "merchandise_freighter_ship",
        "freighter_barge",
        "cargo_liner",
        "bulk_ship",
        "scrap_carrier_ship",
        "bulk_barge",
    ],
    "liquid_bulk": [
        "tanker_ship",
        "tanker_barge",
        "cryo_tanker",
    ],
    "foodstuffs": [
        "reefer",
        "edibles_tanker",
    ],
    "specialist": ["livestock_carrier", "trawler"],
}

# custom remappings of cc1/cc2, used in recolour_sprites, not used in graphics generation, so not in graphics_constants
# post python 3.7, we rely on dict order being stable here, so we can get keys by position when we need to
custom_ship_recolour_sprite_maps = {
    "custom_dark_brown": (105, 106, 33, 34, 35, 36, 37, 38),
    "custom_bauxite": (60, 61, 73, 62, 75, 76, 77, 78),
    "custom_dark_pink": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_light_pink": (43, 44, 45, 46, 47, 166, 167, 168),
    "custom_dark_grey": (3, 16, 17, 18, 19, 20, 21, 22),
    "custom_dark_yellow": (60, 61, 62, 64, 65, 66, 67, 68),
    "custom_dark_white": (18, 7, 8, 10, 11, 12, 13, 14),
    "custom_light_purple": (136, 170, 171, 172, 173, 174, 175, 176),
    "custom_light_mauve": (129, 130, 131, 132, 133, 134, 135, 14),
    "custom_dark_orange": (62, 63, 64, 193, 194, 195, 196, 197),
    "custom_dark_cream": (112, 113, 114, 116, 117, 118, 119, 120),
    # can't name it dark_green cos that conflates with DARK_GREEN
    "custom_green": (
        80,
        82,
        83,
        84,
        85,
        86,
        207,
        209,
    ),
    # can't name it dark_blue cos that conflates with DARK_BLUE
    "custom_blue": (
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        210,
    ),
    # can't name it dark_light_blue cos that would be silly
    "custom_light_blue": (
        155,
        156,
        157,
        158,
        159,
        160,
        161,
        210,
    ),
    # can't name it light_dark_blue cos that would be silly
    "custom_dark_blue": (
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        152,
    ),
    "custom_dark_red": (180, 181, 182, 183, 164, 165, 166, 167),
    "custom_pale_green": (97, 98, 99, 100, 101, 102, 103, 14),
    "custom_dark_green": (89, 90, 91, 92, 93, 94, 95, 31),
}

# up to 127 temp storages are available, might as well allocate them exclusively within the graphics chain to avoid any collisions
temp_storage_ids = dict(
    cc_num_to_randomise=0,  # used in procedures_colour_randomisation_strategies
    auto_colour_randomisation_strategy_num=1,  # used in procedures_colour_randomisation_strategies
)

# cargo aging constant - OTTD default is 185 - dibble this up in favour of ships, as they are relatively slow
CARGO_AGE_PERIOD = 370

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = (
    (20, 28, 89),
    (60, 113, 66),
    (190, 128, 48),
    (330, 113, 66),
    (460, 28, 89),
    (500, 113, 66),
    (630, 128, 48),
    (770, 113, 66),
)

# standard vehicle offsets; custom can be supported if needed by extending ship.offsets
vehicle_offsets = {
    "32px": [
        [-14, -73],
        [-44, -38],
        [-22, -36],
        [8, -38],
        [-14, -73],
        [-42, -38],
        [-22, -36],
        [8, -38],
    ],
    "44px": [
        [-14, -73],
        [-44, -38],
        [-22, -36],
        [8, -38],
        [-14, -73],
        [-42, -38],
        [-22, -36],
        [8, -38],
    ],
    "64px": [
        [-14, -68],
        [-50, -35],
        [-32, -34],
        [3, -34],
        [-14, -68],
        [-50, -35],
        [-32, -34],
        [3, -34],
    ],
    "80px": [
        [-14, -58],
        [-55, -31],
        [-40, -36],
        [-3, -31],
        [-14, -58],
        [-55, -31],
        [-40, -36],
        [-3, -31],
    ],
    "96px": [
        [-14, -58],
        [-59, -29],
        [-48, -36],
        [-8, -29],
        [-14, -58],
        [-61, -29],
        [-48, -36],
        [-9, -29],
    ],
    "112px": [
        [-14, -52],
        [-64, -26],
        [-56, -34],
        [-12, -25],
        [-14, -52],
        [-70, -25],
        [-56, -34],
        [-16, -25],
    ],
    "128px": [
        [-14, -46],
        [-70, -23],
        [-64, -34],
        [-18, -23],
        [-14, -46],
        [-72, -23],
        [-64, -34],
        [-18, -23],
    ],
}

buy_menu_sprite_x_loc = 970
buy_menu_sprite_width = 128
buy_menu_sprite_height = 32
sprites_max_x_extent = 885
docs_ship_image_height = (
    32  # show the full ship (assuming no ships taller than 32px in – view)
)

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants

base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
default_cargos = polar_fox.constants.default_cargos
allowed_refits_by_label = polar_fox.constants.allowed_refits_by_label
disallowed_refits_by_label = polar_fox.constants.disallowed_refits_by_label
generated_files_dir = polar_fox.constants.generated_files_dir
graphics_path = polar_fox.constants.graphics_path
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date
company_colour_maps = polar_fox.constants.company_colour_maps
