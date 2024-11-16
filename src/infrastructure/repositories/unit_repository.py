from src.core.models.unit_model import UnitModel
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.data_sources.nomenclature_data_source import NomenclatureDataSource
from src.infrastructure.data_sources.nomenclature_group_data_source import NomenclatureGroupDataSource
from src.infrastructure.data_sources.unit_data_source import UnitDataSource


class UnitRepository:
    def __init__(self):
        self.__unit_data_source = UnitDataSource()

    def update_start_units(self, data: list[UnitModel]):
        if self.__unit_data_source.is_not_empty():
            return

        for unit in data:
            self.__unit_data_source.create(unit)

    def get_all(self) -> list[UnitModel]:
        return self.__unit_data_source.get_all()

    def get_by_id(self, id: str) -> UnitModel | None:
        return self.__unit_data_source.get(id)

    def create(self, unit: UnitModel) -> UnitModel:
        return self.__unit_data_source.create(unit)

    def create_multiple(self, units: list[UnitModel]) -> list[UnitModel]:
        result = []

        for unit in units:
            result.append(self.__unit_data_source.create(unit))

        return result