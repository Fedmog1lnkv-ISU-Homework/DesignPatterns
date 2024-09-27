from src.core.enums.report_format import ReportFormat
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class RtfReport(AbstractReport):
    @property
    def format(self) -> ReportFormat:
        return ReportFormat.RTF

    def generate(self, data: list) -> str:
        if not data:
            return ""

        rtf_header = [
            r"{\rtf1\ansi\deff0",
            r"{\fonttbl{\f0\fswiss Helvetica;}}",
            r"\f0\fs24"
        ]

        rtf_body = []
        data_properties = self._get_list_properties(data)
        class_name = data[0].__class__.__name__

        for index, item_properties in enumerate([self._flatten_dict(item) for item in data_properties], 1):
            rtf_body.append(f"\\b {class_name} {index}:\\b0 \\par")
            rtf_body.extend([f"\\b {key}:\\b0 {value} \\par" for key, value in item_properties.items()])
            rtf_body.append("\\par")

        rtf_content = rtf_header + rtf_body + ["}"]
        return ''.join(rtf_content)
