from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.event_type import EventType
from src.core.enums.filter_operation_type import FilterOperationType
from src.core.models.nomenclature_model import Nomenclature
from src.core.services.prototype import PrototypeService
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.utils.observer.event import Event


class RecipeManager(AbstractManager):

    _instance = None
    _file_name = None

    __recipe_repository: RecipesRepository = RecipesRepository()
    __prototype_service = PrototypeService()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RecipeManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        
    def update_recipes_by_event(self, nomenclature: Nomenclature) -> None:
        
        all_recipes = self.__recipe_repository.get_all()
        
        filter_recipe = FilterItem()
        filter_recipe.key = 'items.nomenclature.unique_code'
        filter_recipe.value = nomenclature.unique_code
        filter_recipe.operation = FilterOperationType.EQUAL

        filtered_recipes = self.__prototype_service.get_by_filters(all_recipes, [filter_recipe])
        
        for recipe in filtered_recipes:
            for i, item in enumerate(recipe.items):
                if item.nomenclature.unique_code == nomenclature.unique_code:
                    recipe.items[i].nomenclature = nomenclature

            self.__recipe_repository.update(recipe)

    def handle_event(self, event: Event):
        super().handle_event(event)
        
        if event.type == EventType.CHANGE_NOMENCLATURE:
            self.update_recipes_by_event(event.data)