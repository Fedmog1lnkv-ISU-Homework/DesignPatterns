import json

from src.infrastructure.serializers.abstractions.abstract_serializer import AbstractSerializer


class JsonSerializer(AbstractSerializer):
    def serialize(self, obj):
        if not obj:
            return ""

        data = self.get_properties(obj)
        return json.dumps(data, indent=4, sort_keys=True, default=str, ensure_ascii=False)

    def deserialize(self, data: str, obj_type: type):
        json_data = json.loads(data.encode('utf-8'))

        if isinstance(json_data, list):
            return [self.from_dict(i, obj_type) for i in json_data]
        return self.from_dict(json_data, obj_type)