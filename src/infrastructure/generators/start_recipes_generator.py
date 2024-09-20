import datetime

from src.core.models.recipe import Recipe
from src.core.models.recipe_item import RecipeItem
from src.core.models.unit_value import UnitValue
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.infrastructure.generators.start_unit_generator import StartUnitGenerator


class StartRecipesGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StartRecipesGenerator, cls).__new__(cls)
        return cls._instance

    def get_recipes(self) -> list[Recipe]:
        return [self.__generate_recipe_1(), self.__generate_recipe_2()]

    def __generate_recipe_1(self):
        nomenclature_generator = StartNomenclatureGenerator()
        unit_generator = StartUnitGenerator()

        items = [
            RecipeItem(nomenclature_generator.get_wheat_flour(), UnitValue(100, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_sugar(), UnitValue(80, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_butter(), UnitValue(70, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_egg(), UnitValue(1, unit_generator.get_things())),
            RecipeItem(nomenclature_generator.get_vanilla_sugar(), UnitValue(5, unit_generator.get_grams()))
        ]

        steps = [
            "Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.",
            "Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.",
            "Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.",
            "Добавьте в масло яйцо. Проверьте, не горячее ли масло, чтобы яйцо не сварилось. Перемешайте до однородности.",
            "Всыпьте муку, добавьте ванилин, и перемешайте тесто до однородного состояния.",
            "Разогрейте вафельницу по инструкции к ней. Выкладывайте тесто по столовой ложке. Пеките до золотистого цвета.",
            "Осторожно откройте вафельницу и снимите вафлю лопаткой. Горячие вафли мягкие, но затем становятся хрустящими."
        ]

        return Recipe(
            name="ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ",
            items=items,
            duration=datetime.timedelta(minutes=20),
            steps=steps
        )

    def __generate_recipe_2(self):
        nomenclature_generator = StartNomenclatureGenerator()
        unit_generator = StartUnitGenerator()

        items = [
            RecipeItem(nomenclature_generator.get_chicken_fillet(), UnitValue(500, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_mushrooms(), UnitValue(200, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_onion(), UnitValue(1, unit_generator.get_things())),
            RecipeItem(nomenclature_generator.get_bell_pepper(), UnitValue(1, unit_generator.get_things())),
            RecipeItem(nomenclature_generator.get_dairy_cream(), UnitValue(200, unit_generator.get_milliliters())),
            RecipeItem(nomenclature_generator.get_wheat_flour(), UnitValue(12, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_butter(), UnitValue(30, unit_generator.get_grams())),
            RecipeItem(nomenclature_generator.get_water(), UnitValue(100, unit_generator.get_milliliters()))
        ]

        steps = [
            "Куриное филе нарежьте кубиками, обжарьте на сковороде с 15 гр сливочного масла до золотистой корочки.",
            "В другой сковороде обжарьте нарезанные грибы, болгарский перец и лук до мягкости.",
            "В отдельной кастрюле растопите оставшееся масло, добавьте муку и слегка обжарьте. Постепенно влейте сливки и воду, помешивая, чтобы получился соус.",
            "Соедините курицу и овощи, залейте их соусом. Тушите 10-15 минут на слабом огне.",
            "Добавьте соль и перец по вкусу. Подавайте с гарниром на ваш выбор (например, рисом или пастой)."
        ]

        return Recipe(
            name="КУРИЦА С ОВОЩАМИ В СЛИВОЧНОМ СОУСЕ",
            items=items,
            duration=datetime.timedelta(minutes=40),
            steps=steps
        )
