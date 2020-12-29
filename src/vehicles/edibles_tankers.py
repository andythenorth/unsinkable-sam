from ship import EdiblesTanker


def main():
    ship = EdiblesTanker(
        numeric_id=58,
        name="Bounty [Edibles Tanker]",
        gen=1,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=57,
        name="Mystic [Edibles Tanker]",
        gen=1,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=32,
        name="Fresnel [Edibles Tanker]",
        gen=1,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=56,
        name="Belliveau [Edibles Tanker]",
        gen=1,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=18,
        name="Cortes [Edibles Tanker]",
        gen=1,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
