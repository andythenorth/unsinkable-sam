from ship import Trawler


def main():
    ship = Trawler(
        numeric_id=11,
        name="Newfoundland",
        gen=3,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=12,
        name="Rio Pescado",
        gen=3,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=13,
        name="Cromarty",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
