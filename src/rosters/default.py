from roster import Roster

# ships in alphabetical order
from ships import (bulk_carrier_large,
                   bulk_carrier_small,
                   piece_goods_carrier_large,
                   piece_goods_carrier_small,
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
                # ships in buy menu order
                ships = [universal_freighter_micro,
                         universal_freighter_mini,
                         universal_freighter_small,
                         universal_freighter_large,
                         piece_goods_carrier_small,
                         piece_goods_carrier_large,
                         bulk_carrier_small,
                         bulk_carrier_large,
                         tanker_small,
                         tanker_large,
                         trawler_micro,
                         trawler_mini,
                         trawler_small])
