from ship import PaxFastLoadingShip


def main():
    ship = PaxFastLoadingShip(
        numeric_id=29,
        name="Goblin",
        gen=2,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=25,
        name="Arranmore",
        gen=2,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=24,
        name="Cascades",
        gen=2,
        subtype="C",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxFastLoadingShip(
        numeric_id=21,
        name="Valberg",
        gen=2,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
