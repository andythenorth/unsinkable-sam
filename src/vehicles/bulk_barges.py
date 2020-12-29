from ship import BulkBarge


def main():
    ship = BulkBarge(
        numeric_id=35,
        name="Pittman [Bulk Barge]",
        gen=1,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=55,
        name="Lorain [Bulk Barge]",
        gen=1,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=10,
        name="Sandvik [Bulk Barge]",
        gen=1,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=52,
        name="Dyna [Bulk Barge]",
        gen=1,
        subtype="E",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=9,
        name="Bigrock [Bulk Barge]",
        gen=1,
        subtype="F",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
