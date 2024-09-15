from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException, LengthValidationException
from src.core.models.unit_model import UnitModel


class Nomenclature(AbstractEntity):
    """
    Модель номенклатуры
    """

    def __init__(self, name: str, group_id: str, units: UnitModel):
        super().__init__()

        self.__name = None
        self.__units = None
        self.__group_id = None

        self.name = name.strip()
        self.units = units
        self.group_id = group_id

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__group_id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        if len(value) > 255:
            raise LengthValidationException(value, 255)
        self.__name = value.strip()
