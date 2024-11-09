from src.core.enums.event_type import EventType


class Event:
    __type: EventType
    __data = None
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value: EventType):
        self.__type = value
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value