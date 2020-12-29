from ship import UniversalFreighterShip


def main():
    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=6,
        name="Matson [Freighter]",
        subtype="A",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=5,
        name="Gelenbeek [Freighter]",
        subtype="B",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=4,
        name="Eagle [Freighter]",
        subtype="C",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=3,
        name="Akraberg [Freighter]",
        subtype="D",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=41,
        name="Shackleton [Freighter]",
        subtype="E",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=42,
        name="Longstone [Freighter]",
        subtype="F",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
