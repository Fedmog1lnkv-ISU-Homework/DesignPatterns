from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class StoreTransactionDataSource(AbstractDataSource[StoreTransaction]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreTransactionDataSource, cls).__new__(cls)
        return cls._instance