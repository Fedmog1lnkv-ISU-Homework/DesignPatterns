from abc import ABC, abstractmethod

from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.enums.report_format import ReportFormat
from src.core.exceptions.validation_exception import TypeValidationException


class AbstractReport(ABC):
    __format: ReportFormat = ReportFormat.CSV
    __result: str = ""

    """
    Сформировать
    """

    @abstractmethod
    def generate(self, data: list):
        pass

    """
    Тип формата
    """

    @property
    @abstractmethod
    def format(self) -> ReportFormat:
        return self.__format

    """
    Результат формирования отчета
    """

    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, value: str):
        if not isinstance(value, str):
            raise TypeValidationException(value, str)
        self.__result = value

    def _get_list_properties(self, obj: list) -> list[dict]:
        return [self._get_properties(item) for item in obj]

    def _get_properties(self, obj) -> dict:
        props = self._extract_properties(obj)

        if isinstance(obj, AbstractEntity):
            props['unique_code'] = obj.unique_code

        props = self._process_nested_properties(props)

        return props

    def _extract_properties(self, obj) -> dict:
        return {
            key: getattr(obj, key)
            for key, value in obj.__class__.__dict__.items()
            if isinstance(value, property)
        }

    def _process_nested_properties(self, props: dict) -> dict:
        for key, value in props.items():
            if isinstance(value, list):
                props[key] = self._get_list_properties(value)
            elif hasattr(value, '__dict__'):
                props[key] = self._get_properties(value)
        return props

    def _flatten_dict(self, d: dict, parent_key: str = '', sep: str = '.') -> dict:
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items
