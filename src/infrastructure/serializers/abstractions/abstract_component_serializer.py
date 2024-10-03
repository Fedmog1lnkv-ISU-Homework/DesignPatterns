from abc import abstractmethod, ABC
from typing import Generic, TypeVar

T = TypeVar('T')

class AbstractComponentSerializer(ABC, Generic[T]):
    @abstractmethod
    def from_model(self, obj):
        pass

    @abstractmethod
    def to_model(self, data) -> T:
        pass