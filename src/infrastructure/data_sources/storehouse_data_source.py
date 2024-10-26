from src.core.models.storehouse_model import StoreHouseModel
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class StoreHouseDataSource(AbstractDataSource[StoreHouseModel]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreHouseDataSource, cls).__new__(cls)
        return cls._instance