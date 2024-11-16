from src.core.models.unit_model import UnitModel
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class UnitDataSource(AbstractDataSource[UnitModel]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UnitDataSource, cls).__new__(cls)
        return cls._instance