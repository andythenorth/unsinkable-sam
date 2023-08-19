class SpriteLayer(object):
    """
    Class to manage vehicle spritelayers, used when composing vehicles from a stack of multiple sprites.
    """

    def __init__(self, ship):
        self.ship = ship

    @property
    def layer_num(self):
        # relies on layer num being order of list when created, should be fine
        return self.ship.gestalt_graphics.spritelayers.index(self)
