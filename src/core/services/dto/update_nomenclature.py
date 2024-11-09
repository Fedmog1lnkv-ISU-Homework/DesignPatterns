from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class UpdateNomenclatureDTO(AbstractEntity):
    __id: str
    __name: str = None
    __nomenclature_group_id: str = None
    __unit_id: str = None
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__name = value

    @property
    def nomenclature_group_id(self) -> str:
        return self.__nomenclature_group_id

    @nomenclature_group_id.setter
    def nomenclature_group_id(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__nomenclature_group_id = value

    @property
    def unit_id(self) -> str:
        return self.__unit_id

    @unit_id.setter
    def unit_id(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__unit_id = value

    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code