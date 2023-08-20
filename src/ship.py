import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import math
from string import (
    Template,
)  # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, "src", "templates"))

import polar_fox
import global_constants  # expose all constants for easy passing to templates
import utils

from gestalt_graphics.gestalt_graphics import (
    GestaltGraphics,
    GestaltGraphicsVisibleCargo,
    GestaltGraphicsSimpleColourRemaps,
)
from gestalt_graphics.spritelayer import SpriteLayer
import gestalt_graphics.graphics_constants as graphics_constants

from hulls import registered_hulls
from rosters import registered_rosters
from vehicles import numeric_id_defender


class BuyableVariant(object):
    """Simple class for ship variants."""

    def __init__(self, ship, livery, numeric_id):
        self.ship = ship
        self.livery = livery
        self.numeric_id = numeric_id
        if self.numeric_id == self.ship.numeric_id:
            self.id = self.ship.id
        else:
            self.id = self.ship.id + str(numeric_id)

    def get_variant_group_parent_vehicle_id(self):
        return None

    def layer_livery_uses_random(self, layer_livery):
        colour_set = layer_livery.get("colour_set", None)
        if colour_set is not None:
            return colour_set.find("random_liveries") != -1
        # fall through to default
        return False

    def get_recolour_strategy_params(self, spritelayer, context=None):
        try:
            layer_livery = self.livery[spritelayer.layer_num]
        except:
            print("shim for layers not matching layer liveries defined", self.ship.id)
            layer_livery = self.livery[0]
        recolour_strategy_num = self.ship.get_recolour_strategy_num(layer_livery)

        if self.layer_livery_uses_random(layer_livery):
            available_liveries = (
                self.ship.get_candidate_liveries_for_randomised_strategy(layer_livery)
            )
            if layer_livery.get("purchase", None) is not None:
                recolour_strategy_num_purchase = self.ship.get_recolour_strategy_num(
                    layer_livery, context="purchase"
                )
            else:
                recolour_strategy_num_purchase = available_liveries[0]
        else:
            # we have to provide 8 options for nml params, but in this case they are all unused, so just pass them as 0
            available_liveries = [0, 0, 0, 0, 0, 0, 0, 0]
            # purchase strategy will be same as non-purchase
            recolour_strategy_num_purchase = recolour_strategy_num

        cc_num_to_recolour = spritelayer.cc_num_to_recolour_for_liveries
        flag_use_weathering = layer_livery.get("use_weathering", False)
        flag_context_is_purchase = True if context == "purchase" else False

        params_numeric = [
            cc_num_to_recolour,
            flag_use_weathering,
            flag_context_is_purchase,
            recolour_strategy_num,
            recolour_strategy_num_purchase,
        ]

        params_numeric.extend(available_liveries)

        # int used to convert False|True bools to 0|1 values for nml
        return ", ".join(str(int(i)) for i in params_numeric)


