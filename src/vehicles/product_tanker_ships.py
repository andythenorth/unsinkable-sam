from ship import ProductTankerShip


def main():
    ship = ProductTankerShip(
        numeric_id=92,
        name="Polo",
        gen=3,
        subtype="A",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = ProductTankerShip(
        numeric_id=93,
        name="Belgica",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = ProductTankerShip(
        numeric_id=94,
        name="Nintoku",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = ProductTankerShip(
        numeric_id=95,
        name="Schmidt",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = ProductTankerShip(
        numeric_id=96,
        name="Lecointe",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = ProductTankerShip(
        numeric_id=97,
        name="Rocheport",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
