from rosters import registered_rosters
import global_constants
import pickle


class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.numeric_id = kwargs.get("numeric_id")
        self.intro_dates = kwargs.get("intro_dates")
        self.speeds = kwargs.get("speeds")
        self.ships = []

    @property
    def buy_menu_sort_order(self):
        return [ship.id for ship in self.ships]

    @property
    def ships_in_buy_menu_order(self):
        result = []
        for base_id in global_constants.buy_menu_sort_order_ships:
            ships_for_type = [ship for ship in self.ships if ship.base_id == base_id]
            result.extend(
                # note that we want the sort order to be U, A, B, C, D so special handling
                # this *doesn*'t handle the case of changing _multiple_ times between U and A / B / C / D between generations
                sorted(
                    ships_for_type,
                    key=lambda ship: {
                        "U": 1,
                        "A": 2,
                        "B": 3,
                        "C": 4,
                        "D": 5,
                        "E": 6,
                        "F": 7,
                    }[ship.subtype],
                )
            )

        for ship in result:
            # if ship won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(ship)
            except:
                print("Pickling failed for ship:", ship.id)
                raise
        return result

    def register_ship(self, ship):
        self.ships.append(ship)
        ship.roster_id = self.id

    def register(self, disabled=False):
        registered_rosters.append(self)
        self.disabled = disabled
