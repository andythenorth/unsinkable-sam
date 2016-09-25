import global_constants
from ship import Tanker

ship = Tanker(id = 'tanker_small',
            numeric_id = 1,
            title = 'Small [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 240,
            replacement_id = '-none',
            buy_cost = 28,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.8,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 88,
            loading_speed = 40,
            intro_date = 1870,
            buy_menu_bb_xy = [645, 21],
            str_type_info = 'SMALL_TANKER_COASTAL_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 8, 0, 18'],
            vehicle_life = 35)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
