from datetime import datetime

from src.core.abstractions.abstract_entity import AbstractEntity


class UpdateDateBlockDTO(AbstractEntity):

    __value: datetime = None

    @property
    def value(self) -> datetime:
        return self.__value

    @value.setter
    def value(self, value: datetime):
        self.__value = value

    def set_compare_mode(self, other_object) -> bool:
         return self.__unique_code == other_object.__unique_code