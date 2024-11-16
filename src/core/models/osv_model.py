import datetime

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.storehouse_model import StoreHouseModel


class OsvModel(AbstractEntity):
    __start_date: datetime.datetime
    __end_date: datetime.datetime

    __start_amount: float
    __end_amount: float

    __nomenclature: Nomenclature
    __storehouse: StoreHouseModel

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
    def start_amount(self) -> float:
        return self.__start_amount

    @start_amount.setter
    def start_amount(self, value: float):
        if not isinstance(value, float):
            raise TypeValidationException(value, float)
        self.__start_amount = value

    @property
    def end_amount(self) -> float:
        return self.__end_amount

    @end_amount.setter
    def end_amount(self, value: float):
        if not isinstance(value, float):
            raise TypeValidationException(value, float)
        self.__end_amount = value

    @property
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise TypeValidationException(value, Nomenclature)
        self.__nomenclature = value

    @property
    def storehouse(self) -> StoreHouseModel:
        return self.__storehouse

    @storehouse.setter
    def storehouse(self, value: StoreHouseModel):
        if not isinstance(value, StoreHouseModel):
            raise TypeValidationException(value, StoreHouseModel)
        self.__storehouse = value

    def set_compare_mode(self, other_object) -> bool:
        return super().set_compare_mode(other_object)