from ship import UniversalFreighterBarge


def main():
    ship = UniversalFreighterBarge(
        numeric_id=46,
        name="Lindau [Freight Barge]",
        gen=2,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterBarge(
        numeric_id=47,
        name="Detroit [Freight Barge]",
        gen=2,
        subtype="E",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterBarge(
        numeric_id=48,
        name="Roanoke [Freight Barge]",
        gen=2,
        subtype="F",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
