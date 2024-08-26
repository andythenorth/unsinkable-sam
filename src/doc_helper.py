# JFDI module to help do some doc formatting

import global_constants
import utils
import unsinkable_sam

class DocHelper(object):

    def __init__(self, lang_strings):
        self.lang_strings = lang_strings

    def get_ships_by_subclass(self, ships):
        # first find all the subclasses + their vehicles
        ships_by_subclass = {}
        for ship in ships:
            subclass = type(ship)
            if subclass in ships_by_subclass:
                ships_by_subclass[subclass].append(ship)
            else:
                ships_by_subclass[subclass] = [ship]
        # reformat to a list we can then sort so order is consistent
        result = [
            {
                "name": i.__name__,
                "doc": i.__doc__,
                "class_obj": subclass,
                "ships": ships_by_subclass[i],
            }
            for i in ships_by_subclass
        ]
        return sorted(result, key=lambda subclass: subclass["name"])

    def get_roster_name(self, index):
        return self.lang_strings.get("STR_PARAM_ROSTER_OPTION_" + str(index), "")

    def get_roster_by_id(self, roster_id, registered_rosters):
        for roster in registered_rosters:
            if roster.id == roster_id:
                return roster
        # default result
        return None

    def fetch_prop(self, result, prop_name, value):
        result["ship"][prop_name] = value
        result["subclass_props"].append(prop_name)
        return result

    def unpack_name_suffix(self, name_suffix_as_string_name):
        try:
            return self.lang_strings[name_suffix_as_string_name]
        except:
            # no good solution currently for
            # 1. names for roles that are consistent, but ship model name suffixes change (Collier vs. Mini Bulker)
            # 2. no ship in scope
            # probably need a separate set of strings for the role?  Parent types?
            utils.echo_message(
                "Can't return name suffix for " + name_suffix_as_string_name
            )
            return "CABBAGE"

    def unpack_name_string(self, ship):
        return (
            ship._name + " " + self.unpack_name_suffix(ship.name_suffix_as_string_name)
        )

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for ship in subclass["ships"]:
            result = {"ship": {}, "subclass_props": []}

            result = self.fetch_prop(result, "Ship Name", self.unpack_name_string(ship))
            result = self.fetch_prop(result, "Subtype", ship.subtype)
            result = self.fetch_prop(
                result, "Extra Info", self.lang_strings[ship.get_str_type_info()]
            )
            result = self.fetch_prop(result, "Speed Laden", int(ship.speed))
            result = self.fetch_prop(result, "Intro Date", ship.intro_date)
            result = self.fetch_prop(result, "Vehicle Life", ship.vehicle_life)
            result = self.fetch_prop(result, "Capacity", ship.default_capacity)
            result = self.fetch_prop(result, "Buy Cost", ship.buy_cost)
            result = self.fetch_prop(result, "Running Cost", ship.running_cost)
            result = self.fetch_prop(result, "Loading Speed", ship.loading_speed)

            props_to_print[ship] = result["ship"]
            props_to_print[subclass["name"]] = result["subclass_props"]

        return props_to_print

    def get_base_numeric_id(self, vehicle):
        return vehicle.numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]

    def ships_as_tech_tree(self, ships):
        # !! does not handle roster at time of writing
        # structure
        #    |- role_group
        #       |- base_id (role)
        #          |- generation
        #             |- ship
        # if there's no ship matching a combination of keys in the tree, there will be a None entry for that node in the tree, to ease walking the tree
        result = {}
        # much nested loops
        for role_group in global_constants.role_group_mapping:
            role_branches = {}
            for role in global_constants.role_group_mapping[role_group]:
                role_branches[role] = {}
                # hard-coded for now, move to global constants another day
                for subtype in ["A", "B", "C", "D", "E", "F"]:
                    subtype_branch = {}
                    # walk the generations, providing default None objects
                    for gen in range(
                        1,
                        len(
                            self.get_roster_by_id(
                                "default", unsinkable_sam.registered_rosters
                            ).intro_dates["DEFAULT"]
                        )
                        + 1,
                    ):
                        subtype_branch[gen] = None
                    # get the ships matching this role
                    for ship in ships:
                        if ship.base_id == role and ship.subtype == subtype:
                            subtype_branch[ship.gen] = ship
                    # to prevent empty rows in tech tree, only include the subtype_branch if it contains actual ships
                    if set(subtype_branch.values()) != {None}:
                        role_branches[role][subtype] = subtype_branch
            result[role_group] = role_branches
        return result
