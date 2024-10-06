from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.nomenclature_model import Nomenclature
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator


class NomenclatureEntityFactory(ReportEntityFactory[list[Nomenclature]]):
    def get_path_name(self) -> str:
        return 'nomenclatures'

    def get_entity(self):
        return StartNomenclatureGenerator().get_nomenclatures()
