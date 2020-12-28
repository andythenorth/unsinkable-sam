from roster import Roster

def main(disabled=False):
    roster = Roster(
        id="default",
        numeric_id=1,
        speeds={
            "freight": {0: 25, 1950: 35},
            "fast_freight": {},  # unused currently
            "pax_mail": {0: 35, 1950: 45, 1980: 70},
        },
    )
    roster.register(disabled=disabled)
