from src.core.models.store_turnover import StoreTurnover
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class StoreTurnoverDataSource(AbstractDataSource[StoreTurnover]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreTurnoverDataSource, cls).__new__(cls)
        return cls._instance