from typing import TypeVar, Generic

from src.core.abstractions.abstract_entity import AbstractEntity

T = TypeVar('T', bound=AbstractEntity)

class AbstractDataSource(Generic[T]):
    def __init__(self):
        self.__data = {}

    def create(self, value: T) -> T:
        self.__data[value.unique_code] = value
        
        return value 

    def get(self, key: str) -> T | None:
        if key not in self.__data.keys():
            return None
        return self.__data[key]

    def get_all(self) -> list[T]:
        return list(self.__data.values())

    def delete(self, key: str):
        del self.__data[key]

    def delete_all(self):
        self.__data = {}

    def is_not_empty(self):
        return len(self.__data.keys()) > 0