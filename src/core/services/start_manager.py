from src.core.abstractions.abstract_manager import AbstractManager
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.infrastructure.generators.start_recipes_generator import StartRecipesGenerator
from src.infrastructure.generators.start_store_transaction_generator import StoreTransactionGenerator
from src.infrastructure.generators.start_storehouse_generator import StartStoreHouseGenerator
from src.infrastructure.repositories.nomenclature_repository import NomenclatureRepository
from src.infrastructure.repositories.recipes_repository import RecipesRepository
from src.infrastructure.repositories.store_transaction_repository import StoreTransactionRepository
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository


class StartManager(AbstractManager):
    def __init__(self):
        self.__recipes_repository = RecipesRepository()
        self.__nomenclature_repository = NomenclatureRepository()
        self.__storehouse_repository = StoreHouseRepository()
        self.__store_transaction_repository = StoreTransactionRepository()
        
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
        
