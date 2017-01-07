
# shared lists of allowed classes, shared across multiple vehicle types
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
base_refits_by_class = {'empty': [],
                       'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                       'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
                       'liquids': ['CC_LIQUID'],
                       'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'dump_freight': ['CC_BULK'],
                       'flatbed_freight': ['CC_PIECE_GOODS'],
                       'refrigerated_freight': ['CC_REFRIGERATED'],
                       'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

disallowed_refits_by_label = {'non_dump_bulk': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'CERE', 'MAIZ', 'FRUT', 'BEAN', 'CMNT', 'CTCD', 'FERT', 'OLSD', 'SUGR', 'SULP', 'TOFF', 'URAN'],
                              'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL'],
                              'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR', 'RUBR'],
                              'non_freight_special_cases': ['TOUR']}

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ('PASS', # pax first
                'TOUR',
                # "the mail must get through"
                'MAIL',
                # all other cargos - append new ones to end, don't change order
                'COAL',
                'IORE',
                'GRVL',
                'SAND',
                'AORE',
                'CORE',
                'CLAY',
                'SCMT',
                'WOOD',
                'LIME',
                'GOOD',
                'FOOD',
                'STEL',
                'FMSP',
                'ENSP',
                'BEER',
                'BDMT',
                'MNSP',
                'PAPR',
                'WDPR',
                'VEHI',
                'COPR',
                'DYES',
                'OIL_',
                'RFPR',
                'PETR',
                'PLAS',
                'WATR',
                'FISH',
                'CERE',
                'FICR',
                'FRVG',
                'FRUT',
                'GRAI',
                'LVST',
                'MAIZ',
                'MILK',
                'RUBR',
                'SGBT',
                'SGCN',
                'WHEA',
                'WOOL',
                'OLSD',
                'SUGR',
                'BEAN',
                'NITR',
                'JAVA',
                'VEHI',
                'EOIL',
                'CASS',
                'NUTS',
                'MNO2',
                'PHOS',
                'PORE',
                'POTA',
                'FERT',
                'CMNT',
                'CTCD',
                'TOFF',
                'SULP',
                'URAN')

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = 'chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + '/graphics/'

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 740

# OpenTTD's max date
max_game_date = 5000001

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = ((60, 12, 24), (92, 26, 20), (124, 36, 16), (172, 26, 20),
                              (204, 12, 24), (236, 26, 20), (268, 36, 16), (316, 26, 20))
