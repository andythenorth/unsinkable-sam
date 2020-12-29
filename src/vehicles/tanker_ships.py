from ship import TankerShip


def main():
    ship = TankerShip(
        numeric_id=34,
        name="Berwick [TankerShip]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = TankerShip(
        numeric_id=44,
        name="Kalsoy [TankerShip]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=1,
        name="Ellesmere [TankerShip]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = TankerShip(
        numeric_id=43,
        name="Gunfleet [TankerShip]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=2,
        name="Rotterdam [TankerShip]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
