from src.core.models.store_turnover import StoreTurnover
from src.infrastructure.data_sources.storage_turnover_data_source import StoreTurnoverDataSource


class StoreTurnoverRepository:
    def __init__(self):
        self.__store_turnover_data_source = StoreTurnoverDataSource()

    def update_store_turnovers(self, data: list[StoreTurnover]):
        if self.__store_turnover_data_source.is_not_empty():
            self.__store_turnover_data_source.delete_all()

        for turnover in data:
            self.__store_turnover_data_source.create(turnover)

    def get_all(self) -> list[StoreTurnover]:
        return self.__store_turnover_data_source.get_all()