class Ship(object):
    """Base class for all types of ships."""

    def __init__(self, name, numeric_id, gen, subtype, hull, **kwargs):
        self.id = self.base_id + "_gen_" + str(gen) + subtype
        self._name = name  # private var because 'name' is accessed via @property method to add subtype string
        self.numeric_id = numeric_id
        numeric_id_defender.append(numeric_id)
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        self.roster_id = "default"  # only one roster currently
        self.roster.register_ship(self)
        # subtypes determine capacity, and are mapped to hull sizes in subclass
        self.subtype = subtype
        # base hull (defines length, wake graphics, hull graphics if composited etc)
        self.hull = registered_hulls[hull + self.hull_mapping[self.subtype]]
        # generation used to set default intro dates, speed etc unless explicitly set by a vehicle
        self.gen = gen
        # if gen is used, the calculated intro date can be adjusted with +ve or -ve offset
        self.intro_date_offset = kwargs.get("intro_date_offset", None)
        # set gestalt_graphics to a GestaltGraphics-type object per subclass
        self.gestalt_graphics = None
        # option for multiple default cargos, cascading if first cargo(s) are not available
        self.default_cargos = []
        # speed is determined in sub class, or can be over-ridden by individual vehicles
        # optional per-vehicle speed
        self._speed = kwargs.get("speed", None)
        # default to freight speed_class for convenience, over-ride in subclasses as needed
        self.speed_class = "freight"  # over-ride this for, e.g. fast_freight consists
        # default standard capacities_by_subtype for freight for convenience, over-ride in subclasses as needed
        self.capacities_by_subtype = {
            "A": 80,
            "B": 160,
            "C": 240,
            "D": 360,
            "E": 540,
            "F": 810,
        }  # over-ride this for, e.g. pax ship capacities_by_subtype
        # extra type info, better over-ride in subclass
        self.str_type_info = "EMPTY"  # unused currently
        # nml-ish props, mostly optional
        self.sound_effect = kwargs.get("sound_effect", "SOUND_DEPARTURE_CARGO_SHIP")
        self.vehicle_life = kwargs.get(
            "vehicle_life", 100
        )  # default 100 years, assumes 2 generations of ships 1850-2050
        self._buy_cost = kwargs.get("buy_cost", None)
        # !! temp - these need move to subtypes at some point (or as over-rides)
        self.fixed_run_cost_factor = 3.5
        self.fuel_run_cost_factor = 1.0
        # over-ride loading speed in subclasses as needed (suggested values are 0.5 for slower loading and 2 for faster loading)
        self.loading_speed_multiplier = 1
        self.cargo_age_period = kwargs.get(
            "cargo_age_period", global_constants.CARGO_AGE_PERIOD
        )
        # by default ships have multiple capacity options, refittable in depot
        self.capacity_is_refittable_by_cargo_subtype = kwargs.get(
            "capacity_is_refittable_by_cargo_subtype", True
        )
        # most ships use steam effect_spawn_model so set default, over-ride in ships as needed
        self.effect_spawn_model = kwargs.get(
            "effect_spawn_model", "EFFECT_SPAWN_MODEL_STEAM"
        )
        self.effect_type = kwargs.get("effect_type", None)
        # what length to use for cargo sprites in cargo compositing
        self.cargo_length = kwargs.get("cargo_length", None)
        # aids 'project management'
        self.sprites_complete = kwargs.get("sprites_complete", False)

    def resolve_buyable_variants(self):
        # this potentially has sequencing issues as it depends on gestalt_graphics
        # and we need to make sure that's initialised before attempting to create buyable variants
        # as a workaround, currently we're calling this only at template render time
        # the basic form of buyable variants is driven by recolour liveries
        # other forms could be added, or variant groups could be created in other ways, e.g. using different ship classes
        result = []
        for livery in self.gestalt_graphics.liveries:
            # we don't need to know the actual livery here, we rely on matching them up later by indexes, which is fine
            numeric_id = self.numeric_id + len(result)
            result.append(BuyableVariant(self, livery=livery, numeric_id=numeric_id))
        return result

    @property
    def num_unique_spritesheet_suffixes(self):
        print("remove num_unique_spritesheet_suffixes")
        return 1

    @property
    def hull_mapping(self):
        # default mapping of subtypes to hull lengths; over-ride in subclasses as needed
        return {
            "A": "44px",
            "B": "64px",
            "C": "80px",
            "D": "96px",
            "E": "112px",
            "F": "128px",
        }

    @property
    def hull_spritesheet_name(self):
        # generally don't access hull.spritesheet_base_name directly, it needs the gen inserted
        return self.hull.spritesheet_base_name + "_gen_" + str(self.gen)

    @property
    def speed(self):
        # automatic speed, but can over-ride by passing in kwargs for consist
        if self._speed:
            return self._speed
        elif self.speed_class:
            speeds = self.roster.speeds[self.speed_class]
            return speeds[max([year for year in speeds if self.intro_date >= year])]
        else:
            # assume no speed limit
            return None

    def get_speed_adjusted_for_param(self, speed_index):
        # there is a speed adjustment parameter, use that to look up a speed factor
        speed_factors = [0.67, 1, 1.33]
        # allow that integer maths is needed for newgrf cb results; rounding up for safety, capped at max ship speed
        result = int(
            min(math.ceil(3.2 * self.speed * speed_factors[speed_index]), 79 * 3.2)
        )
        return result

    @property
    def adjusted_model_life(self):
        return "VEHICLE_NEVER_EXPIRES"

    @property
    def running_cost(self):
        # calculate a running cost
        gross_tonnage = (
            self.default_capacity * 1.25
        )  # no real need to vary this by ship type
        fixed_run_cost = self.fixed_run_cost_factor * global_constants.FIXED_RUN_COST
        fuel_run_cost = (
            self.fuel_run_cost_factor * gross_tonnage * global_constants.FUEL_RUN_COST
        )
        calculated_run_cost = int(
            (fixed_run_cost + fuel_run_cost) / 98
        )  # divide by magic constant to get costs as factor in 0-255 range
        return min(calculated_run_cost, 255)  # cost factor is a byte, can't exceed 255

    @property
    def intro_date(self):
        # automatic intro_date, but can over-ride by passing in kwargs for consist
        assert self.gen != None, (
            "%s consist has no gen set, which is incorrect" % self.id
        )
        result = self.roster.intro_dates["DEFAULT"][self.gen - 1]
        if self.intro_date_offset is not None:
            result = result + self.intro_date_offset
        return result

    @property
    def refittable_capacity_factors(self):
        # default refittable capacities_by_subtype are [base capacity, 25% underload, 25% overload]
        # over-ride this in the subclass if necessary
        return [1, 0.75, 1.25]

    @property
    def capacities_refittable(self):
        # ships can refit multiple capacities_by_subtype
        # faff: mail ships need to divide default capacity for freight; freight ships multiply default capacity for mail
        # this is theoretically extensible to other cargos/classes, but will get ugly fast eh?
        if self.default_cargos[0] == "MAIL":
            default_base = self.default_capacity / global_constants.mail_multiplier
            mail_base = self.default_capacity
        else:
            default_base = self.default_capacity
            mail_base = self.default_capacity * global_constants.mail_multiplier

        capacities_default = [
            int(default_base * capacity_factor)
            for capacity_factor in self.refittable_capacity_factors
        ]
        capacities_mail = [
            int(mail_base * capacity_factor)
            for capacity_factor in self.refittable_capacity_factors
        ]
        result = {"default": capacities_default, "mail": capacities_mail}
        return result

    @property
    def default_capacity(self):
        return self.capacities_by_subtype[self.subtype]

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [
                cargo_classes.append(cargo_class)
                for cargo_class in global_constants.base_refits_by_class[i]
            ]
        return ",".join(set(cargo_classes))  # use set() here to dedupe

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ",".join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ",".join(self.label_refits_disallowed)

    @property
    def loading_speed(self):
        # loading speed is *not* normalised per capacity for ships, unlike vehicles in Road Hog / Iron Horse
        # 10 is default OTTD value for ships, seems fine to me
        return 10 * self.loading_speed_multiplier

    @property
    def buy_cost(self):
        if self._buy_cost is not None:
            return self._buy_cost
        # !! this is an initial attempt to put buy cost in the correct bracket, but this is not finished !!
        # !! likely this should account for pax / mail / freight etc, this would be better done by sticking a multiplier on the subclass
        return self.default_capacity / 10

    @property
    def name_suffix_as_string_name(self):
        # used in ship name string only
        # may be over-ridden in subclasses
        return "STR_NAME_" + self.base_id.upper()

    def get_str_type_info(self):
        # makes a string id for nml
        return "STR_" + self.str_type_info

    @property
    def name(self):
        return (
            "string(STR_NAME_"
            + self.id.upper()
            + ", string("
            + self.name_suffix_as_string_name
            + "))"
        )

    def get_buy_menu_string(self):
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_EMPTY))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info())

    @property
    def roster(self):
        for roster in registered_rosters:
            if self.roster_id == roster.id:
                return roster

    def get_expression_for_rosters(self):
        # the working definition is one and only one roster per vehicle
        return "param[2]==" + str(self.roster.numeric_id - 1)

    def get_nml_expression_for_default_cargos(self):
        # sometimes first default cargo is not available, so we use a list
        # this avoids unwanted cases like piece cargo ships defaulting to mail when goods cargo not available
        # if there is only one default cargo, the list just has one entry, that's no problem
        if len(self.default_cargos) == 1:
            return self.default_cargos[0]
        else:
            # build stacked ternary operators for cargos
            result = self.default_cargos[-1]
            for cargo in reversed(self.default_cargos[0:-1]):
                result = 'cargotype_available("' + cargo + '")?' + cargo + ":" + result
            return result

    def get_spriterow_counts(self):
        # !! overly nested as assumes that there would be multiple units, doesn't apply to ships
        result = []
        unit_rows = []
        # assumes gestalt_graphics is used to handle any other rows, no other cases at time of writing, could be changed eh?
        unit_rows.extend(self.gestalt_graphics.get_output_row_counts_by_type())
        result.append(unit_rows)
        return result

    @property
    def buy_menu_width(self):
        # currently contains no provision for custom widths
        # but if needed, add _buy_menu_width from constructor kwargs, and check existence of that here
        # standard sizes are multiples of 32, except first size, where 32 is just too small to make a nice sprite
        return int(self.hull.hull_length.split("px")[0])

    @property
    def buy_menu_bb_y_offset(self):
        # !! scaffolding for variable height ships that need offsets on their bounding box for buy menu
        # !! returns a fixed value currently, more wasn't needed yet :P Possibly delete?
        return 16

    @property
    def offsets(self):
        # currently contains no provision for custom offsets
        # but if needed, add _offsets prop from constructor kwargs, and check existence of that here (otherwise returning defaults)
        return global_constants.vehicle_offsets[self.hull.hull_length]

    def get_nml_expression_for_cargo_variant_random_switch(
        self, spritelayer, cargo_id=None
    ):
        switch_id = (
            self.id
            + "_switch_graphics"
            + ("_" + str(cargo_id) if cargo_id is not None else "")
            + ("_" + str(spritelayer.layer_num))
        )
        return "SELF," + switch_id + ", bitmask(TRIGGER_VEHICLE_ANY_LOAD)"

    def get_expression_for_effects(self):
        # provides part of nml switch for effects (smoke), or none if no effects defined
        if self.effect_type is not None:
            result = []
            for index, effect_position in enumerate(self.hull.effects_positions):
                formatted_position = ",".join(str(i) for i in effect_position)
                result.append(
                    "STORE_TEMP(create_effect("
                    + self.effect_type
                    + ","
                    + formatted_position
                    + "), 0x10"
                    + str(index)
                    + ")"
                )
            return "[" + ",".join(result) + "]"
        else:
            return 0

    def get_recolour_strategy_num(self, livery, context=None):
        if context == "purchase":
            colour_set = livery["purchase"]
        else:
            colour_set = livery["colour_set"]
        # > 102 = strategy num will be randomised to one of the other strategy nums
        # 101 = use colour set complementary to player company colour
        # 100 = use colour set from player company colour
        # 0..99 = use colour set number directly (look up by name)
        recolour_strategy_mapping = {
            "company_colour": 100,
            "complement_company_colour": 101,
            "random_liveries_1": 102,
            "random_liveries_2": 103,
            "random_liveries_3": 104,
            "random_liveries_4": 105,
            "random_liveries_5": 106,
            "random_liveries_6": 107,
            "random_liveries_7": 108,
            "random_liveries_8": 109,
            "random_liveries_9": 110,
            "random_liveries_10": 111,
            "random_liveries_11": 112,
        }
        if colour_set in recolour_strategy_mapping.keys():
            return recolour_strategy_mapping[colour_set]
        else:
            return list(global_constants.colour_sets.keys()).index(colour_set)

    def get_candidate_liveries_for_randomised_strategy(self, livery):
        # this will only work with recolour (remap) liveries as of August 2023
        result = []
        for candidate_livery in self.gestalt_graphics.liveries:
            if (
                candidate_livery["colour_set"]
                in global_constants.ship_livery_mixes[livery["colour_set"]]
            ):
                candidate_livery_strategy_num = self.get_recolour_strategy_num(
                    candidate_livery
                )
                result.append(candidate_livery_strategy_num)
        # length of result *must* be 8, as we have up to 8 liveries per buyable wagon variant, and we must provide values for 8 registers
        # this just crudely extends the list, repeating values as needed
        extension = result[0 : 8 - len(result)]
        if len(extension) == 0:
            raise BaseException(
                self.id
                + " get_candidate_liveries_for_randomised_strategy: extension list too short "
                + str(extension)
                + "; \n this is probably because we're slicing 8, and have more than 8 colours defined; which will fail;"
                + "; \n there are now more random bits available for OpenTTD 14 so this might be solvable"
            )
        # !! it's possible this doesn't close
        while len(result) < 8:
            result.extend(extension)
        # yes, I'm sure we could avoid over-extending and then slicing the list, but eh, life is short
        if (len(result)) > 8:
            result = result[0:8]
        return result

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message(
                    "Warning: ship "
                    + self.id
                    + " references cargo label "
                    + i
                    + " which is not defined in the cargo table"
                )

    def render(self):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        # templating
        template = templates[self.gestalt_graphics.nml_template]
        nml_result = template(
            ship=self,
            global_constants=global_constants,
            graphics_constants=graphics_constants,
        )
        return nml_result


