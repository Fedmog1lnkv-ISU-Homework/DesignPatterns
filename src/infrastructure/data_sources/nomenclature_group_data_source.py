from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class NomenclatureGroupDataSource(AbstractDataSource[NomenclatureGroup]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NomenclatureGroupDataSource, cls).__new__(cls)
        return cls._instance