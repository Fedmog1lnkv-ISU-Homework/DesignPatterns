from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.infrastructure.filter.item.item import FilterItem


class FilterItemFactory:
    __json_serializer: JsonSerializer
    
    def __init__(self):
        self.__json_serializer = JsonSerializer()
        
    def from_json(self, data: dict):
        return self.__json_serializer.deserialize_from_dict(data, FilterItem)
        