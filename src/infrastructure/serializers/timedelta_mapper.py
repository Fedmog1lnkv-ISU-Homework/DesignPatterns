import datetime

from src.infrastructure.serializers.abstractions.abstract_component_serializer import AbstractComponentSerializer


class TimedeltaMapper(AbstractComponentSerializer[datetime.timedelta]):

    def from_model(self, obj: datetime.timedelta) -> float:
        return obj.total_seconds()

    def to_model(self, data: float) -> datetime.timedelta:
        return datetime.timedelta(seconds=data)
