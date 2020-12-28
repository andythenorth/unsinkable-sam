from ship import PaxLuxuryShip


def main():
    ship = PaxLuxuryShip(
        id="pax_luxury_C",
        numeric_id=23,
        name="Bonavista [Pax Luxury]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxLuxuryShip(
        id="pax_luxury_D",
        numeric_id=22,
        name="Zealand [Pax Luxury]",
        subtype="D",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )
