import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import global_constants # expose all constants for easy passing to templates
import utils
from graphics_processor.visible_cargo import VisibleCargo, VisibleCargoLiveryOnly
import graphics_processor.utils as graphics_utils
from rosters import registered_rosters
from hulls import registered_hulls

class Ship(object):
    """Base class for all types of ships"""
    def __init__(self, id, **kwargs):
        self.id = id

        # setup properties for this ship
        self.title = kwargs.get('title', None)
        self.numeric_id = kwargs.get('numeric_id', None)
        self.str_type_info = 'EMPTY'
        self.intro_date = kwargs.get('intro_date', None)
        self.vehicle_life = kwargs.get('vehicle_life', 100) # default 100 years, assumes 2 generations of ships 1850-2050
        self.buy_cost = kwargs.get('buy_cost', None)
        self.fixed_run_cost_factor = kwargs.get('fixed_run_cost_factor', None)
        self.fuel_run_cost_factor = kwargs.get('fuel_run_cost_factor', None)
        self.loading_speed_multiplier = 1 # over-ride in subclass as needed (suggested values are 0.5 for slower loading and 2 for faster loading)
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self._speed = kwargs.get('speed', None)
        # by default ships have multiple capacity options, refittable in depot
        self.capacity_is_refittable_by_cargo_subtype = kwargs.get('capacity_is_refittable_by_cargo_subtype', True)
        # most ships use steam effect_spawn_model so set default, over-ride in ships as needed
        self.effect_spawn_model = kwargs.get('effect_spawn_model', 'EFFECT_SPAWN_MODEL_STEAM')
        self.effects = kwargs.get('effects', [])
        # create a structure to hold model variants
        self.model_variants = []
        # base hull (defines length, wake graphics, hull graphics if composited etc)
        self.hull = registered_hulls.get(kwargs.get('hull', None), None)
        # cargo /livery graphics options
        self.visible_cargo = VisibleCargo()
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        self.roster_id = None

    def add_model_variant(self, intro_date, end_date, spritesheet_suffix, graphics_processor=None):
        self.model_variants.append(ModelVariant(intro_date, end_date, spritesheet_suffix, graphics_processor))

    def get_reduced_set_of_variant_dates(self):
        # find all the unique dates that will need a switch constructing
        years = set()
        for variant in self.model_variants:
            years.update((variant.intro_date, variant.end_date))
        years = sorted(years)
        # quick integrity check
        if years[0] != 0:
            utils.echo_message(self.id + " doesn't have at least one model variant with intro date 0 (required for nml switches to work)")
        return years

    def get_variants_available_for_specific_year(self, year):
        # put the data in a format that's easy to render as switches
        result = []
        for variant in self.model_variants:
            if variant.intro_date <= year < variant.end_date:
                result.append(variant.spritesheet_suffix)
        return result # could call set() here, but I didn't bother, shouldn't be needed if model variants set up correctly

    def get_nml_random_switch_fragments_for_model_variants(self):
        # return fragments of nml for use in switches
        result = []
        years = self.get_reduced_set_of_variant_dates()
        for index, year in enumerate(years):
            if index < len(years) - 1:
                from_date = year
                until_date = years[index + 1] - 1
                result.append(str(from_date) + '..' + str(until_date) + ':' + self.id + '_switch_graphics_random_' + str(from_date))
        return result

    @property
    def num_unique_spritesheet_suffixes(self):
        return len(set([i.spritesheet_suffix for i in self.model_variants]))

    @property
    def speed(self):
        # speed determined automatically by intro date, or can be over-ridden per vehicle with _speed in constructor kwargs
        if self._speed is None:
            if self.default_cargo == 'PASS' or self.default_cargo == 'MAIL':
                speeds = self.get_roster(self.roster_id).express_speeds
            else:
                speeds = self.get_roster(self.roster_id).freighter_speeds
            speed = speeds[max([year for year in speeds if self.intro_date >= year])]
        else:
            speed = self._speed
        return speed

    def get_speed_adjusted_for_param(self, speed_index):
        # there is a speed adjustment parameter, use that to look up a speed factor
        speed_factors = [0.67, 1, 1.33]
         # allow that integer maths is needed for newgrf cb results; rounding up for safety, capped at max ship speed
        result = int(min(math.ceil(3.2 * self.speed * speed_factors[speed_index]), 79 * 3.2))
        print(result)
        return result

    @property
    def adjusted_model_life(self):
        return 'VEHICLE_NEVER_EXPIRES'

    @property
    def running_cost(self):
        # calculate a running cost
        gross_tonnage = self.default_cargo_capacity * 1.25 # no real need to vary this by ship type
        fixed_run_cost = self.fixed_run_cost_factor * global_constants.FIXED_RUN_COST
        fuel_run_cost =  self.fuel_run_cost_factor * gross_tonnage * global_constants.FUEL_RUN_COST
        calculated_run_cost = int((fixed_run_cost + fuel_run_cost) / 98) # divide by magic constant to get costs as factor in 0-255 range
        return min(calculated_run_cost, 255) # cost factor is a byte, can't exceed 255

    @property
    def refittable_capacity_factors(self):
        # default refittable capacities are [base capacity, 25% underload, 25% overload]
        # over-ride this in the subclass if necessary
        return [1, 0.75, 1.25]

    @property
    def capacities_refittable(self):
        capacities_pax = [int(self.capacity_pax * capacity_factor) for capacity_factor in self.refittable_capacity_factors]
        capacities_mail = [int(self.capacity_mail * capacity_factor) for capacity_factor in self.refittable_capacity_factors]
        capacities_freight = [int(self.capacity_freight * capacity_factor) for capacity_factor in self.refittable_capacity_factors]
        result = {'pax': capacities_pax, 'mail': capacities_mail, 'freight': capacities_freight}
        return(result)

    @property
    def capacity_pax(self):
        # currently contains no provision for custom widths
        # but if needed, add _capacity_pax from constructor kwargs, and check existence of that here
        capacities = {'micro': 40, 'mini': 125, 'small': 300, 'large': 720}
        return capacities[self.hull.size_class]

    @property
    def capacity_mail(self):
        # currently contains no provision for custom widths
        # but if needed, add _capacity_mail from constructor kwargs, and check existence of that here
        capacities = {'micro': 40, 'mini': 125, 'small': 300, 'large': 720}
        return capacities[self.hull.size_class]

    @property
    def capacity_freight(self):
        # currently contains no provision for custom widths
        # but if needed, add _capacity_freight from constructor kwargs, and check existence of that here
        capacities = {'micro': 40, 'mini': 100, 'small': 240, 'large': 576}
        return capacities[self.hull.size_class]

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [cargo_classes.append(cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes)) # use set() here to dedupe

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ','.join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ','.join(self.label_refits_disallowed)

    @property
    def loading_speed(self):
        # loading speed is *not* normalised per capacity for ships, unlike vehicles in Road Hog / Iron Horse
        # 10 is default OTTD value for ships, seems fine to me
        return 10 * self.loading_speed_multiplier

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        return self.title.split('[')[0]

    def get_str_name_suffix(self):
        # used in ship name string only, relies on name property value being in format "Foo [Bar]" for Name [Type Suffix]
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return 'STR_NAME_SUFFIX_' + type_suffix

    def get_str_type_info(self):
        # makes a string id for nml
        return 'STR_' + self.str_type_info

    def get_name(self):
        return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def get_buy_menu_string(self):
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_EMPTY))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info())

    def get_roster(self, roster_id):
        for roster in registered_rosters:
            if roster_id == roster.id:
                return roster

    def get_expression_for_rosters(self):
        # the working definition is one and only one roster per vehicle
        roster = self.get_roster(self.roster_id)
        return 'param[2]==' + str(roster.numeric_id - 1)

    def get_spriterow_counts(self):
        # !! overly nested as assumes that there would be multiple units, doesn't apply to ships
        result = []
        unit_rows = []
        # assumes visible_cargo is used to handle any other rows, no other cases at time of writing, could be changed eh?
        unit_rows.extend(self.visible_cargo.get_output_row_counts_by_type())
        result.append(unit_rows)
        return result

    @property
    def graphics_processors(self):
        # wrapper to get the graphics processors
        template = self.id + '_template.png'
        return graphics_utils.get_composited_cargo_processors(template = template)

    @property
    def buy_menu_width(self):
        # currently contains no provision for custom widths
        # but if needed, add _buy_menu_width from constructor kwargs, and check existence of that here
        # standard sizes are multiples of 32, except first size, where 32 is just too small to make a nice sprite
        widths = {'micro': 40, 'mini': 64, 'small': 96, 'large': 128}
        return widths[self.hull.size_class]

    @property
    def buy_menu_bb_xy(self):
        # !! deprecated, isn't needed when using rebuilt spritesheets/spriteset templates
        # this is a bit janky as it was added when migrating to standard size_class stuff
        # might need cleaning up in future, or eh, maybe not also
        bb_y = 34 if self.hull.size_class == 'large' else 36
        return [620, bb_y]

    @property
    def buy_menu_bb_y_offset(self):
        # !! scaffolding for variable height ships that need offsets on their bounding box for buy menu
        # !! returns a fixed value currently, more wasn't needed yet :P Possibly delete?
        return 16

    @property
    def offsets(self):
        # currently contains no provision for custom offsets
        # but if needed, add _offsets from constructor kwargs, and check existence of that here
        # !! this will need extending to provide offsets per size_class
        offsets = {'large': [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]],
                   'small': [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]],
                   'mini':  [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]],
                   'micro': [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]]}
        return offsets[self.hull.size_class]

    @property
    def vehicle_nml_template(self):
        if self.visible_cargo.nml_template:
            return self.visible_cargo.nml_template
        # default case
        return 'ship.pynml'

    def get_nml_expression_for_cargo_variant_random_switch(self, variation_num, cargo_id=None):
        switch_id = self.id + "_switch_graphics_" + str(variation_num) + ('_' + str(cargo_id) if cargo_id is not None else '')
        return "SELF," + switch_id + ", bitmask(TRIGGER_VEHICLE_ANY_LOAD)"

    def get_expression_for_effects(self):
        # provides part of nml switch for effects (smoke), or none if no effects defined
        if len(self.effects) > 0:
            result = []
            for index, effect in enumerate(self.effects):
                 result.append('STORE_TEMP(create_effect(' + effect + '), 0x10' + str(index) + ')')
            return '[' + ','.join(result) + ']'
        else:
            return 0

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: ship " + self.id + " references cargo label " + i + " which is not defined in the cargo table")

    def render(self):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        # templating
        template_name = self.vehicle_nml_template
        template = templates[template_name]
        nml_result = template(ship=self, global_constants=global_constants)
        return nml_result


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per ship
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, intro_date, end_date, spritesheet_suffix, graphics_processor):
        self.intro_date = intro_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames
        self.graphics_processor = graphics_processor

    def get_spritesheet_name(self, ship):
        return ship.id + '_' + str(self.spritesheet_suffix) + '.png'


class CourierShip(Ship):
    """
    A relatively fast vessel type for mail, and express freight.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['mail','express_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = ['TOUR']
        self.capacity_cargo_holds = kwargs.get('capacity_cargo_holds', 0)
        self.default_cargo = 'MAIL'
        self.default_cargo_capacity = self.capacity_mail


class PaxFastLoadingShip(Ship):
    """
    Fast-loading passenger vessel - better suited to short routes; keep same speed as luxury pax ship for balancing reasons.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'PASS'
        self.default_cargo_capacity = self.capacity_pax
        self.loading_speed_multiplier = 3


class PaxLuxuryShip(Ship):
    """
    Luxury passenger vessel - better suited to long routes; keep same speed as fast-loading pax ship for balancing reasons.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'PASS'
        self.default_cargo_capacity = self.capacity_pax
        self.cargo_age_period = 3 * global_constants.CARGO_AGE_PERIOD


class UniversalFreighter(Ship):
    """
    General purpose freight vessel type. No pax or mail cargos, refits any other cargo including liquids (in barrels or containers).
    IRL: "multi-purpose vessel".
    Not "general cargo vessel", IRL they carry only piece goods (confusing much?).
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'general_cargo_vessel.pynml'
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = [] # no specific labels needed, refits all freight
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'COAL'
        self.default_cargo_capacity = self.capacity_freight
        # Cargo Graphics
        self.visible_cargo.bulk = True
        self.visible_cargo.piece = True
        self.cargo_length = 3 # !! temp hax to make graphics compile work


