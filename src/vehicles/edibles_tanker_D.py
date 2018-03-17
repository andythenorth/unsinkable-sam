from ship import EdiblesTanker

ship = EdiblesTanker(id='edibles_tanker_D',
                     numeric_id=18,
                     title='[Edibles Tanker]',
                     subtype='D',
                     hull='ShipHouseRear',
                     buy_cost=64,
                     fixed_run_cost_factor=12.0,
                     fuel_run_cost_factor=1.1,
                     intro_date=1870,
                     effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