class BulkBase(Ship):
    """
    Limited set of bulk (mineral) cargos.  Equivalent of Road Hog dump hauler and Iron Horse dump car.
    Tend to be just a single unfitted box hold, distinguishing them from general cargo vessels which have divided holds, tween-decks etc,.
    Mini-bulkers may be self-discharging (crane or conveyor).  Bulk barges less likely to be.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["dump_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            "non_dump_bulk"
        ]
        self.default_cargos = global_constants.default_cargos["dump"]
        self.loading_speed_multiplier = 2


class BulkBarge(BulkBase):
    """
    Bulk barge
    """

    def __init__(self, **kwargs):
        self.base_id = "bulk_barge"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC1,
            house_recolour_map=graphics_constants.house_recolour_roof_CC1_1,
            liveries=[["_DEFAULT"]],
        )


class BulkShip(BulkBase):
    """
    Standard bulk ship
    """

    def __init__(self, **kwargs):
        self.base_id = "bulk_ship"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            spritelayers=[
                SpriteLayer(
                    self,
                    house_recolour_map=graphics_constants.house_recolour_roof_rust_1,
                    hull_recolour_map=graphics_constants.hull_recolour_CC1,
                ),
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC1"],
                )
            ],
            liveries=[
                ["_DEFAULT", "COMPANY_COLOUR_USE_WEATHERING"],
                ["COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING", "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"],
                ["FREIGHT_GREY", "FREIGHT_RUSTY_BLACK"],
                ["FREIGHT_NIGHTSHADE", "FREIGHT_OIL_BLACK"],
                ["FREIGHT_RUSTY_BLACK", "FREIGHT_OIL_BLACK"],
                ["FREIGHT_RUBY", "FREIGHT_BAUXITE"],
                ["FREIGHT_BAUXITE", "FREIGHT_BAUXITE"],
                ["FREIGHT_OCHRE", "FREIGHT_BAUXITE"],
                ["FREIGHT_MINT_GREEN", "FREIGHT_PEWTER"],
                ["FREIGHT_TEAL", "FREIGHT_PEWTER"],
            ],
        )

    @property
    def name_suffix_as_string_name(self):
        # used in ship name string only
        # may be over-ridden in subclasses
        if self.gen < 3:
            return "STR_NAME_COLLIER"
        else:
            return "STR_NAME_MINI_BULKER"


class CargoLiner(Ship):
    """
    Piece goods cargos, other selected cargos.  Equivalent of Road Hog box hauler and Iron Horse box car / van.
    IRL: "GCV", "Break-bulk", "Pallet carrier", also cargo packet (but not mail packet)
    Not "box ship" because IRL they are container carriers (yair).
    The name is ultimately just a generic solution to 'this is not quite a general freighter', that doesn't describe the specific shape or cargo type or RL trade name.
    Many name variants were tried, Cargo Liner seemed to stick.
    """

    def __init__(self, **kwargs):
        self.base_id = "cargo_liner"
        super().__init__(**kwargs)
        self.class_refit_groups = ["packaged_freight"]
        self.label_refits_allowed = [
            "MAIL",
            "GRAI",
            "WHEA",
            "MAIZ",
            "FRUT",
            "BEAN",
            "NITR",
        ]  # Iron Horse compatibility
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = global_constants.default_cargos["box"]
        # Graphics configuration
        # might need to split house stuff down to individual ships / barges?
        if self.subtype in ["A", "C", "E"]:
            house_recolour_map = graphics_constants.house_recolour_roof_silver_1
        elif self.subtype in ["B", "D", "F"]:
            house_recolour_map = graphics_constants.house_recolour_roof_dark_red_1
        else:
            house_recolour_map = graphics_constants.house_recolour_roof_CC1_1
        hull_recolour_map=graphics_constants.hull_recolour_CC1
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    hull_recolour_map=hull_recolour_map,
                    house_recolour_map=house_recolour_map,
                    superstructure_recolour_map=hull_recolour_map,
                ),
            ],
            liveries=[
                ["_DEFAULT"],
                ["FREIGHT_PEWTER"],
                ["FREIGHT_OIL_BLACK"],
                ["FREIGHT_RUBY"],
                ["FREIGHT_GREY"],
                ["FREIGHT_TEAL"],
                ["FREIGHT_SULPHUR"],
            ],
        )


class ContainerCarrier(Ship):
    """
    Refits to limited range of freight cargos, shows container graphics according to load state.
    """

    def __init__(self, **kwargs):
        self.base_id = "bulk_carrier"
        super().__init__(**kwargs)
        self.template = "container_carrier.pynml"
        # maintain other sets (e.g. IH etc) when changing container refits
        self.class_refit_groups = ["express_freight", "packaged_freight"]
        self.label_refits_allowed = ["FRUT", "WATR"]
        self.label_refits_disallowed = ["FISH", "LVST", "OIL_", "TOUR", "WOOD"]
        self.default_cargos = global_constants.default_cargos["intermodal"]


class CoveredHopperCarrier(Ship):
    """
    Bulk cargos needing covered protection.
    """

    def __init__(self, **kwargs):
        self.base_id = "bulk_carrier"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = global_constants.allowed_refits_by_label[
            "covered_hoppers"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos["covered_mineral"]
        self.loading_speed_multiplier = 2
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC1,
            liveries=[["_DEFAULT"]],
        )


class CryoTanker(Ship):
    """
    Specialist tankers for gases under pressure, e.g. Oxygen, Chlorine etc.
    IRL these are pressurised, semi-pressurised, fully refrigerated etc.  We wavey hands that distinction here.
    """

    def __init__(self, **kwargs):
        self.base_id = "cryo_tanker"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = global_constants.allowed_refits_by_label[
            "cryo_gases"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos["cryo_gases"]
        self.loading_speed_multiplier = 2
        # Graphics configuration
        hull_recolour_map = graphics_constants.hull_recolour_CC1
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    deck_recolour_map=graphics_constants.deck_recolour_map_dark_red_1,
                    hull_recolour_map=hull_recolour_map,
                    superstructure_recolour_map=hull_recolour_map,
                ),
                # knock the house roof out specifically so we can make it CC for all liveries
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["HOUSE_MAGIC_RED_COLOUR"],
                    selective_colour_protocols_superstructure=["NONE"],
                    house_recolour_map=graphics_constants.house_recolour_roof_CC1_1,
                ),
                SpriteLayer(
                    self,
                    # pick certain pipes / hatch covers off the superstructure and recolour
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CONSTRUCTION_PURPLE"],
                    superstructure_recolour_map=graphics_constants.construction_purple_recolour_CC1,
                ),
                SpriteLayer(
                    self,
                    # pick the tanks out
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC1"],
                ),
            ],
            liveries=[
                [
                    "_DEFAULT",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "FREIGHT_SILVER",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "FREIGHT_SILVER",
                ],
                [
                    "FREIGHT_PEWTER",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_SILVER",
                ],
                [
                    "FREIGHT_NIGHTSHADE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_PEWTER",
                    "FREIGHT_SILVER",
                ],
                [
                    "FREIGHT_TEAL",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_TEAL",
                    "FREIGHT_SILVER",
                ],
                [
                    "FREIGHT_RUSTY_BLACK",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_RUSTY_BLACK",
                    "FREIGHT_PEWTER",
                ],
                [
                    "FREIGHT_BAUXITE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_BAUXITE",
                    "FREIGHT_PEWTER",
                ],
                [
                    "FREIGHT_RUBY",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "FREIGHT_RUBY",
                ],
                [
                    "FREIGHT_OCHRE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "FREIGHT_BAUXITE",
                    "FREIGHT_RUBY",
                ],
                [
                    "FREIGHT_SULPHUR",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "FREIGHT_OCHRE",
                ],
            ],
        )


class EdiblesTanker(Ship):
    """
    Gallons and gallons and gallons of wine, milk or water.  Except in metric systems, where it's litres.
    """

    def __init__(self, **kwargs):
        self.base_id = "edibles_tanker"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = global_constants.allowed_refits_by_label[
            "edible_liquids"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos["edibles_tank"]
        # Graphics configuration
        hull_recolour_map = graphics_constants.hull_recolour_CC1
        deck_recolour_map = {
            70: 1,
            60: 2,
            72: 3,
            123: 4,
            74: 5,
            75: 6,
        }
        house_recolour_map = (
            graphics_constants.house_recolour_roof_CC1_1.copy()
        )  # copy because update is used to extend the map
        house_recolour_map.update(graphics_constants.recolour_CC2_to_CC1)
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    hull_recolour_map=hull_recolour_map,
                    deck_recolour_map=deck_recolour_map,
                    superstructure_recolour_map=hull_recolour_map,
                ),
                # knock the house roof out specifically so we can make it CC for all liveries
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["HOUSE_MAGIC_RED_COLOUR"],
                    selective_colour_protocols_superstructure=["NONE"],
                    house_recolour_map=house_recolour_map,
                ),
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC1"],
                ),
            ],
            liveries=[
                [
                    "CC_WHITE",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "FREIGHT_SILVER",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                ],
                [
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                ],
                [
                    "FREIGHT_RUSTY_BLACK",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                ],
                [
                    "FREIGHT_OCHRE",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                ],
                [
                    "FREIGHT_SULPHUR",
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                ],
            ],
        )


class FlatDeckBarge(Ship):
    """
    Flat deck, no holds - refits most cargos, not bulk.
    !! Not used?? - this was added as equivalent of Horse flat cars, but that mode doesn't apply to shipping.
    """

    def __init__(self, **kwargs):
        self.base_id = "flat_deck"
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = global_constants.default_cargos["flat"]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat",
            spritelayers=[SpriteLayer(self)],
            liveries=[["_DEFAULT"]],
        )

    # class FruitVegCarrier(Ship):
    """
    Fruit and vegetables, with improved decay rate
    !! deprecated - this was added as equivalent of Horse fruit & veg cars, but that mode doesn't apply to shipping - use reefer / dry cargo instead.
    """


class FreighterBase(Ship):
    """
    General purpose freight vessel type.
    No pax or mail cargos, refits any other cargo including liquids (in barrels or containers).
    Tend to be fitted with divided holds, tween-decks etc, distinguishing them from mini-bulkers which are just a single unfitted box hold.
    IRL: "multi-purpose vessel" (modern designation), or "general cargo vessel" or "dry cargo vessel".  Confusing much?
    Ship version is probably geared (cranes), barge version is probably not.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["all_freight"]
        self.label_refits_allowed = []  # no specific labels needed, refits all freight
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = global_constants.default_cargos["open"]


