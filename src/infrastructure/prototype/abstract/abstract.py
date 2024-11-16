from abc import ABC

from src.infrastructure.factory.type_caster import TypeCaster
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.filter.operation_mapper.operation_mapper import FilterOperationTypeMapper
from src.infrastructure.serializers.json_serializer import JsonSerializer


class AbstractPrototype(ABC):
    _mapper: FilterOperationTypeMapper
    _data: list
    _serializer: JsonSerializer
    __primitives = (int, str, float, bool)
    _type_caster = TypeCaster()
    
    def create(self, filters: list[FilterItem]) -> list:
        result = self._data
        
        for filter_item in filters:
            result = self.get_by_filter_item(result, filter_item)
        
        return result
    
    def __init__(self, data: list, mapper: FilterOperationTypeMapper):
        
        self._mapper = mapper
        self._data = data
        self._serializer = JsonSerializer()

    def parse_fields(self, obj):
        if isinstance(obj, self.__primitives):
            return []
        if obj is None:
            return []
        return list(filter(lambda x: not x.startswith("_") and not callable(getattr(obj.__class__, x)), dir(obj)))
    
    def __check_list_item(self, data: list, key, value, operation) -> bool:

        if len(data) == 0:
            return False
        properties = self.parse_fields(data[0])

        acceptable = False

        current_key, new_key = self.__split_key(key)
        
        for item in data:
            for property_iem in properties:
                if acceptable:
                    break
                property_value = getattr(item, property_iem)
    
                if property_iem == current_key:
                    if new_key is not None:
                        return self.__check_item(property_value, new_key, value, operation)
    
                    if isinstance(property_value, list):
                        for item in property_value:
                            acceptable = self.__check_item(item, key, value, operation)
                            if acceptable:
                                break
                    else:
                        casted_value = self._type_caster.cast_to_type(value, type(property_value))
                        acceptable = operation(property_value, casted_value)
    
                elif isinstance(property_value, type(item)): #recurcive
                    acceptable = self.__check_item(property_value, key, value, operation)

        return acceptable    
    
    def __check_item(self, data, key, value, operation) -> bool:
        
        if isinstance(data, list):
            return self.__check_list_item(data, key, value, operation)

        properties = self.parse_fields(data)

        acceptable = False
        
        current_key, new_key = self.__split_key(key)
        
        for property_iem in properties:
            if acceptable:
                break
            property_value = getattr(data, property_iem)
            
            if property_iem == current_key:
                if new_key is not None:
                    return self.__check_item(property_value, new_key, value, operation)
                
                if isinstance(property_value, list):
                    for item in property_value:
                        acceptable = self.__check_item(item, key, value, operation)
                        if acceptable:
                            break
                else:
                    casted_value = self._type_caster.cast_to_type(value, type(property_value))    
                    acceptable = operation(property_value, casted_value)
                
            elif isinstance(property_value, type(data)): #recurcive
                acceptable = self.__check_item(property_value, key, value, operation)
                
        return acceptable
            
    def __split_key(self, key: str):
        keys = key.split(".")
        if len(keys) == 0:
            return "", ""
        if len(keys) > 1:
            return keys[0], ".".join(keys[1:])
        
        return keys[0], None 
            
    def __check_list(self, data: list, key: str, value, operation) -> list:
        
        result = []
        
        for item in data:
            if self.__check_item(item, key, value, operation):
                result.append(item)
        
        return result
        
    def get_by_filter_item(self, data: list, filter_tem: FilterItem) -> list:
        
        operation = self._mapper.enum_to_operation(filter_tem.operation)
        
        return self.__check_list(data, filter_tem.key, filter_tem.value, operation)
        