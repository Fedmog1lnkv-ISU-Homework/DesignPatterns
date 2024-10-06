from src.core.abstractions.abstract_manager import AbstractManager
from src.infrastructure.generators.start_recipes_generator import StartRecipesGenerator
from src.infrastructure.repositories.recipes_repository import RecipesRepository


class StartManager(AbstractManager):
    def __init__(self):
        self.__recipes_repository = RecipesRepository()
        self.__update_start_recipes()

    def __update_start_recipes(self):
        recipes = StartRecipesGenerator().get_recipes()
        self.__recipes_repository.update_start_recipes(recipes)
