from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.filter_operation_type import FilterOperationType
from src.core.models.store_turnover import StoreTurnover
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.prototype import PrototypeService
from src.infrastructure.factory.store_turnover_factory import StoreTurnoverFactory
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository


class StoreManager(AbstractManager):

    __recipes_repository = RecipesRepository()
    __nomenclature_repository = NomenclatureRepository()
    __storehouse_repository = StoreHouseRepository()
    __store_transaction_repository = StoreTransactionRepository()
    __store_turnover_factory = StoreTurnoverFactory()
    
    __prototype_service = PrototypeService()
    
    def calculate_turnovers(self, dto: StoreTurnoverDTO) -> list[StoreTurnover]:
        
        date_filter = FilterItem()
        
        date_filter.key = 'date'
        date_filter.value = [dto.start_time, dto.end_time]
        date_filter.operation = FilterOperationType.BETWEEN
        
        filters = []
        
        filters.append(date_filter)
        
        if dto.filters is not None:
            for filter in dto.filters:
                filters.append(filter)
        
        transactions = self.__store_transaction_repository.get_all()
        
        filtered_transactions = self.__prototype_service.get_by_filters(transactions, filters)
        
        return self.__store_turnover_factory.create(filtered_transactions)
        
        
        
        