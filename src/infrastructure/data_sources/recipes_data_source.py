from src.core.models.recipe import Recipe
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class RecipesDataSource(AbstractDataSource[Recipe]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RecipesDataSource, cls).__new__(cls)
        return cls._instance
