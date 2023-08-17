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
    "product_tanker_ship",
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
        "product_tanker",
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
    "custom_dark_pink": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_light_pink": (43, 44, 45, 46, 47, 166, 167, 168),
    "custom_grey": (33, 34, 6, 7, 20, 21, 22, 39),
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
    # tried darker bauxite colours, doesn't work well
    "custom_bauxite": (70, 71, 122, 124, 75, 126, 77, 78),
    "custom_light_bauxite": (71, 122, 74, 125, 76, 127, 78, 79),
    "custom_nightshade": (104, 2, 25, 17, 18, 19, 20, 10),
    "custom_light_nightshade": (1, 2, 106, 17, 18, 7, 20, 10),
    "custom_teal": (88, 97, 98, 157, 158, 159, 160, 103),
    "custom_dark_teal": (88, 97, 156, 157, 158, 101, 102, 103),
    "custom_violet": (136, 170, 171, 172, 173, 174, 175, 176),  # WIP, may need improved
    "custom_dark_violet": (
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        14,
    ),  # WIP, may need improved
    "custom_silver": (2, 18, 19, 20, 21, 22, 23, 14),
    "custom_dark_silver": (2, 4, 35, 19, 21, 22, 23, 14),
    "custom_pewter": (2, 3, 18, 19, 20, 21, 22, 13),
    "custom_dark_pewter": (2, 114, 18, 19, 20, 21, 22, 13),
    "custom_sulphur": (62, 62 + 1, 62 + 2, 62 + 3, 62 + 4, 62 + 5, 62 + 6, 62 + 7),
    "custom_dark_sulphur": (62, 62 + 1, 62 + 2, 193, 194, 50, 51, 52),
    "custom_ruby": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_faded_ruby": (71, 72, 73, 43, 44, 76, 77, 47),
    "custom_oil_black": (1, 2, 3, 4, 5, 6, 7, 8),
    "custom_faded_oil_black": (1, 70, 16, 4, 26, 6, 7, 8),
    "custom_rusty_black": (70, 71, 33, 5, 6, 35, 7, 8),
    "custom_faded_rusty_black": (70, 71, 32, 26, 6, 34, 7, 8),
    "custom_gremlin_green": (24, 25, 26, 27, 28, 29, 30, 31),
    "custom_faded_gremlin_green": (24, 25, 26, 109, 28, 29, 59, 103),
    "custom_ochre": (60, 61, 62, 63, 192, 193, 194, 196),
    "custom_faded_ochre": (60, 61, 62, 117, 192, 193, 196, 197),
}

# shared colour sets with variants of CC, may be used by multiple strategies, not used in graphics generation, so not in graphics_constants
# post python 3.7, we rely on dict order being stable here, so we can get keys by position when we need to
colour_sets = {
    "dark_blue": ["COLOUR_DARK_BLUE", "custom_dark_blue"],
    "pale_green": ["COLOUR_PALE_GREEN", "custom_pale_green"],
    "pink": ["COLOUR_PINK", "custom_dark_pink"],
    "yellow": ["COLOUR_YELLOW", "custom_dark_yellow"],
    "red": ["COLOUR_RED", "custom_dark_red"],
    "light_blue": ["COLOUR_LIGHT_BLUE", "custom_light_blue"],
    "green": ["COLOUR_GREEN", "custom_green"],
    "dark_green": ["COLOUR_DARK_GREEN", "custom_dark_green"],
    "blue": ["COLOUR_BLUE", "custom_blue"],
    "cream": ["COLOUR_CREAM", "custom_dark_cream"],
    "mauve": ["COLOUR_MAUVE", "custom_light_mauve"],
    "purple": ["COLOUR_PURPLE", "custom_light_purple"],
    "orange": ["COLOUR_ORANGE", "custom_dark_orange"],
    "brown": ["COLOUR_BROWN", "custom_dark_brown"],
    "grey": ["COLOUR_GREY", "custom_dark_grey"],
    "white": ["COLOUR_WHITE", "custom_dark_white"],
    "freight_bauxite": ["custom_bauxite", "custom_light_bauxite"],
    "freight_grey": ["custom_grey", "COLOUR_GREY"],
    "freight_nightshade": ["custom_nightshade", "custom_light_nightshade"],
    "freight_teal": ["custom_teal", "custom_dark_teal"],
    "freight_violet": ["custom_violet", "custom_dark_violet"],
    "freight_silver": ["custom_silver", "custom_dark_silver"],
    "freight_pewter": ["custom_pewter", "custom_dark_pewter"],
    "freight_sulphur": ["custom_sulphur", "custom_dark_sulphur"],
    "freight_straw": ["COLOUR_BROWN", "COLOUR_CREAM"],
    "freight_ruby": ["custom_ruby", "custom_faded_ruby"],
    "freight_oil_black": ["custom_oil_black", "custom_faded_oil_black"],
    "freight_rusty_black": ["custom_rusty_black", "custom_faded_rusty_black"],
    "freight_gremlin_green": ["custom_gremlin_green", "custom_faded_gremlin_green"],
    "freight_ochre": ["custom_ochre", "custom_faded_ochre"],
    "freight_sand": ["COLOUR_BROWN", "custom_dark_brown"],
}

