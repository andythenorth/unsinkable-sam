from ship import EdiblesTanker


def main():
    ship = EdiblesTanker(
        numeric_id=58,
        name="Bounty",
        gen=2,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=57,
        name="Mystic",
        gen=2,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=32,
        name="Fresnel",
        gen=2,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=56,
        name="Belliveau",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=18,
        name="Cortes",
        gen=2,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
