from ship import BulkBarge


def main():
    ship = BulkBarge(
        numeric_id=35,
        name="Pittman",
        gen=2,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=55,
        name="Lorain",
        gen=2,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=10,
        name="Sandvik",
        gen=2,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=9,
        name="Bigrock",
        gen=2,
        subtype="F",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
