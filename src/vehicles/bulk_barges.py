from ship import BulkCarrier


def main():
    ship = BulkCarrier(
        id="bulk_barge_B",
        numeric_id=35,
        name="Pittman [Bulk Barge]",
        subtype="B",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_barge_C",
        numeric_id=55,
        name="Lorain [Bulk Barge]",
        subtype="C",
        hull="TempHouseNone",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_barge_D",
        numeric_id=10,
        name="Sandvik [Bulk Barge]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_barge_E",
        numeric_id=52,
        name="Dyna [Bulk Barge]",
        subtype="E",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_barge_F",
        numeric_id=9,
        name="Bigrock [Bulk Barge]",
        subtype="F",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
