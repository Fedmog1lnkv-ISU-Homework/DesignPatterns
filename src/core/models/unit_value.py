from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.unit_model import UnitModel


class UnitValue(AbstractEntity):
    __value: float = None
    __unit: UnitModel = None

    def __init__(self, value: float, unit: UnitModel):
        super().__init__()

        self.value = value
        self.unit = unit

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            value = float(value)
            self._value = value
        except:
            raise TypeValidationException(value, float)

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if not isinstance(value, UnitModel):
            raise TypeValidationException(value, UnitModel)
        self._unit = value

    def to_base(self):
        """
        Переводит значение в базовую единицу
        :param value: значение в текущей единице измерения
        :return: значение в базовой единице
        """
        return UnitValue(self.value * self.unit.conversion_factor, self.unit.base_unit)

    @classmethod
    def from_base(cls, value: float, unit: UnitModel):
        """
        Переводит значение из базовой единицы в текущую единицу
        :param value: значение в базовой единице измерения
        :return: значение в текущей единице измерения
        """
        return cls(value / unit.conversion_factor, unit)

    def set_compare_mode(self, other):
        return self.value == other.value and self.unit == other.unit
