from enum import Enum


class FilterOperationType(Enum):
    EQUAL = 0
    LIKE = 1
    BETWEEN = 2

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]
