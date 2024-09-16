from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class NomenclatureGroup(AbstractEntity):
    __name: str = ""

    def __init__(self, type_name: str):
        super().__init__()
        self.__name = type_name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)

        self.__name = value

    @staticmethod
    def create_group():
        return NomenclatureGroup("Ингредиенты")

    def set_compare_mode(self, other) -> bool:
        if not isinstance(other, NomenclatureGroup):
            return False
        return self.name == other.name
