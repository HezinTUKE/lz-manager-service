from enum import Enum


class LZTypes(str, Enum):
    DISTRICT = "DISTRICT"
    VILLAGE = "VILLAGE"
    CITY = "CITY"
    STREET = "STREET"


class LZAddressTypes(str, Enum):
    VILLAGE = "VILLAGE"
    CITY = "CITY"
