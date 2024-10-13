from abc import ABC

from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.filter.operation_mapper.operation_mapper import FilterOperationTypeMapper
from src.infrastructure.serializers.json_serializer import JsonSerializer


class AbstractPrototype(ABC):
    _mapper: FilterOperationTypeMapper
    _data: list
    _serializer: JsonSerializer
    __primitives = (int, str, float, bool)
    
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
        
    def __check_item(self, data, key, value, operation) -> bool:

        properties = self.parse_fields(data)

        acceptable = False
        
        for property_iem in properties:
            if acceptable:
                break
            property_value = getattr(data, property_iem)
            
            if property_iem == key:
                acceptable = operation(property_value, value)
            else:
                acceptable = self.__check_item(property_value, key, value, operation)
                
        return acceptable
            
            
    def __check_list(self, data: list, key: str, value, operation) -> list:
        
        result = []
        
        for item in data:
            if self.__check_item(item, key, value, operation):
                result.append(item)
        
        return result
        
    def get_by_filter_item(self, data: list, filter_tem: FilterItem) -> list:
        
        operation = self._mapper.enum_to_operation(filter_tem.operation)
        
        return self.__check_list(data, filter_tem.key, filter_tem.value, operation)
        