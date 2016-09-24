from roster import Roster

# ships in alphabetical order
from ships import (gcv_large,
                   gcv_micro,
                   gcv_mini,
                   gcv_small,
                   tanker_large,
                   tanker_small)


roster = Roster(id = 'default',
                numeric_id = 1,
                # ships in buy menu order
                ships = [gcv_micro,
                         gcv_mini,
                         gcv_small,
                         gcv_large,
                         tanker_small,
                         tanker_large])
