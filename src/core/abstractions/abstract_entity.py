import uuid
from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """
    Абстрактный класс для наследования моделей данных
    """

    def __init__(self):
        self.__unique_code = str(uuid.uuid4())

    @property
    def unique_code(self) -> str:
        """
        Уникальный код
        """
        return self.__unique_code

    @abstractmethod
    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code

    def __eq__(self, other) -> bool:
        return self.set_compare_mode(other)
