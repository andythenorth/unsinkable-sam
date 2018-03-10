# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    size_class = 'Define in subclass'
    house_position = None # optional, only used when ship is combined from parts by graphics_processor
    # length
    # hull spritesheet file
    # vertical offset if needed, accounting for buy menu especially
    # mask_name
    # effects position (list of 3-tuples for x, y, z positions of effects)
    # fatter / thinner ships might need offset adjustments

    def __init__(self):
        print("__init__")

    @property
    def spritesheet_name(self):
        return self.hull_type + '_house_' + self.house_position +  '_' + self.size_class

    @property
    def mask_name(self):
        return self.hull_type + '_' + self.size_class + '_waterline_mask'

    @property
    def wake_name(self):
        return self.hull_type + '_' + self.size_class + '_wake'


class BargeHouseRearMicro(Hull):
    def __init__(self):
        self.size_class = 'micro'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 14)]


class BargeHouseRearMini(Hull):
    def __init__(self):
        self.size_class = 'mini'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class BargeHouseRearSmall(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(10, 0, 16)]


class PushBargeHouseRearLarge(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'push_barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(13, 2, 16), (13, -2, 16)]


class RiverboatHouseRearSmall(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForwardLarge(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'forward'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(14, 2, 20), (14, -2, 20)]


class ShipHouseRearLarge(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRearSmall(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForwardSmall(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class TempMiniHouseForward(Hull):
    def __init__(self):
        self.size_class = 'mini'
        self.hull_type = 'temp'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempSmallHouseForward(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'temp'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TwoWayFerryMini(Hull):
    def __init__(self):
        self.size_class = 'mini'
        self.hull_type = 'two_way_ferry'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


registered_hulls = {'BargeHouseRearMicro': BargeHouseRearMicro(),
                    'BargeHouseRearMini': BargeHouseRearMini(),
                    'BargeHouseRearSmall': BargeHouseRearSmall(),
                    'PushBargeHouseRearLarge': PushBargeHouseRearLarge(),
                    'RiverboatHouseRearSmall': RiverboatHouseRearSmall(),
                    'ShipHouseForwardLarge': ShipHouseForwardLarge(),
                    'ShipHouseForwardSmall': ShipHouseForwardSmall(),
                    'ShipHouseRearLarge': ShipHouseRearLarge(),
                    'ShipHouseRearSmall': ShipHouseRearSmall(),
                    'TempMiniHouseForward': TempMiniHouseForward(),
                    'TempSmallHouseForward': TempSmallHouseForward(),
                    'TwoWayFerryMini': TwoWayFerryMini()}
