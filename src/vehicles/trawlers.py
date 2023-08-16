from ship import Trawler


def main():
    ship = Trawler(
        numeric_id=110,
        name="Newfoundland",
        gen=3,
        subtype="A",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=120,
        name="Rio Pescado",
        gen=3,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Trawler(
        numeric_id=130,
        name="Cromarty",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
