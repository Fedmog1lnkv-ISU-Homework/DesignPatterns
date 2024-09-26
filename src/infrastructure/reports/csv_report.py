import csv
import io

from src.core.enums.report_format import ReportFormat
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class CsvReport(AbstractReport):
    @property
    def format(self) -> ReportFormat:
        return ReportFormat.CSV

    def generate(self, data: list) -> str:
        if not data:
            return ""

        data_properties = self._get_list_properties(data)
        flat_dicts = [self._flatten_dict(item) for item in data_properties]

        if not flat_dicts:
            return ""

        fieldnames = flat_dicts[0].keys()

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerows(flat_dicts)

        return output.getvalue()
