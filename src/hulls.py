# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    size_class = 'Define in subclass'
    # length
    wake_spritesheet_name = 'ship_128px'
    # hull spritesheet file
    # vertical offset if needed, accounting for buy menu especially
    # effects position
    # fatter / thinner ships might need offset adjustments


class LargeShipHouseRear(Hull):
    size_class = 'large'
    spritesheet_name = 'large_ship_house_rear'


class LargeShipHouseForward(Hull):
    size_class = 'large'
    spritesheet_name = 'test_large_house_rear'


class LargeRiverboatHouseRear(Hull):
    size_class = 'large'
    spritesheet_name = 'large_riverboat_house_rear'


class SmallRiverboatHouseRear(Hull):
    size_class = 'small'
    spritesheet_name = 'small_riverboat_house_rear'


class SmallShipHouseRear(Hull):
    size_class = 'small'
    spritesheet_name = 'small_ship_house_rear'


class TempMini(Hull):
    size_class = 'mini'
    spritesheet_name = 'mini_ship_house_rear'


class TempMicro(Hull):
    size_class = 'micro'
    spritesheet_name = 'micro_ship_house_rear'


registered_hulls = {'LargeRiverboatHouseRear': LargeRiverboatHouseRear(),
                    'LargeShipHouseForward': LargeShipHouseForward(),
                    'LargeShipHouseRear': LargeShipHouseRear(),
                    'SmallRiverboatHouseRear': SmallRiverboatHouseRear(),
                    'SmallShipHouseRear': SmallShipHouseRear(),
                    'TempMini': TempMini(),
                    'TempMicro': TempMicro()}
