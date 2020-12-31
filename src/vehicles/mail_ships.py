from ship import MailShip


def main():
    ship = MailShip(
        numeric_id=28,
        name="Diamond",
        gen=2,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=27,
        name="Delta",
        gen=2,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=26,
        name="Olympic",
        gen=2,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
