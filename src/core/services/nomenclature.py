from src.di.observer_manager import observer_manager
from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.event_type import EventType
from src.core.enums.filter_operation_type import FilterOperationType
from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.nomenclature_model import Nomenclature
from src.core.services.dto.create_nomenclature import CreateNomenclatureDTO
from src.core.services.dto.update_nomenclature import UpdateNomenclatureDTO
from src.core.services.prototype import PrototypeService
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.repositories.nomenclature_group_repository import NomenclatureGroupRepository
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.unit_repository import UnitRepository
from src.utils.observer.event import Event


class NomenclatureManager(AbstractManager):
    _instance = None
    _file_name = None
    
    __nomenclature_repository: NomenclatureRepository = NomenclatureRepository()
    __recipe_repository: RecipesRepository = RecipesRepository()
    __store_transaction_repository: StoreTransactionRepository = StoreTransactionRepository()
    __unit_repository: UnitRepository = UnitRepository()
    __nomenclature_group_repository: NomenclatureGroupRepository = NomenclatureGroupRepository()

    __prototype_service = PrototypeService()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NomenclatureManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        super().__init__()
        
    def get_by_id(self, id: str) -> Nomenclature | None:
        result = self.__nomenclature_repository.get_by_id(id)
        
        return result
    
    def create(self, dto: CreateNomenclatureDTO) -> Nomenclature:
        if not isinstance(dto, CreateNomenclatureDTO):
            raise TypeValidationException(dto, CreateNomenclatureDTO)
        
        unit = self.__unit_repository.get_by_id(dto.unit_id)
        if unit is None:
            raise ValueError("Unit not found")
        
        group = self.__nomenclature_group_repository.get_by_id(dto.nomenclature_group_id)
        if group is None:
            raise ValueError("Nomenclature group not found")
            
        nomenclature = Nomenclature(dto.name, group, unit)
        
        return self.__nomenclature_repository.create(nomenclature)

    def update(self, dto: UpdateNomenclatureDTO) -> Nomenclature:
        if not isinstance(dto, UpdateNomenclatureDTO):
            raise TypeValidationException(dto, UpdateNomenclatureDTO)
        
        old_nomenclature = self.get_by_id(dto.id)
        if old_nomenclature is None:
            raise ValueError("Nomenclature not found")
        
        if dto.unit_id is not None:
            unit = self.__unit_repository.get_by_id(dto.unit_id)
            if unit is None:
                raise ValueError("Unit not found")
            
            old_nomenclature.units = unit

        if dto.nomenclature_group_id is not None:
            group = self.__nomenclature_group_repository.get_by_id(dto.nomenclature_group_id)
            if group is None:
                raise ValueError("Nomenclature group not found")
            
            old_nomenclature.group = group
        
        if dto.name is not None:
            old_nomenclature.name = dto.name
            
        result = self.__nomenclature_repository.update(old_nomenclature)
        
        event = Event()
        event.data = result
        event.type = EventType.CHANGE_NOMENCLATURE
        
        observer_manager.notify(event)

        return result
    
    def __is_used(self, id: str) -> bool:
        all_recipes = self.__recipe_repository.get_all()
        
        filter_recipe = FilterItem()
        filter_recipe.key = 'items.nomenclature.unique_code'
        filter_recipe.value = id
        filter_recipe.operation = FilterOperationType.EQUAL

        filtered_recipes = self.__prototype_service.get_by_filters(all_recipes, [filter_recipe])
        
        if len(filtered_recipes) > 0:
            return True

        all_transactions = self.__store_transaction_repository.get_all()

        filter_recipe = FilterItem()
        filter_recipe.key = 'nomenclature.unique_code'
        filter_recipe.value = id
        filter_recipe.operation = FilterOperationType.EQUAL

        filtered_transactions = self.__prototype_service.get_by_filters(all_transactions, [filter_recipe])

        if len(filtered_transactions) > 0:
            return True
        
        return False
        
    def delete(self, id: str) -> None:
        if not isinstance(id, str):
            raise TypeValidationException(id, str)
        
        if self.__is_used(id):
            raise ValueError("Nomenclature is used")
        
        self.__nomenclature_repository.delete(id)
        
    def handle_event(self, event: Event):
        super().handle_event(event)