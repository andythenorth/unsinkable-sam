# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill


class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    house_position = (
        None  # optional, only used when ship is combined from parts by gestalt_graphics
    )
    # length
    # hull spritesheet file
    # vertical offset if needed, accounting for buy menu especially
    # effects position (list of 3-tuples for x, y, z positions of effects)
    # fatter / thinner ships might need offset adjustments

    def __init__(self):
        print("__init__")

    @property
    def spritesheet_base_name(self):
        return self.hull_type + "_house_" + self.house_position + "_" + self.hull_length


class BargeHouseRear44px(Hull):
    def __init__(self):
        self.hull_length = "44px"
        self.hull_type = "barge"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 14)]


class BargeHouseRear64px(Hull):
    def __init__(self):
        self.hull_length = "64px"
        self.hull_type = "barge"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


class BargeHouseRear96px(Hull):
    def __init__(self):
        self.hull_length = "96px"
        self.hull_type = "barge"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(10, 0, 16)]


class PushBargeHouseRear112px(Hull):
    def __init__(self):
        self.hull_length = "112px"
        self.hull_type = "push_barge"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 1), ("full_load", 3)]
        self.effects_positions = [(13, 2, 16), (13, -2, 16)]


class PushBargeHouseRear128px(Hull):
    def __init__(self):
        self.hull_length = "128px"
        self.hull_type = "push_barge"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 1), ("full_load", 3)]
        self.effects_positions = [(13, 2, 16), (13, -2, 16)]


class ShipHouseForward64px(Hull):
    def __init__(self):
        self.hull_length = "64px"
        self.hull_type = "ship"
        self.house_position = "forward"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseForward80px(Hull):
    def __init__(self):
        self.hull_length = "80px"
        self.hull_type = "ship"
        self.house_position = "forward"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(8, 2, 17), (8, -2, 17)]


class ShipHouseForward96px(Hull):
    def __init__(self):
        self.hull_length = "96px"
        self.hull_type = "ship"
        self.house_position = "forward"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(11, 2, 20), (11, -2, 20)]


class ShipHouseForward112px(Hull):
    def __init__(self):
        self.hull_length = "112px"
        self.hull_type = "ship"
        self.house_position = "forward"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(12, 2, 22), (12, -2, 22)]


class ShipHouseForward128px(Hull):
    def __init__(self):
        self.hull_length = "128px"
        self.hull_type = "ship"
        self.house_position = "forward"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 2)]
        self.effects_positions = [(13, 2, 24), (13, -2, 24)]


class ShipHouseRear44px(Hull):
    def __init__(self):
        self.hull_length = "44px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 14)]


class ShipHouseRear64px(Hull):
    def __init__(self):
        self.hull_length = "64px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(7, 0, 16)]


class ShipHouseRear80px(Hull):
    def __init__(self):
        self.hull_length = "80px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(8, 0, 19)]


class ShipHouseRear96px(Hull):
    def __init__(self):
        self.hull_length = "96px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(11, 0, 24)]


class ShipHouseRear112px(Hull):
    def __init__(self):
        self.hull_length = "112px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(12, 0, 24)]


class ShipHouseRear128px(Hull):
    def __init__(self):
        self.hull_length = "128px"
        self.hull_type = "ship"
        self.house_position = "rear"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 2)]
        self.effects_positions = [(15, 0, 27)]


class TempHouseNone32px(Hull):
    def __init__(self):
        self.hull_length = "32px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone44px(Hull):
    def __init__(self):
        self.hull_length = "44px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone64px(Hull):
    def __init__(self):
        self.hull_length = "64px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone80px(Hull):
    def __init__(self):
        self.hull_length = "80px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


class TempHouseNone96px(Hull):
    def __init__(self):
        self.hull_length = "96px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]
        self.effects_positions = [(11, 0, 24)]


class TempHouseNone112px(Hull):
    def __init__(self):
        self.hull_length = "112px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(11, 0, 12)]


class TempHouseNone128px(Hull):
    def __init__(self):
        self.hull_length = "128px"
        self.hull_type = "temp"
        self.house_position = "none"
        self.load_state_y_offsets = [("empty", -1), ("part_load", 0), ("full_load", 1)]
        self.effects_positions = [(6, 0, 12)]


registered_hulls = {
    "BargeHouseRear44px": BargeHouseRear44px(),
    "BargeHouseRear64px": BargeHouseRear64px(),
    "BargeHouseRear96px": BargeHouseRear96px(),
    "PushBargeHouseRear112px": PushBargeHouseRear112px(),
    "PushBargeHouseRear128px": PushBargeHouseRear128px(),
    "ShipHouseForward64px": ShipHouseForward64px(),
    "ShipHouseForward80px": ShipHouseForward80px(),
    "ShipHouseForward96px": ShipHouseForward96px(),
    "ShipHouseForward112px": ShipHouseForward112px(),
    "ShipHouseForward128px": ShipHouseForward128px(),
    "ShipHouseRear44px": ShipHouseRear44px(),
    "ShipHouseRear64px": ShipHouseRear64px(),
    "ShipHouseRear80px": ShipHouseRear80px(),
    "ShipHouseRear96px": ShipHouseRear96px(),
    "ShipHouseRear112px": ShipHouseRear112px(),
    "ShipHouseRear128px": ShipHouseRear128px(),
    "TempHouseNone32px": TempHouseNone32px(),
    "TempHouseNone44px": TempHouseNone44px(),
    "TempHouseNone64px": TempHouseNone64px(),
    "TempHouseNone80px": TempHouseNone80px(),
    "TempHouseNone96px": TempHouseNone96px(),
    "TempHouseNone112px": TempHouseNone112px(),
    "TempHouseNone128px": TempHouseNone128px(),
}
