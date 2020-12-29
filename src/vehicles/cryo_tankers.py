from ship import CryoTanker


def main():
    ship = CryoTanker(
        numeric_id=63,
        name="Schmieder [Cryo Tanker]",
        gen=1,
        subtype="B",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=64,
        name="Ferrel [Cryo Tanker]",
        gen=1,
        subtype="C",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=38,
        name="Svedlund [Cryo Tanker]",
        gen=1,
        subtype="D",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=62,
        name="Weicher [Cryo Tanker]",
        gen=1,
        subtype="E",
        hull="ShipHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = CryoTanker(
        numeric_id=37,
        name="Picard [Cryo Tanker]",
        gen=1,
        subtype="F",
        hull="ShipHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
