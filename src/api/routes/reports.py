from flask import Blueprint, request

from src.api.routes.entity_factory.nomenclature_entity_factory import NomenclatureEntityFactory
from src.api.routes.entity_factory.nomenclature_group_entity_factory import NomenclatureGroupEntityFactory
from src.api.routes.entity_factory.recipe_entity_factory import RecipeEntityFactory
from src.api.routes.entity_factory.unit_entity_factory import UnitEntityFactory
from src.core.enums.report_format import ReportFormat
from src.core.services.settings_manager import SettingsManager
from src.infrastructure.factory.report_factory import ReportFactory

__entity_factories = [
    NomenclatureEntityFactory(),
    RecipeEntityFactory(),
    UnitEntityFactory(),
    NomenclatureGroupEntityFactory()
]

reports_blueprint = Blueprint('/api/reports', __name__, url_prefix='/api/reports')


@reports_blueprint.route('/formats', methods=['GET'])
def get_report_formats():
    return {'formats': ReportFormat.get_all()}


@reports_blueprint.route('/report/<entity>', methods=['GET'])
def get_report(entity):
    report_format_str = request.args.get('format')
    if report_format_str is None:
        return 'No report format', 400
    report_format_str = report_format_str.upper()
    if report_format_str not in ReportFormat.get_all():
        return f'Unknown report format {report_format_str}', 400

    report_format = ReportFormat[report_format_str]

    settings = SettingsManager().settings

    report = ReportFactory().create(settings, report_format)

    for entity_factory in __entity_factories:
        if entity_factory.get_path_name() == entity:
            return report.generate(entity_factory.get_entity())

    return f'Entity not found {entity}', 404
