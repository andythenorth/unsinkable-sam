from ship import BulkShip


def main():
    ship = BulkShip(
        numeric_id=54,
        name="Saltlick [Mini Bulker]",
        gen=2,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=53,
        name="Lotsberget [Mini Bulker]",
        gen=2,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=51,
        name="Gravelly [Mini Bulker]",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=50,
        name="Alligator [Mini Bulker]",
        gen=2,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
