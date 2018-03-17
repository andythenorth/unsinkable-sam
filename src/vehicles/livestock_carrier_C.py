from ship import LivestockCarrier

ship = LivestockCarrier(id='livestock_carrier_C',
                        numeric_id=20,
                        title='[Livestock Carrier]',
                        subtype='C',
                        hull='ShipHouseRear',
                        buy_cost=28,
                        fixed_run_cost_factor=3.5,
                        fuel_run_cost_factor=1.0,
                        intro_date=1870,
                        effect_type='EFFECT_SPRITE_STEAM')

ship.add_model_variant(spritesheet_suffix=0)
