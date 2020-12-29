from ship import LivestockCarrier


def main():
    ship = LivestockCarrier(
        numeric_id=20,
        name="Gore Creek [Livestock Carrier]",
        subtype="D",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = LivestockCarrier(
        numeric_id=16,
        name="Sharkbait [Livestock Carrier]",
        subtype="F",
        hull="ShipHouseForward",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
