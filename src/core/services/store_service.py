from copy import deepcopy
from datetime import datetime

from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.filter_operation_type import FilterOperationType
from src.core.models.store_turnover import StoreTurnover
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.prototype import PrototypeService
from src.core.services.settings_manager import SettingsManager
from src.infrastructure.factory.store_turnover_factory import StoreTurnoverFactory
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.store_turnover_repository import StoreTurnoverRepository
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository


class StoreManager(AbstractManager):

    __recipes_repository = RecipesRepository()
    __nomenclature_repository = NomenclatureRepository()
    __storehouse_repository = StoreHouseRepository()
    __store_transaction_repository = StoreTransactionRepository()
    __store_turnover_repository = StoreTurnoverRepository()
    __store_turnover_factory = StoreTurnoverFactory()
    __settings_manager = SettingsManager()
    
    __prototype_service = PrototypeService()

    def init_store_turnovers_by_date_block(self) -> None:

        settings = self.__settings_manager.settings

        dto = StoreTurnoverDTO()

        dto.end_time = settings.date_block
        dto.start_time = datetime.min

        turnovers = self.calculate_turnovers(dto)

        self.__store_turnover_repository.update_store_turnovers(turnovers)

    def update_turnovers_by_date_block(self, new_date_block: datetime) -> None:

        dto = StoreTurnoverDTO()

        dto.end_time = new_date_block

        turnovers = self.get_turnovers(dto)

        self.__store_turnover_repository.update_store_turnovers(turnovers)

    def calculate_turnovers_with_date_block(self, dto: StoreTurnoverDTO) -> list[StoreTurnover]:

        dto.start_time = self.__settings_manager.settings.date_block

        new_turnovers = self.calculate_turnovers(dto)

        old_turnovers = self.__store_turnover_repository.get_all()

        filtered_old_turnovers = self.__prototype_service.get_by_filters(old_turnovers, dto.filters)

        result = self.__store_turnover_factory.merge_turnovers(new_turnovers, filtered_old_turnovers)

        return result

    def get_turnovers(self, dto: StoreTurnoverDTO) -> list[StoreTurnover]:

        settings = self.__settings_manager.settings

        dto = deepcopy(dto)

        if dto.start_time is None:
            if dto.end_time < settings.date_block:
                dto.start_time = datetime.min
            else:
                return self.calculate_turnovers_with_date_block(dto)

        return self.calculate_turnovers(dto)

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
        
        
        
        