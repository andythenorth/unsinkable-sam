from ship import FreighterBarge


def main():
    ship = FreighterBarge(
        numeric_id=99,
        name="Maryport",
        gen=3,
        subtype="C",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterBarge(
        numeric_id=46,
        name="Lindau",
        gen=3,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterBarge(
        numeric_id=47,
        name="Detroit",
        gen=3,
        subtype="E",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterBarge(
        numeric_id=48,
        name="Roanoke",
        gen=3,
        subtype="F",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
