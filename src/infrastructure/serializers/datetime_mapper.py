import datetime
from enum import Enum

from src.infrastructure.serializers.abstractions.abstract_component_serializer import AbstractComponentSerializer


class DatetimeMapper(AbstractComponentSerializer[datetime.datetime]):

    def from_model(self, obj: datetime.datetime) -> float:
        return obj.timestamp()

    def to_model(self, data: float) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(data)


