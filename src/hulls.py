# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    house_position = None # optional, only used when ship is combined from parts by gestalt_graphics
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
        return self.hull_type + '_house_' + self.house_position +  '_' + self.hull_length

    @property
    def mask_name(self):
        return self.hull_type  + '_waterline_mask_' + self.hull_length

    @property
    def wake_name(self):
        return self.hull_type + '_wake_' + self.hull_length


class BargeHouseRear44px(Hull):
    def __init__(self):
        self.hull_length = '44px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 14)]


class BargeHouseRear64px(Hull):
    def __init__(self):
        self.hull_length = '64px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class BargeHouseRear96px(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(10, 0, 16)]


class PushBargeHouseRear128px(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'push_barge'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(13, 2, 16), (13, -2, 16)]


class ShipHouseForward96px(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForward128px(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'ship'
        self.house_position = 'forward'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(14, 2, 20), (14, -2, 20)]


class ShipHouseRear80px(Hull):
    def __init__(self):
        self.hull_length = '80px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRear96px(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRear112px(Hull):
    def __init__(self):
        self.hull_length = '112px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRear128px(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]
        self.effects_positions = [(11, 0, 24)]


class TempHouseNone32px(Hull):
    def __init__(self):
        self.hull_length = '32px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone44px(Hull):
    def __init__(self):
        self.hull_length = '44px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone64px(Hull):
    def __init__(self):
        self.hull_length = '64px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone96px(Hull):
    def __init__(self):
        self.hull_length = '96px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]
        self.effects_positions = [(11, 0, 24)]


class TempHouseNone128px(Hull):
    def __init__(self):
        self.hull_length = '128px'
        self.hull_type = 'temp'
        self.house_position = 'none'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]
        self.effects_positions = [(6, 0, 12)]


registered_hulls = {'BargeHouseRear44px': BargeHouseRear44px(),
                    'BargeHouseRear64px': BargeHouseRear64px(),
                    'BargeHouseRear96px': BargeHouseRear96px(),
                    'PushBargeHouseRear128px': PushBargeHouseRear128px(),
                    'ShipHouseForward96px': ShipHouseForward96px(),
                    'ShipHouseForward128px': ShipHouseForward128px(),
                    'ShipHouseRear80px': ShipHouseRear80px(),
                    'ShipHouseRear96px': ShipHouseRear96px(),
                    'ShipHouseRear112px': ShipHouseRear112px(),
                    'ShipHouseRear128px': ShipHouseRear128px(),
                    'TempHouseNone32px': TempHouseNone32px(),
                    'TempHouseNone44px': TempHouseNone44px(),
                    'TempHouseNone64px': TempHouseNone64px(),
                    'TempHouseNone96px': TempHouseNone96px(),
                    'TempHouseNone128px': TempHouseNone128px()}
