from ship import PaxLuxuryShip


def main():
    ship = PaxLuxuryShip(
        numeric_id=23,
        name="Bonavista [Pax Luxury]",
        subtype="C",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxLuxuryShip(
        numeric_id=22,
        name="Zealand [Pax Luxury]",
        subtype="D",
        hull="TempHouseNone",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )
