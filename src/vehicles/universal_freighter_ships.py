from ship import UniversalFreighter


def main():
    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_A",
        numeric_id=6,
        name="Matson [Freighter]",
        subtype="A",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_B",
        numeric_id=5,
        name="Gelenbeek [Freighter]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_C",
        numeric_id=4,
        name="Eagle [Freighter]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_D",
        numeric_id=3,
        name="Akraberg [Freighter]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_E",
        numeric_id=41,
        name="Shackleton [Freighter]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )

    ship = UniversalFreighter(
        roster_id="default",
        id="universal_freighter_ship_F",
        numeric_id=42,
        name="Longstone [Freighter]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
