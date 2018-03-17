from ship import FruitVegCarrier

ship = FruitVegCarrier(id='fruit_veg_carrier_C',
                       numeric_id=31,
                       title='[Fruit Veg Carrier]',
                       subtype='C',
                       hull='ShipHouseForward',
                       buy_cost=28,
                       fixed_run_cost_factor=3.5,
                       fuel_run_cost_factor=1.0,
                       intro_date=1870,
                       effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
