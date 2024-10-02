import uuid
from abc import ABC, abstractmethod

from src.core.exceptions.validation_exception import TypeValidationException


class AbstractEntity(ABC):
    """
    Абстрактный класс для наследования моделей данных
    """
    __unique_code: str = None

    def __init__(self):
        self.__unique_code = str(uuid.uuid4())

    @property
    def unique_code(self) -> str:
        """
        Уникальный код
        """
        return self.__unique_code
    
    @unique_code.setter
    def unique_code(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)

        self.__unique_code = value.strip()

    @abstractmethod
    def set_compare_mode(self, other_object) -> bool:
        return self.__unique_code == other_object.__unique_code

    def __eq__(self, other) -> bool:
        return self.set_compare_mode(other)
