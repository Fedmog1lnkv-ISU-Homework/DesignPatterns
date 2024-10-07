from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.unit_model import UnitModel
from src.infrastructure.generators.start_unit_generator import StartUnitGenerator


class UnitEntityFactory(ReportEntityFactory[list[UnitModel]]):
    def get_path_name(self) -> str:
        return 'units'

    def get_entity(self):
        return StartUnitGenerator().get_units()
