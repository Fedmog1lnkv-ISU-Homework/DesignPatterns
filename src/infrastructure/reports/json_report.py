import json

from src.core.enums.report_format import ReportFormat
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class JsonReport(AbstractReport):
    @property
    def format(self) -> ReportFormat:
        return ReportFormat.JSON

    def generate(self, data: list):
        if not data:
            return ""
        
        data = self._get_list_properties(data)
        return json.dumps(data, indent=4, sort_keys=True, default=str, ensure_ascii=False)
