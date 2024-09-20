import datetime

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.recipe_item import RecipeItem


class Recipe(AbstractEntity):
    def set_compare_mode(self, other_object) -> bool:
        return super().set_compare_mode(other_object)

    def __init__(self, name: str, items: list[RecipeItem], duration: datetime.timedelta, steps: list[str]):
        super().__init__()
        self.__name = None
        self.__items = None
        self.__duration = None
        self.__steps = None

        self.name = name
        self.items = items
        self.duration = duration
        self.steps = steps


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__name = value

    @property
    def items(self) -> list[RecipeItem]:
        return self.__items

    @items.setter
    def items(self, value):
        if not isinstance(value, list):
            raise TypeValidationException(value, list)
        self.__items = value

    @property
    def duration(self) -> datetime.timedelta:
        return self.__duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, datetime.timedelta):
            raise TypeValidationException(value, datetime.timedelta)
        self.__duration = value

    @property
    def steps(self) -> list[str]:
        return self.__steps

    @steps.setter
    def steps(self, value):
        if not isinstance(value, list):
            raise TypeValidationException(value, list)
        self.__steps = value
