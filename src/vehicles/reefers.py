from ship import Reefer


def main():
    ship = Reefer(
        numeric_id=760,
        name="Seafrost",
        gen=3,
        subtype="A",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = Reefer(
        numeric_id=610,
        name="Langara",
        gen=3,
        subtype="B",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = Reefer(
        numeric_id=600,
        name="Samphire",
        gen=3,
        subtype="C",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = Reefer(
        numeric_id=140,
        name="Kodiak",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = Reefer(
        numeric_id=590,
        name="Caribou",
        gen=3,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = Reefer(
        numeric_id=150,
        name="Helsinki",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )
