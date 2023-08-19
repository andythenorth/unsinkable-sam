import gestalt_graphics.graphics_constants as graphics_constants


class SpriteLayer(object):
    """
    Class to manage vehicle spritelayers, used when composing vehicles from a stack of multiple sprites.
    """

    # possibly the named ranges should go to constants, but they're not reused, and currently this class is short, so eh, don't abstract too far
    selective_colour_named_ranges = {
        "CC1": [graphics_constants.CC1 + i for i in range(8)],
        "CC2": [graphics_constants.CC2 + i for i in range(8)],
    }

    def __init__(self, ship, **kwargs):
        self.ship = ship
        self.selective_colour_protocols = kwargs.get("selective_colour_protocols", None)

        self.deck_recolour_map=kwargs.get("deck_recolour_map", None)
        self.house_recolour_map=kwargs.get("house_recolour_map", None)
        self.hull_recolour_map=kwargs.get("hull_recolour_map", None)
        self.superstructure_recolour_map=kwargs.get("superstructure_recolour_map", None)
        # set to 2 in kwargs if recolour sprite remaps should be applied to 2cc not 1cc (can't do both)
        self.cc_num_to_recolour_for_liveries = kwargs.get("cc_num_to_recolour_for_liveries", 1)

    @property
    def layer_num(self):
        # relies on layer num being order of list when created, should be fine
        return self.ship.gestalt_graphics.spritelayers.index(self)

    @property
    def colours_to_select_for_inclusion(self):
        # returns a flat list of colours which will be selected (picked) into a layer from a source sprite image
        # be aware that adding negative protocols ("all but X") may have "interesting" side effects if used combinatorially
        result = []
        if self.selective_colour_protocols == None:
            # just select all if nothing is specified
            result = [i for i in range(255)]
        else:
            for protocol in self.selective_colour_protocols:
                result.extend(self.selective_colour_named_ranges[protocol])
        return result
