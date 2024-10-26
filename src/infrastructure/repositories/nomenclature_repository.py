from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.data_sources.nomenclature_data_source import NomenclatureDataSource


class NomenclatureRepository:
    def __init__(self):
        self.__nomenclatures_data_source = NomenclatureDataSource()

    def update_start_nomenclatures(self, data: list[Nomenclature]):
        if self.__nomenclatures_data_source.is_not_empty():
            return

        for recipe in data:
            self.__nomenclatures_data_source.create(recipe)

    def get_all(self) -> list[Nomenclature]:
        return self.__nomenclatures_data_source.get_all()