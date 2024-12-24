from enum import StrEnum


class HTMXRequestHeader(StrEnum):
    REQUEST = 'HX-Request'
    BOOSTED = 'HX-Boosted'
    CURRENT_URL = 'HX-Current-URL'
    TARGET = 'HX-Target'
    TRIGGER = 'HX-Trigger'


class HTMXResponseHeader(StrEnum):
    PUSH_URL = ''
    REPLACE_URL = ''
    RESWAP = 'HX_Reswap'
    RETARGET = 'HX-Retarget'
    TRIGGER = 'HX-Trigger'