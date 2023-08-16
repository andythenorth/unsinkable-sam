from ship import FreighterShip


def main():
    ship = FreighterShip(
        roster_id="default",
        numeric_id=300,
        name="Shackleton",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=600,
        name="Matson",
        gen=3,
        subtype="A",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=7,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=500,
        name="Gelenbeek",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=5,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=400,
        name="Eagle",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=6,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=300,
        name="Akraberg",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=7,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=410,
        name="Thesiger",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=420,
        name="Longstone",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=8,
        sprites_complete=True,
    )


"""
    ship = FreighterShip(
        roster_id="default",
        numeric_id=170,
        name="Fiennes",
        gen=4,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )
"""
