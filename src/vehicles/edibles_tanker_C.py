import global_constants
from ship import EdiblesTanker

ship = EdiblesTanker(id='edibles_tanker_C',
                     numeric_id=32,
                     title='[Edibles Tanker]',
                     subtype='C',
                     hull='ShipHouseRear',
                     buy_cost=64,
                     fixed_run_cost_factor=12.0,
                     fuel_run_cost_factor=1.1,
                     intro_date=1870,
                     effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
