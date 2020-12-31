from ship import PaxFastLoadingShip


def main():
    ship = PaxFastLoadingShip(
        numeric_id=29,
        name="Goblin",
        gen=3,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=25,
        name="Arranmore",
        gen=3,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=24,
        name="Cascades",
        gen=3,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=21,
        name="Valberg",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
