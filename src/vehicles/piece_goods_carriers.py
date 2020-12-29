from ship import PieceGoodsCarrier


def main():
    ship = PieceGoodsCarrier(
        numeric_id=7,
        name="Rampside [Piece Goods Carrier]",
        gen=1,
        subtype="D",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=45,
        name="Rivingen [Piece Goods Carrier]",
        gen=1,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=8,
        name="Trondheim [Piece Goods Carrier]",
        gen=1,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
