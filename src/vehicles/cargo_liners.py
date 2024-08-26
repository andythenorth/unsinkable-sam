from ship import CargoLiner


def main():
    ship = CargoLiner(
        numeric_id=90,
        name="Amethyste",
        gen=2,
        subtype="E",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
        sprites_complete=False,
    )

    ship = CargoLiner(
        numeric_id=750,
        name="Inisheer",
        gen=3,
        subtype="A",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = CargoLiner(
        numeric_id=700,
        name="Braddock",
        gen=3,
        subtype="B",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = CargoLiner(
        numeric_id=710,
        name="Magellan",
        gen=3,
        subtype="C",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = CargoLiner(
        numeric_id=70,
        name="Rampside",
        gen=3,
        subtype="D",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = CargoLiner(
        numeric_id=450,
        name="Rivingen",
        gen=3,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = CargoLiner(
        numeric_id=80,
        name="Trondheim",
        gen=3,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )
