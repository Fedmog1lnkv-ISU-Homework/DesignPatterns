import datetime

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class GetOsvDTO(AbstractEntity):
    __start_date: datetime.datetime
    __end_date: datetime.datetime
    __storehouse_id: str = None

    @property
    def start_date(self) -> datetime.datetime:
        return self.__start_date

    @start_date.setter
    def start_date(self, value: datetime.datetime):
        if not isinstance(value, datetime.datetime):
            raise TypeValidationException(value, datetime.datetime)
        self.__start_date = value

    @property
    def end_date(self) -> datetime.datetime:
        return self.__end_date

    @end_date.setter
    def end_date(self, value: datetime.datetime):
        if not isinstance(value, datetime.datetime):
            raise TypeValidationException(value, datetime.datetime)
        self.__end_date = value

    @property
    def storehouse_id(self) -> str:
        return self.__storehouse_id

    @storehouse_id.setter
    def storehouse_id(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__storehouse_id = value

    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code
