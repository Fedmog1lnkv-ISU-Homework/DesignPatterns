import json
import os

from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.event_type import EventType
from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.recipe import Recipe
from src.core.models.store_transaction import StoreTransaction
from src.core.models.storehouse_model import StoreHouseModel
from src.core.models.unit_model import UnitModel
from src.core.services.settings_manager import SettingsManager
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
from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.utils.observer.event import Event


class StartManager(AbstractManager):

    __settings_manager = SettingsManager()
    __json_serializer = JsonSerializer()

    def __init__(self):
        self.__recipes_repository = RecipesRepository()
        self.__nomenclature_repository = NomenclatureRepository()
        self.__storehouse_repository = StoreHouseRepository()
        self.__store_transaction_repository = StoreTransactionRepository()
        self.__nomenclature_group_repository = NomenclatureGroupRepository()
        self.__unit_repository = UnitRepository()

        self.__name_to_repository = {
            "recipe": self.__recipes_repository,
            "nomenclature": self.__nomenclature_repository,
            "storehouse": self.__storehouse_repository,
            "store_transaction": self.__store_transaction_repository,
            "nomenclature_group": self.__nomenclature_group_repository,
            "unit": self.__unit_repository,
        }

        self.__name_to_class = {
            "recipe": Recipe,
            "nomenclature": Nomenclature,
            "storehouse": StoreHouseModel,
            "store_transaction": StoreTransaction,
            "nomenclature_group": NomenclatureGroup,
            "unit": UnitModel,
        }

        settings = self.__settings_manager.settings

        if settings.firs_start:
            self.__update_start_repositories()
        else:
            self.__update_start_from_dump()

    def all_data_to_json(self):
        result_data = {}

        for name, repository in self.__name_to_repository.items():
            result_data[name] = self.__json_serializer.serialize_to_dict(repository.get_all())

        return result_data

    def dump_data(self, filename = None):
        result_data = self.all_data_to_json()

        settings = self.__settings_manager.settings

        if filename is None:
            filename = settings.dump_path

        try:
            full_name = f"{os.curdir}{os.sep}{filename}"

            with open(full_name, 'w', encoding='utf-8') as stream:
                json.dump(result_data, stream, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Ошибка записи в файл {filename}: {e}")

    def __update_start_from_dump(self):
        entity_data = {}

        settings = self.__settings_manager.settings

        filename = settings.dump_path

        try:
            full_name = f"{os.curdir}{os.sep}{filename}"
            with open(full_name, 'r', encoding='utf-8') as stream:
                data = json.load(stream)

                for name, entity_type in self.__name_to_class.items():
                    if name in data:
                        entity_data[name] = self.__json_serializer.deserialize_from_dict(data[name], entity_type)

                for name, repository in self.__name_to_repository.items():
                    repository.create_multiple(entity_data[name])

                print("Данные загружены из файла.")
        except IOError as e:
            print(f"Ошибка чтения из файла {filename}: {e}")

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

        if event.type == EventType.DUMP_DATA:
            self.dump_data(event.data)
