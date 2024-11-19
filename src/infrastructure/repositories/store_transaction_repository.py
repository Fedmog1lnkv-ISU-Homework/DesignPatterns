from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.data_sources.store_transaction_data_source import StoreTransactionDataSource


class StoreTransactionRepository:
    def __init__(self):
        self.__store_transaction_data_source = StoreTransactionDataSource()

    def update_start_store_transactions(self, data: list[StoreTransaction]):
        if self.__store_transaction_data_source.is_not_empty():
            return

        for recipe in data:
            self.__store_transaction_data_source.create(recipe)

    def get_all(self) -> list[StoreTransaction]:
        return self.__store_transaction_data_source.get_all()

    def create_multiple(self, data: list[StoreTransaction]):
        result = []

        for transaction in data:
            result.append(self.__store_transaction_data_source.create(transaction))

        return result

    def create(self, data: StoreTransaction):
        self.__store_transaction_data_source.create(data)

    def update(self, data: StoreTransaction):
        self.__store_transaction_data_source.create(data)