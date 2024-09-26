from xml.etree.ElementTree import Element, tostring, SubElement

from src.core.enums.report_format import ReportFormat
from src.infrastructure.reports.abstractions.abstract_report import AbstractReport


class XmlReport(AbstractReport):
    @property
    def format(self) -> ReportFormat:
        return ReportFormat.XML

    def generate(self, data: list) -> str:
        if not data:
            return ""

        root = Element("root")
        class_name = data[0].__class__.__name__

        for i, item in enumerate(self._get_list_properties(data), 1):
            object_element = SubElement(root, f"{class_name}_{i}")
            self._build_xml_from_dict(item, object_element)

        return tostring(root, encoding='unicode', xml_declaration=True)

    def _build_xml_from_dict(self, data_dict: dict, parent: Element):
        for key, value in data_dict.items():
            child = SubElement(parent, key)
            if isinstance(value, dict):
                self._build_xml_from_dict(value, child)
            else:
                child.text = str(value)
