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
    
    def get_by_id(self, id: str) -> Nomenclature | None:
        return self.__nomenclatures_data_source.get(id)
    
    def create(self, nomenclature: Nomenclature) -> Nomenclature:
        return self.__nomenclatures_data_source.create(nomenclature)
    
    def create_multiple(self, nomenclatures: list[Nomenclature]) -> list[Nomenclature]:
        result = []
        
        for nomenclature in nomenclatures:
            result.append(self.__nomenclatures_data_source.create(nomenclature))
        
        return result
    
    def update(self, nomenclature: Nomenclature) -> Nomenclature:
        return self.__nomenclatures_data_source.create(nomenclature)
    
    def delete(self, id: str) -> None:
        self.__nomenclatures_data_source.delete(id)