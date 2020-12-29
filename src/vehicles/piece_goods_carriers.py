from ship import PieceGoodsCarrier


def main():
    ship = PieceGoodsCarrier(
        numeric_id=7,
        name="Rampside [Piece Goods Carrier]",
        subtype="D",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=45,
        name="Rivingen [Piece Goods Carrier]",
        subtype="E",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        numeric_id=8,
        name="Trondheim [Piece Goods Carrier]",
        subtype="F",
        hull="ShipHouseForward",
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