class FreighterBarge(FreighterBase):
    """
    Barge-type freighter
    """

    def __init__(self, **kwargs):
        self.base_id = "freighter_barge"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            piece="open",
            spritelayers=[SpriteLayer(self)],
            house_recolour_map=graphics_constants.house_recolour_roof_CC1_1,
            liveries=[["_DEFAULT"]],
        )


class FreighterShip(FreighterBase):
    """
    Standard freighter
    """

    def __init__(self, **kwargs):
        self.base_id = "freighter_ship"
        super().__init__(**kwargs)
        # Graphics configuration
        if self.subtype in ["A", "C", "E"]:
            house_recolour_map = graphics_constants.house_recolour_roof_dark_red_1
        elif self.subtype in ["B", "D", "F"]:
            house_recolour_map = graphics_constants.house_recolour_roof_silver_1
        else:
            house_recolour_map = None
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            piece="open",
            spritelayers=[
                SpriteLayer(
                    self,
                    house_recolour_map=house_recolour_map,
                    hull_recolour_map=graphics_constants.hull_recolour_CC1,
                )
            ],
            liveries=[
                ["_DEFAULT"],
                ["FREIGHT_PEWTER"],
                ["FREIGHT_OIL_BLACK"],
                ["FREIGHT_RUBY"],
                ["FREIGHT_GREY"],
                ["FREIGHT_TEAL"],
                ["FREIGHT_RUSTY_BLACK"],
            ],
        )


