from ship import EdiblesTanker


def main():
    ship = EdiblesTanker(
        numeric_id=58,
        name="Bounty [Edibles Tanker]",
        subtype="B",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=57,
        name="Mystic [Edibles Tanker]",
        subtype="C",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=32,
        name="Fresnel [Edibles Tanker]",
        subtype="D",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=56,
        name="Belliveau [Edibles Tanker]",
        subtype="E",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=18,
        name="Cortes [Edibles Tanker]",
        subtype="F",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
