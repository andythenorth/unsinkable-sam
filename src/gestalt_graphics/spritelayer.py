import gestalt_graphics.graphics_constants as graphics_constants


class SpriteLayer(object):
    """
    Class to manage vehicle spritelayers, used when composing vehicles from a stack of multiple sprites.
    """

    # possibly the named ranges should go to constants, but they're not reused, and currently this class is short, so eh, don't abstract too far
    selective_colour_named_ranges = {
        "CC1": [graphics_constants.CC1 + i for i in range(8)],
        "CC2": [graphics_constants.CC2 + i for i in range(8)],
        "CONSTRUCTION_PURPLE": [graphics_constants.construction_purple + i for i in range(8)],
        "DECK_BROWN": [i for i in graphics_constants.deck_brown],
        "HOUSE_MAGIC_RED_COLOUR": [graphics_constants.house_magic_red_colour + i for i in range(8)],
        # be aware that adding negative protocols ("all but X") may have "interesting" side effects if used combinatorially with other rules
        "NONE": [],
        "NOT_1CC": [i for i in range(255) if i not in [graphics_constants.CC1 + i for i in range(8)]],
        # as fallback / default
        "ALL": [i for i in range(255)],
    }

    def __init__(self, ship, **kwargs):
        self.ship = ship
        self.selective_colour_protocols = {
            "hull": kwargs.get("selective_colour_protocols_hull", ["ALL"]),
            "superstructure": kwargs.get(
                "selective_colour_protocols_superstructure", ["ALL"]
            ),
        }
        self.deck_recolour_map = kwargs.get("deck_recolour_map", None)
        self.house_recolour_map = kwargs.get("house_recolour_map", None)
        self.hull_recolour_map = kwargs.get("hull_recolour_map", None)
        self.superstructure_recolour_map = kwargs.get(
            "superstructure_recolour_map", None
        )
        # set to 2 in kwargs if recolour sprite remaps should be applied to 2cc not 1cc (can't do both)
        self.cc_num_to_recolour_for_liveries = kwargs.get(
            "cc_num_to_recolour_for_liveries", 1
        )

    @property
    def layer_num(self):
        # relies on layer num being order of list when created, should be fine
        return self.ship.gestalt_graphics.spritelayers.index(self)

    def get_colours_to_select_for_inclusion(self, component):
        # returns a flat list of colours which will be selected (picked) into a layer from a source sprite image
        result = []
        for protocol in self.selective_colour_protocols[component]:
            result.extend(self.selective_colour_named_ranges[protocol])
        return result
