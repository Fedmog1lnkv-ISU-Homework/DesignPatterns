from datetime import datetime

from yaml import FlowSequenceEndToken

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.enums.trsndsction_type import TransactionType
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.storehouse_model import StoreHouseModel
from src.core.models.unit_model import UnitModel


class StoreTransaction(AbstractEntity):
    __storehouse: StoreHouseModel = None
    __nomenclature: Nomenclature = None
    __count: float = 0.0
    __type: TransactionType = None
    __measure_unit: UnitModel = None
    __date: datetime = None
    
    @property
    def storehouse(self):
        return self.__storehouse
    
    @property
    def nomenclature(self):
        return self.__nomenclature
    
    @property
    def count(self):
        return self.__count
    
    @property
    def type(self):
        return self.__type
    
    @property
    def measure_unit(self):
        return self.__measure_unit
    
    @property
    def date(self):
        return self.__date
    
    @storehouse.setter
    def storehouse(self, value: StoreHouseModel):
        if not isinstance(value, StoreHouseModel):
            raise TypeValidationException(value, StoreHouseModel)
        self.__storehouse = value
        
    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise TypeValidationException(value, Nomenclature)
        self.__nomenclature = value
        
    @count.setter
    def count(self, value: float):
        if not isinstance(value, float):
            raise TypeValidationException(value, float)
        self.__count = value
        
    @type.setter
    def type(self, value: TransactionType):
        if not isinstance(value, TransactionType):
            raise TypeValidationException(value, TransactionType)
        self.__type = value
        
    @measure_unit.setter
    def measure_unit(self, value: UnitModel):
        if not isinstance(value, UnitModel):
            raise TypeValidationException(value, UnitModel)
        self.__measure_unit = value
        
    @date.setter
    def date(self, value: datetime):
        if not isinstance(value, datetime):
            raise TypeValidationException(value, datetime)
        self.__date = value

    def set_compare_mode(self, other) -> bool:
        return super().set_compare_mode(other)