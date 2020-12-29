from ship import TankerBarge


def main():
    ship = TankerBarge(
        numeric_id=40,
        name="Durance [TANK_BARGE]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = TankerBarge(
        numeric_id=49,
        name="Notto [TANK_BARGE]",
        subtype="E",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerBarge(
        numeric_id=39,
        name="Columbus [TANK_BARGE]",
        subtype="F",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
