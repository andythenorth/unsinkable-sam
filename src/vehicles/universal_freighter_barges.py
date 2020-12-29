from ship import UniversalFreighterBarge


def main():
    ship = UniversalFreighterBarge(
        numeric_id=46,
        name="Lindau [Freight Barge]",
        subtype="D",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterBarge(
        numeric_id=47,
        name="Detroit [Freight Barge]",
        subtype="E",
        hull="PushBargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterBarge(
        numeric_id=48,
        name="Roanoke [Freight Barge]",
        subtype="F",
        hull="PushBargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
