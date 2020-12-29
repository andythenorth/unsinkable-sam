from ship import Reefer


def main():
    ship = Reefer(
        numeric_id=61,
        name="Langara [Reefer]",
        subtype="B",
        hull="BargeHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = Reefer(
        numeric_id=60,
        name="Samphire [Reefer]",
        subtype="C",
        hull="ShipHouseRear",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = Reefer(
        numeric_id=14,
        name="Kodiak [Reefer]",
        subtype="D",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        numeric_id=59,
        name="Caribou [Reefer]",
        subtype="E",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        numeric_id=15,
        name="Helsinki [Reefer]",
        subtype="F",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
