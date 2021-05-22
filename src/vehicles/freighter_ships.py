from ship import FreighterShip


def main():
    ship = FreighterShip(
        roster_id="default",
        numeric_id=30,
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
        numeric_id=6,
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
        numeric_id=5,
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
        numeric_id=4,
        name="Eagle",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=3,
        name="Akraberg",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=41,
        name="Thesiger",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = FreighterShip(
        roster_id="default",
        numeric_id=42,
        name="Longstone",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )


"""
    ship = FreighterShip(
        roster_id="default",
        numeric_id=17,
        name="Fiennes",
        gen=4,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )
"""
