from ship import UniversalFreighterShip


def main():
    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=6,
        name="Matson [Freighter]",
        gen=1,
        subtype="A",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=5,
        name="Gelenbeek [Freighter]",
        gen=1,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=4,
        name="Eagle [Freighter]",
        gen=1,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=3,
        name="Akraberg [Freighter]",
        gen=1,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=41,
        name="Shackleton [Freighter]",
        gen=1,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=42,
        name="Longstone [Freighter]",
        gen=1,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=30,
        name="Thesiger [Freighter]",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )
