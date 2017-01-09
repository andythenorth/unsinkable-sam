# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # simple class to hold the base hull properties for a ship
    def __init__(self):
        self.size_class = '' # !! probably redundant when this is done
        # length
        # wake spritesheet file?
        # hull spritesheet file
        # vertical offset if needed, accounting for buy menu especially
        # effects position
        # fatter / thinner ships might need offset adjustments


class LargeShipHouseRear(Hull):
    def __init__(self):
        super(LargeShipHouseRear, self).__init__()
        self.size_class = 'large'


class LargeShipHouseForward(Hull):
    def __init__(self):
        super(LargeShipHouseForward, self).__init__()
        self.size_class = 'large'


class LargeRiverboatHouseRear(Hull):
    def __init__(self):
        super(LargeRiverboatHouseRear, self).__init__()
        self.size_class = 'large'


class SmallShipHouseRear(Hull):
    def __init__(self):
        super(SmallShipHouseRear, self).__init__()
        self.size_class = 'small'


registered_hulls = {'LargeRiverboatHouseRear': LargeRiverboatHouseRear(),
                    'LargeShipHouseForward': LargeShipHouseForward(),
                    'LargeShipHouseRear': LargeShipHouseRear(),
                    'SmallShipHouseRear': SmallShipHouseRear()}
