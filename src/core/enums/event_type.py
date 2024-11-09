from enum import Enum


class EventType(Enum):
    CHANGE_NOMENCLATURE = 1

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]