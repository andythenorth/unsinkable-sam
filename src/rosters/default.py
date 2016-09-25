from roster import Roster

# ships in alphabetical order
from ships import (universal_freighter_large,
                   universal_freighter_micro,
                   universal_freighter_mini,
                   universal_freighter_small,
                   tanker_large,
                   tanker_small)


roster = Roster(id = 'default',
                numeric_id = 1,
                # ships in buy menu order
                ships = [universal_freighter_micro,
                         universal_freighter_mini,
                         universal_freighter_small,
                         universal_freighter_large,
                         tanker_small,
                         tanker_large])
