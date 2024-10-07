from enum import Enum


class ReportFormat(Enum):
    CSV = 1
    MARKDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]
