from ship import Trawler


def main():
    ship = Trawler(
        numeric_id=11,
        name="Newfoundland [Trawler]",
        subtype="A",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=12,
        name="Rio Pescado [Trawler]",
        subtype="B",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=13,
        name="Cromarty [Trawler]",
        subtype="D",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )
