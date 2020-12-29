from ship import PaxLuxuryShip


def main():
    ship = PaxLuxuryShip(
        numeric_id=23,
        name="Bonavista [Pax Luxury]",
        gen=1,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxLuxuryShip(
        numeric_id=22,
        name="Zealand [Pax Luxury]",
        gen=1,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
