from ship import LivestockCarrier


def main():
    ship = LivestockCarrier(
        numeric_id=20,
        name="Gore Creek",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=16,
        name="Sharkbait",
        gen=3,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
