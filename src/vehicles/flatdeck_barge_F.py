from ship import FlatDeckBarge

ship = FlatDeckBarge(
    numeric_id=17,
    name="Pensacola [Flatdeck Barge]",
    subtype="F",
    hull="PushBargeHouseRear",
    fixed_run_cost_factor=3.5,
    fuel_run_cost_factor=1.0,
    intro_date=1870,
    effect_type="EFFECT_SPRITE_DIESEL",
    cargo_length=7,
)
