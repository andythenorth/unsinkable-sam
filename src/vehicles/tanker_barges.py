from ship import TankerBarge


def main():
    ship = TankerBarge(
        numeric_id=40,
        name="Durance [TANK_BARGE]",
        subtype="D",
        hull="BargeHouseRear",
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
        intro_date=1870,
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
