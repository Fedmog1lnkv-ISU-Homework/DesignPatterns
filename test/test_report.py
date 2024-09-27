import os

from src.core.enums.report_format import ReportFormat
from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.unit_model import UnitModel
from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager
from src.infrastructure.data_sources.recipes_data_source import RecipesDataSource
from src.infrastructure.factory.report_factory import ReportFactory


def test_nomenclature_report():
    group = NomenclatureGroup.create_group()
    unit_base = UnitModel("грамм", 1.0)
    unit = UnitModel("килограмм", 1000.0, unit_base)
    n1 = Nomenclature("name1", group, unit)
    n2 = Nomenclature("name2", group, unit)

    settings_manager = SettingsManager(os.path.join("new_test_settings.json"))
    settings = settings_manager.settings

    factory = ReportFactory()

    for value in ReportFormat.__members__.values():
        report = factory.create(settings, value)
        res = report.generate([n1, n2])
        with open(f'reports/nomenclature/report.{str(report.format.name).lower()}', 'w+', encoding="UTF-8") as file:
            file.write(res)


def test_reciep_report():
    data_source = RecipesDataSource()
    StartManager()
    recieps = data_source.get_all()

    settings_manager = SettingsManager(os.path.join("new_test_settings.json"))
    settings = settings_manager.settings

    factory = ReportFactory()

    for value in ReportFormat.__members__.values():
        report = factory.create(settings, value)
        res = report.generate(recieps)
        with open(f'reports/reciept/report.{str(report.format.name).lower()}', 'w+', encoding="UTF-8") as file:
            file.write(res)
