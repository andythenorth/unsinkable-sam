from ship import TankerShip


def main():
    ship = TankerShip(
        numeric_id=34,
        name="Berwick [TankerShip]",
        gen=1,
        subtype="B",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = TankerShip(
        numeric_id=44,
        name="Kalsoy [TankerShip]",
        gen=1,
        subtype="C",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=1,
        name="Ellesmere [TankerShip]",
        gen=1,
        subtype="D",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
    ship = TankerShip(
        numeric_id=43,
        name="Gunfleet [TankerShip]",
        gen=1,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerShip(
        numeric_id=2,
        name="Rotterdam [TankerShip]",
        gen=1,
        subtype="F",
        hull="ShipHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
