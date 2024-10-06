from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator


class NomenclatureGroupEntityFactory(ReportEntityFactory[list[NomenclatureGroup]]):
    def get_path_name(self) -> str:
        return 'nomenclature-groups'

    def get_entity(self):
        return StartNomenclatureGenerator().get_groups()