class LivestockCarrier(Ship):
    """
    Special type for livestock (as you might guess).
    """

    def __init__(self, **kwargs):
        self.base_id = "livestock_carrier"
        super().__init__(**kwargs)
        self.class_refit_groups = ["empty"]
        self.label_refits_allowed = [
            "LVST"
        ]  # set to livestock by default, don't need to make it refit
        self.label_refits_disallowed = []
        self.default_cargos = ["LVST"]  # no need for fallbacks, single refit
        # improved decay rate
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_silver,
            house_recolour_map=graphics_constants.house_recolour_roof_dark_red_1,
            liveries=[["_DEFAULT"]],
        )


class LogTug(Ship):
    """
    Specialist type for hauling logs only, has some specialist refit and speed behaviours.
    """

    def __init__(self, **kwargs):
        self.base_id = "log_tug"
        super().__init__(**kwargs)
        self.template = "log_tug.pynml"
        self.class_refit_groups = ["empty"]
        self.label_refits_allowed = ["WOOD"]
        self.label_refits_disallowed = []
        self.default_cargos = ["WOOD"]  # no need for fallbacks, single refit


class MailShip(Ship):
    """
    A relatively fast vessel type for mail and express freight.
    """

    def __init__(self, **kwargs):
        self.base_id = "mail_ship"
        super().__init__(**kwargs)
        self.speed_class = "pax_mail"
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = global_constants.default_cargos["mail"]
        # these are the mail capacities_by_subtype for ships that have MAIL as default; freight capacity will be divided by global_constants.mail_multipler
        self.capacities_by_subtype = {
            "A": 40,
            "B": 120,
            "D": 360,
        }  # no large mail ships, by design
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC1,
            liveries=[["_DEFAULT"]],
        )


