from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException, LengthValidationException
from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.unit_model import UnitModel


class Nomenclature(AbstractEntity):
    """
    Модель номенклатуры
    """

    def __init__(self, name: str, group: NomenclatureGroup, units: UnitModel):
        super().__init__()

        self.__name = None
        self.__units = None
        self.__group = None

        self.name = name.strip()
        self.units = units
        self.group = group

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: NomenclatureGroup):
        if not isinstance(value, NomenclatureGroup):
            raise TypeValidationException(value, NomenclatureGroup)
        self.__group = value

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

    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, value: UnitModel):
        if value is None:
            return
        if not isinstance(value, UnitModel):
            raise TypeValidationException(value, UnitModel)
        self.__units = value


    def set_compare_mode(self, other) -> bool:
        return super().set_compare_mode(other)
