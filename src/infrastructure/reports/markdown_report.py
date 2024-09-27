from src.core.enums.report_format import ReportFormat
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class MarkdownReport(AbstractReport):
    @property
    def format(self) -> ReportFormat:
        return ReportFormat.MARKDOWN

    def generate(self, data: list) -> str:
        if not data:
            return ""

        markdown_lines = []
        data_properties = self._get_list_properties(data)
        class_name = data[0].__class__.__name__
        flat_dicts = [self._flatten_dict(item) for item in data_properties]

        for index, item_properties in enumerate(flat_dicts, 1):
            markdown_lines.append(f"## {class_name} {index}\n")
            markdown_lines.extend([f"**{key}**: {value}" for key, value in item_properties.items()])
            markdown_lines.append("\n---\n")

        return "\n".join(markdown_lines)
