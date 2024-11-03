import builtins
from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class UnitModel(AbstractEntity):
    """
    Модель единицы измерения
    """
    __name: str= None
    __conversion_factor: float = None
    __base_unit: 'UnitModel' = None

    def __init__(self, name: str, conversion_factor: float, base_unit=None):
        super().__init__()

        self.name = name.strip()  # наименование
        self.conversion_factor = conversion_factor  # коэффициент пересчета
        self.base_unit = base_unit  # базовая единица

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)

        self.__name = value.strip()

    @property
    def conversion_factor(self) -> float:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: float):
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeValidationException(value, float)

        self.__conversion_factor = value

    @property
    def base_unit(self):
        return self.__base_unit

    def get_super_base_unit(self) -> 'UnitModel':
        unit = self
        total_conversion_factor = self.conversion_factor
        
        while unit.base_unit is not None:
            unit = unit.base_unit
            total_conversion_factor *= unit.conversion_factor
        
        return unit

    @base_unit.setter
    def base_unit(self, unit):
        if unit is None:
            return
        if not isinstance(unit, UnitModel):
            raise TypeValidationException(unit, UnitModel)

        self.__base_unit = unit

    def set_compare_mode(self, other) -> bool:
        """
        Сравнение по наименованию
        :param other: другой объект для сравнения
        :return: True, если объекты равны по имени, иначе False
        """
        if not isinstance(other, UnitModel):
            return False
        return self.name == other.name and self.conversion_factor ==  other.conversion_factor

builtins.UnitModel = UnitModel