from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository


class StoreTransactionEntityFactory():

    __repository: StoreTransactionRepository = StoreTransactionRepository()

    def get_path_name(self) -> str:
        return 'store_transaction'

    def get_entity(self):
        return self.__repository.get_all()