from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.enums.report_format import ReportFormat
from src.core.exceptions.validation_exception import TypeValidationException, LengthValidationException
from src.infrastructure.reports.csv_report import CsvReport
from src.infrastructure.reports.json_report import JsonReport
from src.infrastructure.reports.markdown_report import MarkdownReport
from src.infrastructure.reports.rtf_report import RtfReport
from src.infrastructure.reports.xml_report import XmlReport


class Settings(AbstractEntity):
    """
    Модель настроек.
    """
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bic: str = ""
    __name: str = ""
    __type_of_ownership: str = ""
    __default_report_format: ReportFormat = ReportFormat.CSV
    __report_map: dict[ReportFormat, type] = {
        ReportFormat.CSV: CsvReport,
        ReportFormat.MARKDOWN: MarkdownReport,
        ReportFormat.JSON: JsonReport,
        ReportFormat.XML: XmlReport,
        ReportFormat.RTF: RtfReport
    }

    def __str__(self):
        return (f"inn={self.inn} \n"
                f"account={self.account} \n"
                f"correspondent_account={self.correspondent_account} \n"
                f"bic={self.bic} \n"
                f"name={self.name} \n"
                f"type_of_ownership={self.type_of_ownership}")

    @property
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, new_inn) -> None:
        if not isinstance(new_inn, str):
            raise TypeValidationException(new_inn, str)
        if len(new_inn) != 12:
            raise LengthValidationException(new_inn, 12)

        self.__inn = new_inn

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, new_account) -> None:
        if not isinstance(new_account, str):
            raise TypeValidationException(new_account, str)
        if len(new_account) != 11:
            raise LengthValidationException(new_account, 11)

        self.__account = new_account

    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, new_correspondent_account) -> None:
        if not isinstance(new_correspondent_account, str):
            raise TypeValidationException(new_correspondent_account, str)
        if len(new_correspondent_account) != 11:
            raise LengthValidationException(new_correspondent_account, 11)

        self.__correspondent_account = new_correspondent_account

    @property
    def bic(self) -> str:
        return self.__bic

    @bic.setter
    def bic(self, new_bic) -> None:
        if not isinstance(new_bic, str):
            raise TypeValidationException(new_bic, str)
        if len(new_bic) != 9:
            raise LengthValidationException(new_bic, 9)

        self.__bic = new_bic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        if not isinstance(new_name, str):
            raise TypeValidationException(new_name, str)
        self.__name = new_name

    @property
    def type_of_ownership(self) -> str:
        return self.__type_of_ownership

    @type_of_ownership.setter
    def type_of_ownership(self, new_type_of_ownership) -> None:
        if not isinstance(new_type_of_ownership, str):
            raise TypeValidationException(new_type_of_ownership, str)
        if len(new_type_of_ownership) != 5:
            raise LengthValidationException(new_type_of_ownership, 5)
        self.__type_of_ownership = new_type_of_ownership

    @property
    def default_report_format(self) -> ReportFormat:
        return self.__default_report_format

    @default_report_format.setter
    def default_report_format(self, value: ReportFormat):
        if not isinstance(value, ReportFormat):
            raise TypeValidationException(value, ReportFormat)
        self.__default_report_format = value

    @property
    def report_map(self) -> dict[ReportFormat, type]:
        return self.__report_map

    def to_json(self) -> dict:
        """
        Преобразовать настройки в JSON.
        """
        return {
            "inn": self.inn,
            "account": self.account,
            "correspondent_account": self.correspondent_account,
            "bic": self.bic,
            "name": self.name,
            "type_of_ownership": self.type_of_ownership
        }

    def set_compare_mode(self, other) -> bool:
        return super().set_compare_mode(other)