from src.core.enums.report_format import ReportFormat
from src.core.models.settings import Settings
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class ReportFactory:

    @staticmethod
    def __create_internal(report_map: dict[ReportFormat, type], report_format: ReportFormat):
        result = report_map[report_format]
        return result()

    def create(self, settings: Settings, report_format: ReportFormat) -> AbstractReport:
        return self.__create_internal(settings.report_map, report_format)

    def create_default(self, settings: Settings):
        return self.__create_internal(settings.report_map, settings.default_report_format)
