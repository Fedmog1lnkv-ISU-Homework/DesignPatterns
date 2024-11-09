from src.core.abstractions.abstract_manager import AbstractManager
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.infrastructure.generators.start_recipes_generator import StartRecipesGenerator
from src.infrastructure.generators.start_store_transaction_generator import StoreTransactionGenerator
from src.infrastructure.generators.start_storehouse_generator import StartStoreHouseGenerator
from src.infrastructure.generators.start_unit_generator import StartUnitGenerator
from src.infrastructure.repositories.nomenclature_group_repository import NomenclatureGroupRepository
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository
from src.infrastructure.repositories.unit_repository import UnitRepository
from src.utils.observer.event import Event


class StartManager(AbstractManager):
    def __init__(self):
        self.__recipes_repository = RecipesRepository()
        self.__nomenclature_repository = NomenclatureRepository()
        self.__storehouse_repository = StoreHouseRepository()
        self.__store_transaction_repository = StoreTransactionRepository()
        self.__nomenclature_group_repository = NomenclatureGroupRepository()
        self.__unit_repository = UnitRepository()
        
        self.__update_start_repositories()

    def __update_start_repositories(self):
        recipes = StartRecipesGenerator().get_recipes()
        self.__recipes_repository.update_start_recipes(recipes)
        
        nomenclatures = StartNomenclatureGenerator().get_nomenclatures()
        self.__nomenclature_repository.update_start_nomenclatures(nomenclatures)
        
        stores = StartStoreHouseGenerator().get_storehouses()
        self.__storehouse_repository.update_start_storehouses(stores)
        
        store_transactions = StoreTransactionGenerator().get_store_transactions()
        self.__store_transaction_repository.update_start_store_transactions(store_transactions)  
        
        units = StartUnitGenerator().get_units()
        self.__unit_repository.update_start_units(units)
        
        nomenclature_groups = StartNomenclatureGenerator().get_groups()
        self.__nomenclature_group_repository.update_start_nomenclature_groups(nomenclature_groups)

    def handle_event(self, event: Event):
        super().handle_event(event)
        
