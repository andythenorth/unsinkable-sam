import global_constants
from ship import FlatDeckBarge

ship = FlatDeckBarge(id='flatdeck_barge_C',
                     numeric_id=19,
                     title='[Flatdeck Barge]',
                     subtype='C',
                     hull='BargeHouseRear',
                     buy_cost=28,
                     fixed_run_cost_factor=3.5,
                     fuel_run_cost_factor=1.0,
                     intro_date=1870,
                     effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
