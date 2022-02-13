from ship import LivestockCarrier


def main():
    ship = LivestockCarrier(
        numeric_id=72,
        name="Kittimack",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=73,
        name="Gore Creek",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = LivestockCarrier(
        numeric_id=20,
        name="Dockacre",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=74,
        name="Erry Vane",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = LivestockCarrier(
        numeric_id=16,
        name="Sharkbait",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
