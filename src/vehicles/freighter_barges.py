from ship import FreighterBarge


def main():
    ship = FreighterBarge(
        numeric_id=990,
        name="Maryport",
        gen=3,
        subtype="C",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterBarge(
        numeric_id=460,
        name="Lindau",
        gen=3,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterBarge(
        numeric_id=470,
        name="Detroit",
        gen=3,
        subtype="E",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=5,
    )

    ship = FreighterBarge(
        numeric_id=480,
        name="Roanoke",
        gen=3,
        subtype="F",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
