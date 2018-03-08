from roster import Roster

# ships in alphabetical order
from ships import (bulk_carrier_large,
                   bulk_carrier_small,
                   edibles_tanker_large,
                   #edibles_tanker_small,
                   flatdeck_barge_large,
                   flatdeck_barge_small,
                   fruit_veg_carrier_large,
                   livestock_carrier_large,
                   livestock_carrier_small,
                   #mail_ship_large, # no large mail ship, nonsense having so many mailbags in one vehicle
                   mail_ship_micro,
                   mail_ship_mini,
                   mail_ship_small,
                   pax_fast_loading_large,
                   pax_fast_loading_micro,
                   pax_fast_loading_mini,
                   pax_fast_loading_small,
                   pax_luxury_large,
                   pax_luxury_small,
                   piece_goods_carrier_large,
                   piece_goods_carrier_small,
                   reefer_large,
                   reefer_small,
                   #supply_vessel_large,
                   #supply_vessel_small,
                   tanker_large,
                   tanker_small,
                   trawler_small,
                   trawler_micro,
                   trawler_mini,
                   universal_freighter_large,
                   universal_freighter_micro,
                   universal_freighter_mini,
                   universal_freighter_small)


roster = Roster(id = 'default',
                numeric_id = 1,
                express_speeds = {0: 35, 1950: 45, 1980: 70},
                freighter_speeds = {0: 25, 1950: 35},
                # ships in buy menu order
                ships = [pax_fast_loading_micro,
                         pax_fast_loading_mini,
                         pax_fast_loading_small,
                         pax_fast_loading_large,
                         pax_luxury_small,
                         pax_luxury_large,
                         mail_ship_micro,
                         mail_ship_mini,
                         mail_ship_small,
                         universal_freighter_micro,
                         universal_freighter_mini,
                         universal_freighter_small,
                         universal_freighter_large,
                         piece_goods_carrier_small,
                         piece_goods_carrier_large,
                         flatdeck_barge_small,
                         flatdeck_barge_large,
                         bulk_carrier_small,
                         bulk_carrier_large,
                         tanker_small,
                         tanker_large,
                         livestock_carrier_small,
                         livestock_carrier_large,
                         edibles_tanker_large,
                         reefer_small,
                         reefer_large,
                         fruit_veg_carrier_large,
                         trawler_micro,
                         trawler_mini,
                         trawler_small
                         ])
