from rosters import registered_rosters
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
        for ship in self.ships:
            # if ship won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(ship)
            except:
                print("Pickling failed for ship:", ship.id)
                # raise # commented out because Coop Jenkins always fails to pickle the ship :(
        return self.ships

    def register_ship(self, ship):
        self.ships.append(ship)
        ship.roster_id = self.id

    def register(self, disabled=False):
        registered_rosters.append(self)
        self.disabled = disabled
