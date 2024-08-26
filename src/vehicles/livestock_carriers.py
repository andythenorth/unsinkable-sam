from ship import LivestockCarrier


def main():
    ship = LivestockCarrier(
        numeric_id=720,
        name="Kittimack",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=730,
        name="Gore Creek",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = LivestockCarrier(
        numeric_id=200,
        name="Dockacre",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=740,
        name="Erry Vane",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = LivestockCarrier(
        numeric_id=160,
        name="Sharkbait",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
