from polar_fox import base_refits_by_class, cargo_labels, chameleon_cache_dir, generated_files_dir, graphics_path, max_game_date

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
disallowed_refits_by_label = {'non_dump_bulk': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'CERE', 'MAIZ', 'FRUT', 'BEAN', 'CMNT', 'CTCD', 'FERT', 'OLSD', 'SUGR', 'SULP', 'TOFF', 'URAN'],
                              'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL'],
                              'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR', 'RUBR', 'SULP'],
                              'non_flatbed_freight': ['FOOD', 'FISH', 'LVST', 'FRUT', 'BEER', 'MILK', 'JAVA', 'SUGR', 'NUTS', 'EOIL', 'BOOM', 'FERT'],
                              'non_freight_special_cases': ['TOUR']}

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# mailbags are < 1t, multiply capacity appropriately
mail_multiplier = 2

# cargo aging constant - OTTD default is 185 - dibble this up in favour of ships, as they are relatively slow
CARGO_AGE_PERIOD = 370

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = ((20, 28, 89), (60, 113, 66), (186, 128, 48), (318, 113, 66),
                              (444, 28, 89), (484, 113, 66), (610, 128, 48), (742, 113, 66))

# standard vehicle offsets; custom can be supported if needed by extending ship.offsets
vehicle_offsets = {'micro': [[-15, -38], [-64, -32], [-66, -25], [-64, -22], [-15, -38], [-64, -22], [-68, -25], [-38, -20]],
                   'mini':  [[-14, -66], [-54, -32], [-32, -34], [-4, -32], [-14, -66], [-54, -34], [-32, -34], [-4, -32]],
                   'small': [[-14, -58], [-59, -29], [-48, -36], [-8, -29], [-14, -58], [-61, -29], [-48, -36], [-9, -29]],
                   'large': [[-14, -46], [-70, -23], [-64, -34], [-18, -23], [-14, -46], [-72, -23], [-64, -34], [-18, -23]]}

buy_menu_sprite_width = 128
buy_menu_sprite_height = 32
