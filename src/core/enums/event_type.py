from enum import Enum


class EventType(Enum):
    CHANGE_NOMENCLATURE = 1
    DUMP_DATA = 2
    HTTP_REQUEST_GOT = 3

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]