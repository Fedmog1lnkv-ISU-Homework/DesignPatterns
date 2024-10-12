from src.core.enums.filter_operation_type import FilterOperationType
from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class FilterItem(AbstractEntity):
    __key: str = None
    __value: str = None
    __operation: FilterOperationType = None
    
    @property
    def key(self):
        return self.__key
    
    @key.setter
    def key(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        
        self.__key = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value: FilterOperationType):
        self.__operation = value

    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code
    