class PieceGoodsCarrier(Ship):
    """
    Piece goods cargos, other selected cargos.  Equivalent of Road Hog box hauler and Iron Horse box wagon.
    IRL: "GCV", "Break-bulk", "Pallet carrier".
    Not "box ship" because IRL they are container carriers (yair).
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = 'general_cargo_vessel.pynml'
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR'] # Iron Horse compatibility
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'GOOD'
        self.default_cargo_capacity = self.capacity_freight


class FlatDeckBarge(Ship):
    """
    Flat deck, no holds - refits most cargos, not bulk.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = 'general_cargo_vessel.pynml'
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'STEL'
        self.default_cargo_capacity = self.capacity_freight


class BulkCarrier(Ship):
    """
    Limited set of bulk (mineral) cargos.  Equivalent of Road Hog dump hauler and Iron Horse hopper wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = 'general_cargo_vessel.pynml'
        self.class_refit_groups = ['dump_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_dump_bulk']
        self.default_cargo = 'COAL'
        self.default_cargo_capacity = self.capacity_freight
        self.loading_speed_multiplier = 2
        # Cargo Graphics
        self.visible_cargo.bulk = True


class UtilityVessel(Ship):
    """
    Refits everything.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['pax_mail','all_freight']
        self.label_refits_allowed = [] # no specific labels needed, GCV refits all cargo
        self.label_refits_disallowed = []
        self.default_cargo = 'PASS'
        self.default_cargo_capacity = self.capacity_pax

    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_UTILITY,${capacity_mail},${capacity_cargo_holds}))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info(), capacity_pax=self.capacity_pax,
                                            capacity_mail=self.capacity_mail, capacity_cargo_holds=self.capacity_cargo_holds)


