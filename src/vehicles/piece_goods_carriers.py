from ship import PieceGoodsCarrier


def main():
    ship = PieceGoodsCarrier(
        id="piece_goods_carrier_D",
        numeric_id=7,
        name="Rampside [Piece Goods Carrier]",
        subtype="D",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        id="piece_goods_carrier_E",
        numeric_id=45,
        name="Rivingen [Piece Goods Carrier]",
        subtype="E",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PieceGoodsCarrier(
        id="piece_goods_carrier_F",
        numeric_id=8,
        name="Trondheim [Piece Goods Carrier]",
        subtype="F",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