class PaxShipBase(Ship):
    """
    Common base class for passenger vessels.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos["pax"]
        self.capacities_by_subtype = {"A": 40, "B": 125, "C": 300, "D": 720}
        self.sound_effect = "SOUND_DEPARTURE_FERRY"


class PaxFastLoadingShip(PaxShipBase):
    """
    Fast-loading passenger vessel - better suited to short routes; keep same speed as luxury pax ship for balancing reasons.
    """

    def __init__(self, **kwargs):
        self.base_id = "pax_fast_loading"
        super().__init__(**kwargs)
        self.speed_class = "pax_mail"
        self.loading_speed_multiplier = 3
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC1,
            liveries=[["_DEFAULT"]],
        )

    @property
    def hull_mapping(self):
        # default mapping of subtypes to hull lengths; over-ride in subclasses as needed
        # !! WIP the actual mappings here are somewhat undecided
        return {"A": "44px", "B": "44px", "C": "64px", "D": "96px"}


class PaxLuxuryShip(PaxShipBase):
    """
    Luxury passenger vessel - better suited to long routes; keep same speed as fast-loading pax ship for balancing reasons.
    """

    def __init__(self, **kwargs):
        self.base_id = "pax_luxury"
        super().__init__(**kwargs)
        self.speed_class = "pax_mail"
        self.cargo_age_period = 3 * global_constants.CARGO_AGE_PERIOD
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC2,
            liveries=[["_DEFAULT"]],
        )

    @property
    def hull_mapping(self):
        # default mapping of subtypes to hull lengths; over-ride in subclasses as needed
        # !! WIP the actual mappings here are somewhat undecided
        return {"A": "44px", "B": "64px", "C": "96px", "D": "128px"}


class Reefer(Ship):
    """
    Refits to limited range of refrigerated cargos, with 'improved' cargo decay rate.
    """

    def __init__(self, **kwargs):
        self.base_id = "reefer"
        super().__init__(**kwargs)
        self.class_refit_groups = ["refrigerated_freight"]
        self.label_refits_allowed = (
            []
        )  # no specific labels needed, refits all cargos that have refrigerated class
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos["reefer"]
        # improved decay rate
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        # Graphics configuration
        hull_recolour_map = graphics_constants.hull_recolour_CC1
        deck_recolour_map = {
            70: 1,
            60: 2,
            71: 2,
            72: 3,
            73: 4,
            123: 4,
            74: 5,
            75: 6,
        }
        house_recolour_map = (
            graphics_constants.house_recolour_roof_dark_red_1.copy()
        )  # copy because update is used to extend the map
        # extend to invert funnel CC
        house_recolour_map.update(graphics_constants.recolour_CC2_to_CC1)
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    hull_recolour_map=hull_recolour_map,
                    house_recolour_map=house_recolour_map,
                    deck_recolour_map=deck_recolour_map,
                    superstructure_recolour_map=hull_recolour_map,
                ),
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC1"],
                ),
                SpriteLayer(
                    self,
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC2"],
                    superstructure_recolour_map=graphics_constants.recolour_CC2_to_CC1,
                ),
            ],
            liveries=[
                [
                    "CC_WHITE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "FREIGHT_SILVER",
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING",
                    "CC_WHITE",
                    "COMPANY_COLOUR_USE_WEATHERING",
                ],
                [
                    "FREIGHT_TEAL",
                    "CC_WHITE",
                    "FREIGHT_TEAL",
                ],
            ],
        )


class TankerBase(Ship):
    """
    Ronseal ("does what it says on the tin", for those without extensive knowledge of UK advertising).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = "vehicle_with_visible_cargo.pynml"
        self.class_refit_groups = ["liquids"]
        self.label_refits_allowed = (
            []
        )  # refits most cargos that have liquid class even if they might be edibles
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            "non_generic_liquids"
        ]
        self.default_cargos = global_constants.default_cargos["tank"]


