from ship import MerchandiseFreighterShip


def main():
    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=780,
        name="Pendeen",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=790,
        name="Pitney",
        gen=3,
        subtype="A",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=7,
        sprites_complete=True,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=800,
        name="Bamburgh",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=5,
        sprites_complete=True,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=810,
        name="Achillbeg",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=6,
        sprites_complete=True,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=820,
        name="Rosenthal",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=7,
        sprites_complete=True,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=830,
        name="Watchet",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = MerchandiseFreighterShip(
        roster_id="default",
        numeric_id=840,
        name="Amherst",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=8,
        sprites_complete=True,
    )
