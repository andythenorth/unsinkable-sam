from ship import Reefer

ship = Reefer(id='reefer_C',
              numeric_id=14,
              title='[Reefer]',
              subtype='C',
              hull='ShipHouseForward',
              buy_cost=28,
              fixed_run_cost_factor=3.5,
              fuel_run_cost_factor=1.0,
              intro_date=1870,
              effect_type='EFFECT_SPRITE_STEAM')

ship.add_model_variant(spritesheet_suffix=0)
