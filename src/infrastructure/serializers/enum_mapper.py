from enum import Enum

from src.infrastructure.serializers.abstractions.abstract_component_serializer import AbstractComponentSerializer


class EnumMapper(AbstractComponentSerializer[Enum]):

    def from_model(self, obj: Enum) -> int:
        return obj.value

    def to_model(self, data: int) -> int:
        return data