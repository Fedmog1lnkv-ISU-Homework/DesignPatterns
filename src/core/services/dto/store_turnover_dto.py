from datetime import datetime

from src.core.abstractions.abstract_entity import AbstractEntity
from src.infrastructure.filter.item.item import FilterItem


class StoreTurnoverDTO(AbstractEntity):
    
    __filters: list[FilterItem] = None
    __start_time: datetime = None
    __end_time: datetime = None
    
    @property
    def filters(self) -> list[FilterItem]:
        return self.__filters
    
    @property
    def start_time(self) -> datetime:
        return self.__start_time
    
    @property
    def end_time(self) -> datetime:
        return self.__end_time
    
    @filters.setter
    def filters(self, value: list[FilterItem]):
        self.__filters = value
    
    @start_time.setter
    def start_time(self, value: datetime):
        self.__start_time = value
    
    @end_time.setter
    def end_time(self, value: datetime):
        self.__end_time = value

    def set_compare_mode(self, other_object) -> bool:
         return self.__unique_code == other_object.__unique_code