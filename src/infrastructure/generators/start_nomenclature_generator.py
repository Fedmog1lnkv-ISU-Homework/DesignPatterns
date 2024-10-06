from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.generators.start_unit_generator import StartUnitGenerator


class StartNomenclatureGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StartNomenclatureGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        generator = StartUnitGenerator()

        self.__group = NomenclatureGroup('Еда')

        self.__wheat_flour = Nomenclature('Пшеничная мука', self.__group, generator.get_kilograms())
        self.__sugar = Nomenclature('Сахар', self.__group, generator.get_kilograms())
        self.__butter = Nomenclature('Сливочное масло', self.__group, generator.get_kilograms())
        self.__egg = Nomenclature('Яйцо', self.__group, generator.get_kilograms())
        self.__vanilla_sugar = Nomenclature('Ванильный сахар', self.__group, generator.get_kilograms())
        self.__chicken_fillet = Nomenclature('Куриное филе', self.__group, generator.get_kilograms())
        self.__mushrooms = Nomenclature('Шампиньоны', self.__group, generator.get_kilograms())
        self.__onion = Nomenclature('Лук репчатый', self.__group, generator.get_kilograms())
        self.__dairy_cream = Nomenclature('Сливки', self.__group, generator.get_liters())
        self.__bell_pepper = Nomenclature('Болгарский перец', self.__group, generator.get_things())
        self.__water = Nomenclature('Вода', self.__group, generator.get_liters())

    def get_groups(self) -> list[NomenclatureGroup]:
        return [self.__group]

    def get_nomenclatures(self) -> list[Nomenclature]:
        return [
            self.__wheat_flour,
            self.__sugar,
            self.__butter,
            self.__egg,
            self.__vanilla_sugar,
            self.__chicken_fillet,
            self.__mushrooms,
            self.__onion,
            self.__dairy_cream,
            self.__bell_pepper,
            self.__water
        ]

    def get_wheat_flour(self) -> Nomenclature:
        return self.__wheat_flour

    def get_sugar(self) -> Nomenclature:
        return self.__sugar

    def get_butter(self) -> Nomenclature:
        return self.__butter

    def get_egg(self) -> Nomenclature:
        return self.__egg

    def get_vanilla_sugar(self) -> Nomenclature:
        return self.__vanilla_sugar

    def get_chicken_fillet(self) -> Nomenclature:
        return self.__chicken_fillet

    def get_mushrooms(self) -> Nomenclature:
        return self.__mushrooms

    def get_onion(self) -> Nomenclature:
        return self.__onion

    def get_bell_pepper(self) -> Nomenclature:
        return self.__bell_pepper

    def get_dairy_cream(self) -> Nomenclature:
        return self.__dairy_cream

    def get_water(self) -> Nomenclature:
        return self.__water
