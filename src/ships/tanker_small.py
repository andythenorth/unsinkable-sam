import global_constants
from ship import Tanker

ship = Tanker(id = 'tanker_small',
            numeric_id = 1,
            title = 'Small [Tanker]',
            size_class = 'small',
            buy_cost = 28,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.8,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            loading_speed = 40,
            intro_date = 1870,
            str_type_info = 'SMALL_TANKER_COASTAL_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 8, 0, 18'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
