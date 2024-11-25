from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3


class LogItem:
    __level: LogLevel
    __message: str

    def __init__(self, level: LogLevel, message: str):
        self.__level = level
        self.__message = message

    @property
    def level(self):
        return self.__level

    @property
    def message(self):
        return self.__message

    @level.setter
    def level(self, value: LogLevel):
        self.__level = value

    @message.setter
    def message(self, value: str):
        self.__message = value
