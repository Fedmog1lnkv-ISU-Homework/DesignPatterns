from src.core.models.storehouse_model import StoreHouseModel
from src.infrastructure.data_sources.storehouse_data_source import StoreHouseDataSource


class StoreHouseRepository:
    def __init__(self):
        self.__storehouse_data_source = StoreHouseDataSource()

    def update_start_storehouses(self, data: list[StoreHouseModel]):
        if self.__storehouse_data_source.is_not_empty():
            return

        for recipe in data:
            self.__storehouse_data_source.create(recipe)

    def create_multiple(self, data: list[StoreHouseModel]):
        result = []

        for storehouse in data:
            result.append(self.__storehouse_data_source.create(storehouse))

        return result

    def get_all(self) -> list[StoreHouseModel]:
        return self.__storehouse_data_source.get_all()

    def get_by_id(self, id: str) -> StoreHouseModel:
        return self.__storehouse_data_source.get(id)