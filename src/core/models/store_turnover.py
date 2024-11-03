from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.storehouse_model import StoreHouseModel
from src.core.models.unit_model import UnitModel


class StoreTurnover(AbstractEntity):
    
    __nomenclature: Nomenclature = None
    __store_house: StoreHouseModel = None
    __measurement_unit: UnitModel = None
    __amount: float = 0.0
    
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
        return self.__store_house
    
    @storehouse.setter
    def storehouse(self, value: StoreHouseModel):
        if not isinstance(value, StoreHouseModel):
            raise TypeValidationException(value, StoreHouseModel)
        
        self.__store_house = value
        
    @property
    def unit(self) -> UnitModel:
        return self.__measurement_unit
    
    @unit.setter
    def unit(self, value: UnitModel):
        if not isinstance(value, UnitModel):
            raise TypeValidationException(value, UnitModel)
        
        self.__measurement_unit = value
        
    @property
    def amount(self) -> float :
        return self.__amount
    
    @amount.setter
    def amount(self, value: float):
        if not isinstance(value, float):
            raise TypeValidationException(value, float)
        
        self.__amount = value

    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code
    
    