class TankerBarge(TankerBase):
    """
    Tanker barge
    """

    def __init__(self, **kwargs):
        self.base_id = "tanker_barge"
        super().__init__(**kwargs)
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            deck_recolour_map=graphics_constants.deck_recolour_map_dark_red_1,
            house_recolour_map=graphics_constants.house_recolour_roof_CC1_1,
            liveries=[["_DEFAULT"]],
        )


class TankerShip(TankerBase):
    """
    Standard tanker
    """

    def __init__(self, **kwargs):
        self.base_id = "tanker_ship"
        super().__init__(**kwargs)
        if self.subtype in ["A", "C", "E"]:
            house_recolour_map = (
                graphics_constants.house_recolour_roof_dark_red_1.copy()
            )  # copy because update is used to extend the map
            house_recolour_map.update(graphics_constants.recolour_CC2_to_CC1)
        elif self.subtype in ["B", "D", "F"]:
            house_recolour_map = (
                graphics_constants.house_recolour_roof_silver_1.copy()
            )  # copy because update is used to extend the map
        else:
            house_recolour_map = []
        house_recolour_map.update(graphics_constants.recolour_CC2_to_CC1)
        hull_recolour_map = graphics_constants.hull_recolour_CC1
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    deck_recolour_map=graphics_constants.deck_recolour_map_dark_red_1,
                    hull_recolour_map=hull_recolour_map,
                    house_recolour_map=house_recolour_map,
                    superstructure_recolour_map=hull_recolour_map,
                ),
                SpriteLayer(
                    self,
                    # pick certain pipes / hatch covers off the superstructure and recolour
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CONSTRUCTION_PURPLE"],
                    superstructure_recolour_map=graphics_constants.construction_purple_recolour_CC1,
                ),
            ],
            liveries=[
                ["_DEFAULT", "COMPANY_COLOUR_USE_WEATHERING"],
                ["COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING", "COMPANY_COLOUR_USE_WEATHERING"],
                ["FREIGHT_SILVER", "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"],
                ["FREIGHT_GREY", "FREIGHT_PEWTER"],
                ["FREIGHT_OIL_BLACK", "FREIGHT_PEWTER"],
                ["FREIGHT_MINT_GREEN", "FREIGHT_GREMLIN_GREEN"],
                ["FREIGHT_TEAL", "FREIGHT_TEAL"],
                ["FREIGHT_RUSTY_BLACK", "FREIGHT_PEWTER"],
                ["FREIGHT_BAUXITE", "FREIGHT_PEWTER"],
                ["FREIGHT_RUBY", "FREIGHT_BAUXITE"],
                ["FREIGHT_OCHRE", "FREIGHT_BAUXITE"],
                ["FREIGHT_SULPHUR", "FREIGHT_OCHRE"],
            ],
        )


