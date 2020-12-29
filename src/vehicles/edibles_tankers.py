from ship import EdiblesTanker


def main():
    ship = EdiblesTanker(
        numeric_id=58,
        name="Bounty [Edibles Tanker]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=57,
        name="Mystic [Edibles Tanker]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=32,
        name="Fresnel [Edibles Tanker]",
        subtype="D",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=56,
        name="Belliveau [Edibles Tanker]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = EdiblesTanker(
        numeric_id=18,
        name="Cortes [Edibles Tanker]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=12.0,
        fuel_run_cost_factor=1.1,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
