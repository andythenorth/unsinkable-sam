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

    # !! only whilst refactoring
    temp_size_mapping = {'large':'128px', 'small':'96px', 'mini':'64px', 'micro':'44px'}

    def __init__(self):
        print("__init__")

    @property
    def size_class(self):
        # !! only whilst refactoring
        for k, v in self.temp_size_mapping.items():
            if v == self.hull_length:
                return k

    @property
    def spritesheet_name(self):
        return self.hull_type + '_house_' + self.house_position +  '_' + self.hull_length

    @property
    def mask_name(self):
        return self.hull_type  + '_waterline_mask_' + self.hull_length

    @property
    def wake_name(self):
        return self.hull_type + '_wake_' + self.hull_length


class BargeHouseRearMicro(Hull):
    def __init__(self):
        self.hull_length = '44px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 14)]


class BargeHouseRearMini(Hull):
    def __init__(self):
        self.hull_length = '64px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class BargeHouseRearSmall(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(10, 0, 16)]


class PushBargeHouseRearLarge(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'push_barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(13, 2, 16), (13, -2, 16)]


class RiverboatHouseRearSmall(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForwardLarge(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'ship'
        self.house_position = 'forward'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(14, 2, 20), (14, -2, 20)]


class ShipHouseRearLarge(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRearSmall(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForwardSmall(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class TempHouseNoneLarge(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNoneMicro(Hull):
    def __init__(self):
        self.hull_length = '44px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNoneMini(Hull):
    def __init__(self):
        self.hull_length = '64px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNoneSmall(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TwoWayFerryMini(Hull):
    def __init__(self):
        self.hull_length = '64px'
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
                    'TempHouseNoneLarge': TempHouseNoneLarge(),
                    'TempHouseNoneMicro': TempHouseNoneMicro(),
                    'TempHouseNoneMini': TempHouseNoneMini(),
                    'TempHouseNoneSmall': TempHouseNoneSmall(),
                    'TwoWayFerryMini': TwoWayFerryMini()}
