import datetime
from abc import abstractmethod, ABC
from typing import get_origin, get_args, get_type_hints

from src.core.abstractions.abstract_entity import AbstractEntity


class AbstractSerializer(ABC):
    __primitives = [int, str, float, bool]

    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize(self, data, obj_type):
        pass

    def get_properties(self, obj: list | object) -> list[dict] | dict:
        if isinstance(obj, list):
            return self._get_list_properties(obj)
        else:
            return self._get_object_properties(obj)

    def _get_list_properties(self, obj: list) -> list[dict]:
        res = []
        for item in obj:
            if hasattr(item, '__dict__'):
                res += [self._get_object_properties(item)]
            else:
                res += [item]
        return res

    def _get_object_properties(self, obj) -> dict:
        props = self._extract_properties(obj)

        if isinstance(obj, AbstractEntity):
            props['unique_code'] = obj.unique_code

        props = self._process_nested_properties(props)

        return props

    def _extract_properties(self, obj) -> dict:
        return {
            key: getattr(obj, key)
            for key, value in obj.__class__.__dict__.items()
            if isinstance(value, property)
        }

    def _process_nested_properties(self, props: dict) -> dict:
        for key, value in props.items():
            if isinstance(value, list):
                props[key] = self._get_list_properties(value)
            elif hasattr(value, '__dict__') and not isinstance(value, (list, dict)):
                props[key] = self._get_object_properties(value)
            elif isinstance(value, datetime.timedelta):
                props[key] = value.total_seconds()
            else:
                props[key] = value
        return props

    def from_dict(self, data, obj_type):
        if data is None:
            return None

        if obj_type in self.__primitives:
            return data

        if issubclass(obj_type, datetime.timedelta):
            return datetime.timedelta(seconds=float(data))

        if get_origin(obj_type) == list:
            list_type = get_args(obj_type)[0]
            return [self.from_dict(i, list_type) for i in data]

        instance = obj_type.__new__(obj_type, obj_type)

        properties = get_type_hints(obj_type)

        for prop, value in data.items():
            if prop == "unique_code":
                type_hint_name = "_AbstractEntity__unique_code"
            else:
                type_hint_name = f"_{obj_type.__name__}__{prop}"

            if type_hint_name not in properties.keys():
                continue

            setattr(instance, prop, self.from_dict(value, properties[type_hint_name]))

        return instance
