from ship import BulkBarge


def main():
    """
        possible barge names
        name="Sintra",
        name="Klink",
        name="Skansin",
        name="Grinna",
        name="Carson",
        name="Anvil",
    """

    ship = BulkBarge(
        numeric_id=350,
        name="Pittman",
        gen=2,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=550,
        name="Lorain",
        gen=2,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=100,
        name="Sandvik",
        gen=2,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkBarge(
        numeric_id=90,
        name="Bigrock",
        gen=2,
        subtype="F",
        hull="PushBargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