class LivestockCarrier(Ship):
    """
    Special type for livestock (as you might guess).
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['empty']
        self.label_refits_allowed = ['LVST'] # set to livestock by default, don't need to make it refit
        self.label_refits_disallowed = []
        self.default_cargo = 'LVST'
        self.default_cargo_capacity = self.capacity_freight
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD # improved decay rate


class LogTug(Ship):
    """
    Specialist type for hauling logs only, has some specialist refit and speed behaviours.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'log_tug.pynml'
        self.class_refit_groups = ['empty']
        self.label_refits_allowed = ['WOOD']
        self.label_refits_disallowed = []
        self.default_cargo = 'WOOD'
        self.default_cargo_capacity = self.capacity_freight


class Trawler(Ship):
    """
    Dedicated to fishing
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'FISH'
        self.default_cargo_capacity = self.capacity_freight


class Tanker(Ship):
    """
    Ronseal ("does what it says on the tin", for those without extensive knowledge of UK advertising).
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'vehicle_with_visible_cargo.pynml'
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = [] # refits most cargos that have liquid class even if they might be edibles
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['edible_liquids'] # don't allow known edible liquids
        self.default_cargo = 'OIL_'
        self.default_cargo_capacity = self.capacity_freight
        # Cargo graphics
        self.visible_cargo = VisibleCargoLiveryOnly()
        self.visible_cargo.tanker = True


class EdiblesTanker(Ship):
    """
    Gallons and gallons and gallons of wine, milk or water.  Except in metric systems, where it's litres.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'ship.pynml'
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = [] # refits most cargos that have liquid class even if they might be inedibles
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_edible_liquids'] # don't allow known inedibles
        self.default_cargo = 'WATR'
        self.default_cargo_capacity = self.capacity_freight


class Reefer(Ship):
    """
    Refits to limited range of refrigerated cargos, with 'improved' cargo decay rate.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'general_cargo_vessel.pynml'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = [] # no specific labels needed, refits all cargos that have refrigerated class
        self.label_refits_disallowed = []
        self.default_cargo = 'GOOD'
        self.default_cargo_capacity = self.capacity_freight
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD # improved decay rate


class ContainerCarrier(Ship):
    """
    Refits to limited range of freight cargos, shows container graphics according to load state.
    """
    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self.template = 'container_carrier.pynml'
        # maintain other sets (e.g. IH etc) when changing container refits
        self.class_refit_groups = ['express_freight','packaged_freight']
        self.label_refits_allowed = ['FRUT','WATR']
        self.label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD']
        self.default_cargo = 'GOOD'
        self.default_cargo_capacity = self.capacity_freight
