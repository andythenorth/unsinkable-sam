# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    size_class = 'Define in subclass'
    # length
    # hull spritesheet file
    # vertical offset if needed, accounting for buy menu especially
    # mask_name
    # effects position
    # fatter / thinner ships might need offset adjustments
    print("HULL")

    def __init__(self):
        print("__init__")

    @property
    def spritesheet_name(self):
        return self.size_class +  '_' + self.hull_type + '_house_' + self.house_position

    @property
    def mask_name(self):
        return self.hull_type + '_' + self.size_class + '_hull_mask'

    @property
    def wake_name(self):
        return self.hull_type + '_' + self.size_class + '_wake'

    @property
    def load_state_y_offsets(self):
        # !! obviously incomplete.  _might_ need to also check hull_type for truly accurate y_offsets
        # !! e.g. riverboat hull height doesn't always vary by length; whereas ships do
        if self.size_class == 'small':
            return [('empty', -1), ('part_load', 0), ('full_load', 1)]
        else:
            return [('empty', -1), ('part_load', 1), ('full_load', 3)]


class LargeShipHouseRear(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'rear'


class LargeShipHouseForward(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'rear'


class LargeRiverboatHouseRear(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'


class SmallRiverboatHouseRear(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'


class SmallShipHouseRear(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'ship'
        self.house_position = 'rear'


class TempMini(Hull):
    def __init__(self):
        self.size_class = 'mini'
        self.hull_type = 'ship'
        self.house_position = 'rear'


class TempMicro(Hull):
    def __init__(self):
        self.size_class = 'micro'
        self.hull_type = 'ship'
        self.house_position = 'rear'


registered_hulls = {'LargeRiverboatHouseRear': LargeRiverboatHouseRear(),
                    'LargeShipHouseForward': LargeShipHouseForward(),
                    'LargeShipHouseRear': LargeShipHouseRear(),
                    'SmallRiverboatHouseRear': SmallRiverboatHouseRear(),
                    'SmallShipHouseRear': SmallShipHouseRear(),
                    'TempMini': TempMini(),
                    'TempMicro': TempMicro()}
