from ship import CryoTanker


def main():
    ship = CryoTanker(
        numeric_id=63,
        name="Schmieder",
        gen=3,
        subtype="B",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=64,
        name="Ferrel",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=38,
        name="Svedlund",
        gen=3,
        subtype="D",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=62,
        name="Weicher",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=37,
        name="Picard",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
