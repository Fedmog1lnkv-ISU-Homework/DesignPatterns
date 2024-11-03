from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository


class StoreTransactionEntityFactory(ReportEntityFactory[list[StoreTransaction]]):

    __repository: StoreTransactionRepository = StoreTransactionRepository()

    def get_path_name(self) -> str:
        return 'store_transaction'

    def get_entity(self):
        return self.__repository.get_all()