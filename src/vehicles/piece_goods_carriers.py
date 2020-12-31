from ship import PieceGoodsCarrier


def main():
    ship = PieceGoodsCarrier(
        numeric_id=7,
        name="Rampside",
        gen=3,
        subtype="D",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=45,
        name="Rivingen",
        gen=3,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=8,
        name="Trondheim",
        gen=3,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
