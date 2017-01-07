import global_constants
from ship import Tanker

ship = Tanker(id = 'tanker_large',
            numeric_id = 2,
            title = 'Large [Tanker]',
            size_class = 'large',
            buy_cost = 64,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.1,
            intro_date = 1870,
            str_type_info = 'COASTAL_TANKER',
            effects = ['EFFECT_SPRITE_DIESEL, 12, 0, 18'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=ship.graphics_processors[0])
