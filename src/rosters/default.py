from roster import Roster


def main(disabled=False):
    roster = Roster(
        id="default",
        numeric_id=1,
        # left as dict when copying from Iron Horse, assumes might split pax / freight / hovercraft etc in future?  Bets that I end up making it just a list?
        intro_dates={
            "DEFAULT": [1860, 1900, 1960, 2020],
        },
        speeds={
            "freight": {0: 25, 1950: 35},
            "fast_freight": {},  # unused currently
            "pax_mail": {0: 35, 1950: 45, 1980: 70},
        },
    )
    roster.register(disabled=disabled)
