from datetime import timedelta

import pytest

from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.recipe import Recipe
from src.core.models.recipe_item import RecipeItem
from src.core.models.unit_model import UnitModel
from src.core.models.unit_value import UnitValue
from src.core.services.start_manager import StartManager
from src.infrastructure.data_sources.recipes_data_source import RecipesDataSource


def test_initial_recipes_added():
    data_source = RecipesDataSource()
    old_len = len(data_source.get_all())
    StartManager()
    new_len = len(data_source.get_all())

    assert new_len > old_len


def test_initial_recipes_not_added():
    data_source = RecipesDataSource()
    StartManager()
    old_len = len(data_source.get_all())
    StartManager()
    new_len = len(data_source.get_all())

    assert new_len == old_len


def test_recipe_item_validation():
    with pytest.raises(TypeValidationException):
        RecipeItem('', UnitValue(1, UnitModel('', 1)))

    with pytest.raises(TypeValidationException):
        RecipeItem(Nomenclature('', '', UnitModel('', 1)), '')


def test_recipe_validation():
    Recipe(name='', items=[], duration=timedelta(minutes=10), steps=[])

    with pytest.raises(TypeValidationException):
        Recipe(name=1, items=[], duration=timedelta(minutes=10), steps=[])

    with pytest.raises(TypeValidationException):
        Recipe(name='', items={}, duration=timedelta(minutes=10), steps=[])

    with pytest.raises(TypeValidationException):
        Recipe(name='', items=[], duration=1, steps=[])

    with pytest.raises(TypeValidationException):
        Recipe(name='', items=[], duration=timedelta(minutes=10), steps=1)
