from typing import TypeVar, Generic

from src.core.abstractions.abstract_entity import AbstractEntity

T = TypeVar('T', bound=AbstractEntity)

class AbstractDataSource(Generic[T]):
    def __init__(self):
        self.__data = {}

    def create(self, value: T):
        self.__data[value.unique_code] = value

    def get(self, key: str) -> T | None:
        return self.__data[key]

    def get_all(self) -> list[T]:
        return list(self.__data.values())

    def delete(self, key: str):
        del self.__data[key]

    def is_not_empty(self):
        return len(self.__data.keys()) > 0