from ship import PaxFastLoadingShip


def main():
    ship = PaxFastLoadingShip(
        numeric_id=290,
        name="Goblin",
        gen=3,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=250,
        name="Arranmore",
        gen=3,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=240,
        name="Cascades",
        gen=3,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=210,
        name="Valberg",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
