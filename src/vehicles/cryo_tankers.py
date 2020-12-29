from ship import CryoTanker


def main():
    ship = CryoTanker(
        numeric_id=63,
        name="Schmieder [Cryo Tanker]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=64,
        name="Ferrel [Cryo Tanker]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=38,
        name="Svedlund [Cryo Tanker]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=62,
        name="Weicher [Cryo Tanker]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=2.0,
        fuel_run_cost_factor=1.8,
        intro_date=1870,
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=37,
        name="Picard [Cryo Tanker]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
