from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.unit_value import UnitValue


class RecipeItem(AbstractEntity):
    __nomenclature: Nomenclature = None
    __unit_value: UnitValue = None

    def set_compare_mode(self, other_object) -> bool:
        return super().set_compare_mode(other_object)

    def __init__(self, nomenclature: Nomenclature, unit_value: UnitValue):
        super().__init__()

        self.nomenclature = nomenclature
        self.unit_value = unit_value


    @property
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value):
        if not isinstance(value, Nomenclature):
            raise TypeValidationException(value, Nomenclature)
        self.__nomenclature = value

    @property
    def unit_value(self) -> UnitValue:
        return self.__unit_value

    @unit_value.setter
    def unit_value(self, value):
        if not isinstance(value, UnitValue):
            raise TypeValidationException(value, UnitValue)
        self.__unit_value = value