from ship import Reefer


def main():
    ship = Reefer(
        id="reefer_B",
        numeric_id=61,
        name="Langara [Reefer]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = Reefer(
        id="reefer_C",
        numeric_id=60,
        name="Samphire [Reefer]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = Reefer(
        id="reefer_D",
        numeric_id=14,
        name="Kodiak [Reefer]",
        subtype="D",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        id="reefer_E",
        numeric_id=59,
        name="Caribou [Reefer]",
        subtype="E",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        id="reefer_F",
        numeric_id=15,
        name="Helsinki [Reefer]",
        subtype="F",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
