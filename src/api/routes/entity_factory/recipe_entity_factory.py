from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.recipe import Recipe
from src.infrastructure.repositories.recipes_repository import RecipesRepository


class RecipeEntityFactory(ReportEntityFactory[list[Recipe]]):
    def get_path_name(self) -> str:
        return 'recipes'

    def get_entity(self):
        return RecipesRepository().get_all()
