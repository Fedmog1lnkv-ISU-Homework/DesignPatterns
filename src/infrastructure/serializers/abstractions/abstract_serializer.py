from abc import abstractmethod, ABC
from enum import Enum
from typing import get_origin, get_args, get_type_hints

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.infrastructure.serializers.datetime_mapper import DatetimeMapper
from src.infrastructure.serializers.timedelta_mapper import TimedeltaMapper


class AbstractSerializer(ABC):
    __primitives = [int, str, float, bool]
    __mappers = [
        TimedeltaMapper(),
        DatetimeMapper(),
    ]

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
            ind = False
            for mapper in self.__mappers:
                if isinstance(value, get_args(type(mapper).__orig_bases__[0])[0]):
                    props[key] = mapper.from_model(value)
                    ind = True
                    break
            if ind:
                continue
                
            if isinstance(value, list):
                props[key] = self._get_list_properties(value)
            elif hasattr(value, '__dict__') and not isinstance(value, (list, dict)):
                props[key] = self._get_object_properties(value)
            else:
                props[key] = value
        return props

    def from_dict(self, data, obj_type):
        if data is None:
            return None

        if obj_type in self.__primitives:
            return data

        for mapper in self.__mappers:
            if issubclass(obj_type, get_args(type(mapper).__orig_bases__[0])[0]):
                return mapper.to_model(data)

        if get_origin(obj_type) == list:
            if not isinstance(data, list):
                raise TypeValidationException(data, list)
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

            field_class = properties[type_hint_name]

            if issubclass(field_class, Enum):
                for value in field_class.__members__.values():
                    if value.value == data[prop] or value.name == data[prop]:
                        setattr(instance, prop, value)
                        break
    
                continue
        
            setattr(instance, prop, self.from_dict(value, properties[type_hint_name]))

        return instance
