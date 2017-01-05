import global_constants
from ship import EdiblesTanker

ship = EdiblesTanker(id = 'edibles_tanker_large',
            numeric_id = 18,
            title = 'Large [Edibles Tanker]',
            size_class = 'large',
            buy_cost = 64,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.1,
            offsets = [[-14, -42], [-68, -26], [-55, -30], [-16, -26], [-14, -54], [-66, -27], [-55, -30], [-14, -26]],
            loading_speed = 40,
            intro_date = 1870,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'COASTAL_TANKER',
            effects = ['EFFECT_SPRITE_DIESEL, 12, 0, 18'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
