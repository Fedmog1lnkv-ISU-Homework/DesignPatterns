from src.core.services.dto.update_nomenclature import UpdateNomenclatureDTO
from src.core.services.nomenclature import NomenclatureManager
from src.core.services.recipe_manager import RecipeManager
from src.core.services.start_manager import StartManager
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.utils.observer.observer import ObserverManager


def test_observ_in_recipe_manager():
    nomenclature_manager = NomenclatureManager()
    recipe_manager = RecipeManager()

    StartManager()

    observer_manager = ObserverManager()
    observer_manager.add(recipe_manager)

    nomenclature = StartNomenclatureGenerator().get_egg()

    update_nomenclature_dto = UpdateNomenclatureDTO()

    update_nomenclature_dto.id = nomenclature.unique_code
    update_nomenclature_dto.name = "test eggs"

    updated_nomenclature = nomenclature_manager.update(update_nomenclature_dto)

    all_recipes = recipe_manager.get_all()

    found_updated_nomenclature = False

    for recipe in all_recipes:
        for item in recipe.items:
            if item.nomenclature.unique_code == updated_nomenclature.unique_code:
                assert item.nomenclature.name == "test eggs"
                found_updated_nomenclature = True

    assert found_updated_nomenclature
