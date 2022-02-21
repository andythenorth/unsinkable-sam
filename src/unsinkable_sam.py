#!/usr/bin/env python

import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

from hulls import registered_hulls

from rosters import registered_rosters
from rosters import default

from vehicles import numeric_id_defender

# ship_types in alphabetical order
from vehicles import (
    bulk_ships,
    bulk_barges,
    cargo_liners,
    cryo_tankers,
    edibles_tankers,
    freighter_barges,
    freighter_ships,
    livestock_carriers,
    mail_ships,
    pax_fast_loading_ships,
    pax_luxury_ships,
    reefers,
    tanker_barges,
    tanker_ships,
    trawlers,
    utility_hovercraft,
)


def get_ships_in_buy_menu_order():
    ships = []
    # first compose the buy menu order list
    buy_menu_sort_order = []
    if makefile_args.get("roster", "ALL") == "ALL":
        active_rosters = [roster.id for roster in registered_rosters]
    else:
        active_rosters = [makefile_args["roster"]]  # make sure it's iterable
    for roster in registered_rosters:
        if roster.id in active_rosters:
            buy_menu_sort_order.extend(roster.buy_menu_sort_order)
            ships.extend(roster.ships_in_buy_menu_order)

    # now guard against any ships missing from buy menu order or vice versa, as that wastes time asking 'wtf?' when they don't appear in game
    ship_id_defender = set([ship.id for ship in ships])
    buy_menu_defender = set(buy_menu_sort_order)
    for id in buy_menu_defender.difference(ship_id_defender):
        utils.echo_message(
            "Warning: ship "
            + id
            + " in buy_menu_sort_order, but not found in registered ships"
        )
    for id in ship_id_defender.difference(buy_menu_defender):
        utils.echo_message(
            "Warning: ship "
            + id
            + " in ships, but not in buy_menu_sort_order - won't show in game"
        )
    # rarely triggered guard against unused hulls being defined - just a tidy-minds issue
    used_hulls = set([ship.hull for ship in ships])
    for hull in registered_hulls.values():
        if hull not in used_hulls:
            utils.echo_message("Hull " + str(hull) + " is defined but unused")
    return ships


def vacant_numeric_ids_formatted():
    # when adding vehicles it's useful to know what the next free numeric ID is
    # tidy-mind problem, but do we have any vacant numeric ID slots in the currently used range?
    max_id = max(numeric_id_defender)
    id_gaps = []
    for id in range(0, max_id):
        if id not in numeric_id_defender:
            id_gaps.append(str(id))
    return (
        "Vacant numeric ID slots: "
        + ", ".join(id_gaps)
        + (" and from " if len(id_gaps) > 0 else "")
        + str(max_id + 1)
        + " onwards"
    )


def main():
    # rosters
    default.main(disabled=False)

    # ship_types (in alphabetical order)
    bulk_ships.main()
    # bulk_barges.main() # barges need refactored to be riverboats / push barges
    cargo_liners.main()
    # cryo_tankers.main()
    edibles_tankers.main()
    # freighter_barges.main()
    freighter_ships.main()
    # livestock_carriers.main()
    # mail_ships.main()
    # pax_fast_loading_ships.main()
    # pax_luxury_ships.main()
    reefers.main()
    # tanker_barges.main()
    tanker_ships.main()
    # trawlers.main()
    # utility_hovercraft.main()
