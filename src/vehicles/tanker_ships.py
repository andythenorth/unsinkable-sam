from ship import Tanker


def main():
    ship = Tanker(
        id="tanker_ship_B",
        numeric_id=34,
        name="Berwick [Tanker]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = Tanker(
        id="tanker_ship_C",
        numeric_id=44,
        name="Kalsoy [Tanker]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = Tanker(
        id="tanker_ship_D",
        numeric_id=1,
        name="Ellesmere [Tanker]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = Tanker(
        id="tanker_ship_E",
        numeric_id=43,
        name="Gunfleet [Tanker]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = Tanker(
        id="tanker_ship_F",
        numeric_id=2,
        name="Rotterdam [Tanker]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
