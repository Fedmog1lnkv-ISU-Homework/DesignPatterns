from src.core.models.unit_model import UnitModel


class StartUnitGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StartUnitGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.__grams = UnitModel('гр', 1)
        self.__kilograms = UnitModel('кг', 1000, self.__grams)

        self.__things = UnitModel('шт', 1)
        self.__tens = UnitModel('десяток', 10, self.__things)

        self.__milliliters = UnitModel('мл', 1)
        self.__liters = UnitModel('л', 1000, self.__milliliters)

    def get_units(self) -> list[UnitModel]:
        return [
            self.__grams,
            self.__kilograms,
            self.__things,
            self.__tens,
            self.__milliliters,
            self.__liters
        ]

    def get_grams(self) -> UnitModel:
        return self.__grams

    def get_kilograms(self) -> UnitModel:
        return self.__kilograms

    def get_things(self) -> UnitModel:
        return self.__things

    def get_tens(self) -> UnitModel:
        return self.__tens

    def get_milliliters(self) -> UnitModel:
        return self.__milliliters

    def get_liters(self) -> UnitModel:
        return self.__liters