# not in alphabetical order as uses TankerBase
class ProductTankerShip(TankerBase):
    """
    Visual variant of the standard tanker, for visual variety
    """

    def __init__(self, **kwargs):
        self.base_id = "product_tanker_ship"
        super().__init__(**kwargs)
        # Graphics configuration
        hull_recolour_map = graphics_constants.hull_recolour_CC1
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[
                SpriteLayer(
                    self,
                    deck_recolour_map=graphics_constants.deck_recolour_map_dark_red_1,
                    hull_recolour_map=hull_recolour_map,
                    house_recolour_map=graphics_constants.house_recolour_roof_silver_1,
                    superstructure_recolour_map=hull_recolour_map,
                ),
                SpriteLayer(
                    self,
                    # pick certain pipes / hatch covers off the superstructure and recolour
                    selective_colour_protocols_hull=["NONE"],
                    selective_colour_protocols_superstructure=["CC1"],
                ),
            ],
            liveries=[
                ["_DEFAULT", "COMPANY_COLOUR_USE_WEATHERING"],
                ["COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING", "COMPANY_COLOUR_USE_WEATHERING"],
                ["FREIGHT_SILVER", "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"],
                ["FREIGHT_GREY", "FREIGHT_PEWTER"],
                ["FREIGHT_OIL_BLACK", "FREIGHT_PEWTER"],
                ["FREIGHT_MINT_GREEN", "FREIGHT_GREMLIN_GREEN"],
                ["FREIGHT_TEAL", "FREIGHT_TEAL"],
                ["FREIGHT_RUSTY_BLACK", "FREIGHT_PEWTER"],
                ["FREIGHT_BAUXITE", "FREIGHT_PEWTER"],
                ["FREIGHT_RUBY", "FREIGHT_RUBY"],
                ["FREIGHT_OCHRE", "FREIGHT_RUBY"],
                ["FREIGHT_SULPHUR", "FREIGHT_OCHRE"],
            ],
        )


class Trawler(Ship):
    """
    Dedicated to fishing
    """

    def __init__(self, **kwargs):
        self.base_id = "trawler"
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = ["FISH"]  # no need for fallbacks, single refit
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_dark_blue,
            apply_hull_recolours_to_ship=True,  # to delete, no longer used, set supestructure_recolour_map to same as hull instead
            liveries=[["_DEFAULT"]],
        )


class UtilityHovercraft(Ship):
    """
    Hovercraft for express freight
    """

    def __init__(self, **kwargs):
        self.base_id = "utility_hovercraft"
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = global_constants.default_cargos["mail"]
        # these are the mail capacities_by_subtype for ships that have MAIL as default; freight capacity will be divided by global_constants.mail_multipler
        self.capacities_by_subtype = {
            "A": 40,
            "B": 120,
            "D": 360,
        }  # no large mail ships, by design
        self._speed = 50
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleColourRemaps(
            spritelayers=[SpriteLayer(self)],
            hull_recolour_map=graphics_constants.hull_recolour_CC1,
            liveries=[["_DEFAULT"]],
        )
