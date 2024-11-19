from src.core.models.recipe import Recipe
from src.infrastructure.data_sources.recipes_data_source import RecipesDataSource


class RecipesRepository:
    def __init__(self):
        self.__recipes_data_source = RecipesDataSource()

    def update_start_recipes(self, start_recipes: list[Recipe]):
        if self.__recipes_data_source.is_not_empty():
            return

        for recipe in start_recipes:
            self.__recipes_data_source.create(recipe)

    def create_multiple(self, recipes: list[Recipe]):
        result = []

        for recipe in recipes:
            result.append(self.__recipes_data_source.create(recipe))

        return result

    def get_all(self) -> list[Recipe]:
        return self.__recipes_data_source.get_all()
    
    def update(self, recipe: Recipe) -> Recipe:
        return self.__recipes_data_source.create(recipe)
