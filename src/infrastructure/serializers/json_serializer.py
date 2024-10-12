import json

from src.infrastructure.serializers.abstractions.abstract_serializer import AbstractSerializer


class JsonSerializer(AbstractSerializer):
    def serialize(self, obj):
        if not obj:
            return ""

        data = self.get_properties(obj)
        return json.dumps(data, indent=4, sort_keys=True, default=str, ensure_ascii=False)

    def serialize_to_dict(self, obj):
        return self.get_properties(obj)
    
    def deserialize(self, data: str, obj_type: type):
        if isinstance(data, list):
            return [self.from_dict(item, obj_type) for item in data]
            
        json_data = json.loads(data.encode('utf-8'))

        if isinstance(json_data, list):
            return [self.from_dict(i, obj_type) for i in json_data]
        return self.from_dict(json_data, obj_type)

    def deserialize_from_dict(self, data: dict, obj_type: type):
        if isinstance(data, list):
            return [self.from_dict(i, obj_type) for i in data]
        
        return self.from_dict(data, obj_type)