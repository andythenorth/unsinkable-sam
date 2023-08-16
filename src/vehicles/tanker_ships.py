from ship import TankerShip


def main():
    ship = TankerShip(
        numeric_id=43,
        name="Chirikov",
        gen=2,
        subtype="E",
        hull="TempHouseNone",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=670,
        name="Salso",
        gen=3,
        subtype="A",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=340,
        name="Berwick",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = TankerShip(
        numeric_id=440,
        name="Kalsoy",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = TankerShip(
        numeric_id=10,
        name="Ellesmere",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = TankerShip(
        numeric_id=190,
        name="Gunfleet",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=True,
    )

    ship = TankerShip(
        numeric_id=20,
        name="Rotterdam",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=True,
    )


"""
    ship = TankerShip(
        numeric_id=310,
        name="Escobar",
        gen=4,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
"""
