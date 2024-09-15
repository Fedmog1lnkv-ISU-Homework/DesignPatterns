from src.core.abstractions.abstract_entity import AbstractEntity
from src.core.models.settings import Settings


class OrganizationModel(AbstractEntity):
    """
    Модель организации с ИНН, БИК, Счетом и Формой собственности
    """

    def __init__(self, settings: Settings):
        super().__init__()
        self.__inn = settings.inn
        self.__account = settings.account
        self.__correspondent_account = settings.correspondent_account
        self.__bic = settings.bic
        self.__name = settings.name
        self.__type_of_ownership = settings.type_of_ownership

    @property
    def inn(self) -> str:
        return self.__inn

    @property
    def bic(self) -> str:
        return self.__bic

    @property
    def account(self) -> str:
        return self.__account

    @property
    def org_type(self) -> str:
        return self.__type_of_ownership

    @property
    def name(self) -> str:
        return self.__name

    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account

    def set_compare_mode(self, other):
        return self.inn == other.inn
