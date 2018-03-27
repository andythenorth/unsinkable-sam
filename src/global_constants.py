# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

grfid = r"\55\53\53\33"

# cargo aging constant - OTTD default is 185 - dibble this up in favour of ships, as they are relatively slow
CARGO_AGE_PERIOD = 370

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = ((20, 28, 89), (60, 113, 66), (186, 128, 48), (318, 113, 66),
                              (444, 28, 89), (484, 113, 66), (610, 128, 48), (742, 113, 66))

# standard vehicle offsets; custom can be supported if needed by extending ship.offsets
vehicle_offsets = {'32px': [[-14, -73], [-44, -38], [-22, -36], [8, -38], [-14, -73], [-42, -38], [-22, -36], [8, -38]],
                   '44px': [[-14, -73], [-44, -38], [-22, -36], [8, -38], [-14, -73], [-42, -38], [-22, -36], [8, -38]],
                   '64px':  [[-14, -68], [-50, -35], [-32, -34], [3, -34], [-14, -68], [-50, -35], [-32, -34], [3, -34]],
                   '96px': [[-14, -58], [-59, -29], [-48, -36], [-8, -29], [-14, -58], [-61, -29], [-48, -36], [-9, -29]],
                   '128px': [[-14, -46], [-70, -23], [-64, -34], [-18, -23], [-14, -46], [-72, -23], [-64, -34], [-18, -23]]}

buy_menu_sprite_width = 128
buy_menu_sprite_height = 32

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants
base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
default_cargos = polar_fox.constants.default_cargos
disallowed_refits_by_label = polar_fox.constants.disallowed_refits_by_label
generated_files_dir = polar_fox.constants.generated_files_dir
graphics_path = polar_fox.constants.graphics_path
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date