# select a colour that matches the current company colour
# current company colour: complementary colour
complements_to_company_colours = {
    "COLOUR_DARK_BLUE": "COLOUR_BLUE",
    "COLOUR_PALE_GREEN": "COLOUR_GREEN",
    "COLOUR_PINK": "COLOUR_RED",
    "COLOUR_YELLOW": "COLOUR_ORANGE",
    "COLOUR_RED": "COLOUR_PINK",
    "COLOUR_LIGHT_BLUE": "COLOUR_BLUE",
    "COLOUR_GREEN": "COLOUR_DARK_GREEN",
    "COLOUR_DARK_GREEN": "COLOUR_GREEN",
    "COLOUR_BLUE": "COLOUR_DARK_BLUE",
    "COLOUR_CREAM": "COLOUR_BROWN",
    "COLOUR_MAUVE": "COLOUR_PURPLE",
    "COLOUR_PURPLE": "COLOUR_MAUVE",
    "COLOUR_ORANGE": "COLOUR_YELLOW",
    "COLOUR_BROWN": "COLOUR_CREAM",
    "COLOUR_GREY": "COLOUR_BROWN",  # more likely we want to complement grey with brown than white
    "COLOUR_WHITE": "COLOUR_GREY",
}

# ship liveries overlap between rosters so are in global constants (engine liveries are per-roster)
# custom remappings of cc1/cc2, used in recolour_sprites, not used in graphics generation, so not in graphics_constants
ship_liveries = {
    # _DEFAULT only used for cases where the livery isn't actually meaningful, e.g. randomised consists
    "_DEFAULT": {
        "colour_set": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPANY_COLOUR_USE_WEATHERING": {
        "colour_set": "company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPANY_COLOUR_NO_WEATHERING": {
        "colour_set": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING": {
        "colour_set": "complement_company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPLEMENT_COMPANY_COLOUR_NO_WEATHERING": {
        "colour_set": "complement_company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_1": {
        "colour_set": "random_liveries_1",
        "purchase": "company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_NO_WEATHERING_1": {
        "colour_set": "random_liveries_1",
        "purchase": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_2": {
        "colour_set": "random_liveries_2",
        "purchase": "complement_company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_NO_WEATHERING_2": {
        "colour_set": "random_liveries_2",
        "purchase": "complement_company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_3": {
        "colour_set": "random_liveries_3",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_NO_WEATHERING_3": {
        "colour_set": "random_liveries_3",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_4": {
        "colour_set": "random_liveries_4",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_5": {
        "colour_set": "random_liveries_5",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_6": {
        "colour_set": "random_liveries_6",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_7": {
        "colour_set": "random_liveries_7",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_8": {
        "colour_set": "random_liveries_8",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_9": {
        "colour_set": "random_liveries_9",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_10": {
        "colour_set": "random_liveries_10",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_LIVERIES_11": {
        "colour_set": "random_liveries_11",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_BAUXITE": {
        "colour_set": "freight_bauxite",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_BAUXITE_NO_WEATHERING": {
        "colour_set": "freight_bauxite",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREMLIN_GREEN": {
        "colour_set": "freight_gremlin_green",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREY": {
        "colour_set": "freight_grey",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREY_NO_WEATHERING": {
        "colour_set": "freight_grey",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_NIGHTSHADE": {
        "colour_set": "freight_nightshade",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_NIGHTSHADE_NO_WEATHERING": {
        "colour_set": "freight_nightshade",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_OCHRE": {
        "colour_set": "freight_ochre",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_OIL_BLACK": {
        "colour_set": "freight_oil_black",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_RUSTY_BLACK": {
        "colour_set": "freight_rusty_black",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_PEWTER": {
        "colour_set": "freight_pewter",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_RUBY": {
        "colour_set": "freight_ruby",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_RED": {
        "colour_set": "red",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SAND": {
        "colour_set": "freight_sand",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SILVER": {
        "colour_set": "freight_silver",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_STRAW": {
        "colour_set": "freight_straw",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SULPHUR": {
        "colour_set": "freight_sulphur",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_TEAL": {
        "colour_set": "freight_teal",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_VIOLET": {
        "colour_set": "freight_violet",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "CC_BLUE": {
        "colour_set": "blue",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "CC_DARK_BLUE": {
        "colour_set": "dark_blue",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
}

# for ships with mixed livery, the permitted liveries for that specific mix type
ship_livery_mixes = {
    # company colour + 1
    "random_liveries_1": ["complement_company_colour", "company_colour"],
    # most everything (but explicit add, so not *everything*)
    "random_liveries_2": [
        "company_colour",
        "complement_company_colour",
        "freight_bauxite",
        "freight_grey",
        "freight_nightshade",
        "freight_silver",
        "freight_teal",
        "freight_violet",
    ],
    # rust belt
    "random_liveries_3": [
        "freight_bauxite",
        "freight_grey",
        "freight_nightshade",
    ],
    # chemicals
    "random_liveries_4": ["freight_teal", "freight_violet"],
    # silver-ish
    "random_liveries_5": ["freight_silver", "freight_pewter"],
    # yellow / ochre
    "random_liveries_6": ["freight_sulphur", "freight_ochre"],
    # rust / ruby
    "random_liveries_7": ["freight_ruby", "freight_bauxite"],
    # black
    "random_liveries_8": ["freight_oil_black", "freight_nightshade"],
    # ochre / sand
    "random_liveries_9": ["freight_ochre", "freight_sand"],
    # moss /
    "random_liveries_10": ["freight_gremlin_green", "freight_silver"],
    # yellow / faded
    "random_liveries_11": ["freight_sulphur", "freight_straw"],
}

# up to 127 temp storages are available, might as well allocate them exclusively within the graphics chain to avoid any collisions
temp_storage_ids = dict(
    cc_num_to_recolour=0,  # used in procedures_colour_randomisation_strategies
    flag_use_weathering=1,  # used in procedures_recolour_strategies
    recolour_livery_num_0=2,  # used in procedures_recolour_strategies
    recolour_livery_num_1=3,  # used in procedures_recolour_strategies
    recolour_livery_num_2=4,  # used in procedures_recolour_strategies
    recolour_livery_num_3=5,  # used in procedures_recolour_strategies
    recolour_livery_num_4=6,  # used in procedures_recolour_strategies
    recolour_livery_num_5=7,  # used in procedures_recolour_strategies
    recolour_livery_num_6=8,  # used in procedures_recolour_strategies
    recolour_livery_num_7=9,  # used in procedures_recolour_strategies
    flag_context_is_purchase=10,  # used in procedures_recolour_strategies
    recolour_strategy_num=11,  # used in procedures_recolour_strategies
    recolour_strategy_num_purchase=12,  # used in procedures_recolour_strategies
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
