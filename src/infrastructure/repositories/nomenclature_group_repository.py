from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.data_sources.nomenclature_data_source import NomenclatureDataSource
from src.infrastructure.data_sources.nomenclature_group_data_source import NomenclatureGroupDataSource


class NomenclatureGroupRepository:
    def __init__(self):
        self.__nomenclature_groups_data_source = NomenclatureGroupDataSource()

    def update_start_nomenclature_groups(self, data: list[NomenclatureGroup]):
        if self.__nomenclature_groups_data_source.is_not_empty():
            return

        for nomenclature_group in data:
            self.__nomenclature_groups_data_source.create(nomenclature_group)

    def get_all(self) -> list[NomenclatureGroup]:
        return self.__nomenclature_groups_data_source.get_all()

    def get_by_id(self, id: str) -> NomenclatureGroup | None:
        return self.__nomenclature_groups_data_source.get(id)

    def create(self, nomenclature_group: NomenclatureGroup) -> NomenclatureGroup:
        return self.__nomenclature_groups_data_source.create(nomenclature_group)

    def create_multiple(self, nomenclature_groups: list[NomenclatureGroup]) -> list[NomenclatureGroup]:
        result = []

        for nomenclature_group in nomenclature_groups:
            result.append(self.__nomenclature_groups_data_source.create(nomenclature_group))

        return result