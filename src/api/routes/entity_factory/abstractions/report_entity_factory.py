from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class ReportEntityFactory(ABC, Generic[T]):

    @abstractmethod
    def get_path_name(self) -> str:
        pass

    @abstractmethod
    def get_entity(self) -> T:
        pass
