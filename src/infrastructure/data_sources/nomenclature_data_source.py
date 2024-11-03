from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.data_sources.abstractions.abstract_data_source import AbstractDataSource


class NomenclatureDataSource(AbstractDataSource[Nomenclature]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NomenclatureDataSource, cls).__new__(cls)
        return cls._instance