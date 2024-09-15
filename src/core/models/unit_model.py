from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.exceptions.validation_exception import TypeValidationException


class UnitModel(AbstractEntity):
    """
    Модель единицы измерения
    """

    def __init__(self, name: str, conversion_factor: float, base_unit=None):
        super().__init__()
        self.__name = None
        self.__conversion_factor = None
        self.__base_unit = None

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

    @base_unit.setter
    def base_unit(self, unit):
        if unit is None:
            return
        if not isinstance(unit, UnitModel):
            raise TypeValidationException(unit, UnitModel)

        self.__base_unit = unit

    def to_base(self, value: float) -> float:
        """
        Переводит значение в базовую единицу
        :param value: значение в текущей единице измерения
        :return: значение в базовой единице
        """
        return value * self.__conversion_factor

    def from_base(self, value: float) -> float:
        """
        Переводит значение из базовой единицы в текущую единицу
        :param value: значение в базовой единице измерения
        :return: значение в текущей единице измерения
        """
        return value / self.__conversion_factor

    def set_compare_mode(self, other) -> bool:
        """
        Сравнение по наименованию
        :param other: другой объект для сравнения
        :return: True, если объекты равны по имени, иначе False
        """
        if not isinstance(other, UnitModel):
            return False
        return self.name == other.name and self.conversion_factor ==  other.conversion_factor

