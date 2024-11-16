from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.filter_operation_type import FilterOperationType
from src.core.models.osv_model import OsvModel
from src.core.services.dto.get_osv import GetOsvDTO
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.prototype import PrototypeService
from src.core.services.store_service import StoreManager
from src.infrastructure.factory.osv_factory import OsvFactory, CreateOsvFactoryDTO
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository
from src.utils.observer.event import Event


class OsvManager(AbstractManager):
    _instance = None
    _file_name = None

    __nomenclature_repository: NomenclatureRepository = NomenclatureRepository()
    __store_transaction_repository: StoreTransactionRepository = StoreTransactionRepository()
    __storehouse_repository: StoreHouseRepository = StoreHouseRepository()

    __store_manager: StoreManager = StoreManager()
    __prototype_service = PrototypeService()

    __osv_factory: OsvFactory = OsvFactory()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OsvManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def get_by_dto(self, dto: GetOsvDTO) -> list[OsvModel]:

        filters = []

        if dto.storehouse_id is not None:
            filter_item = FilterItem()

            filter_item.key = "storehouse.unique_code"
            filter_item.value = dto.storehouse_id
            filter_item.operation = FilterOperationType.EQUAL

            filters.append(filter_item)

        start_turnovers_dto = StoreTurnoverDTO()

        start_turnovers_dto.end_time = dto.start_date
        start_turnovers_dto.filters = filters

        start_turnovers = self.__store_manager.get_turnovers(start_turnovers_dto)

        end_turnovers_dto = StoreTurnoverDTO()

        end_turnovers_dto.start_time = dto.start_date
        end_turnovers_dto.end_time = dto.end_date
        end_turnovers_dto.filters = filters

        start_to_end_turnovers = self.__store_manager.get_turnovers(end_turnovers_dto)

        end_turnovers = self.__store_manager.merge_turnovers(start_to_end_turnovers, start_turnovers)

        nomenclatures = self.__nomenclature_repository.get_all()

        storehouses = []

        if dto.storehouse_id is not None:
            storehouses.append(self.__storehouse_repository.get_by_id(dto.storehouse_id))
        else:
            storehouses = self.__storehouse_repository.get_all()

        create_osv_dto = CreateOsvFactoryDTO()

        create_osv_dto.storehouses = storehouses
        create_osv_dto.nomenclatures = nomenclatures

        create_osv_dto.end_turnovers = end_turnovers
        create_osv_dto.end_date = dto.end_date

        create_osv_dto.start_turnovers = start_turnovers
        create_osv_dto.start_date = dto.start_date

        result = self.__osv_factory.create(create_osv_dto)

        return result

    def handle_event(self, event: Event):
        pass