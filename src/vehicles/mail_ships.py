from ship import MailShip


def main():
    ship = MailShip(
        numeric_id=28,
        name="Diamond [Mail Ship]",
        subtype="A",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=27,
        name="Delta [Mail Ship]",
        subtype="B",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=26,
        name="Olympic [Mail Ship]",
        subtype="D",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )
