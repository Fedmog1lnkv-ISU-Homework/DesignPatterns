from src.core.abstractions.abstract_manager import AbstractManager
from src.core.models.settings import Settings
from src.core.services.dto.update_date_block_dto import UpdateDateBlockDTO
from src.infrastructure.repositories.settings_repository import SettingsRepository


class SettingsManager(AbstractManager):
    """
    Менеджер настроек
    """
    _instance = None
    _file_name = None

    def __new__(cls, file_name: str = "settings.json", settings_dict: dict = None):
        if cls._instance is None or file_name != cls._file_name:
            cls._file_name = file_name
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance._repository = SettingsRepository(file_name)

            if settings_dict:
                cls._instance._settings = SettingsManager._from_dict(settings_dict)
            else:
                cls._instance._settings = cls._instance._repository.get_settings()
        return cls._instance

    @staticmethod
    def _from_dict(data: dict) -> Settings:
        """
        Создать объект Settings из словаря.
        """
        settings = Settings()
        fields = [attr for attr in dir(settings) if not attr.startswith("_")]

        for field in fields:
            field_lower = field.lower()
            if field_lower in data:
                value = data[field_lower]
                setattr(settings, field, value)

        return settings

    def update_date_block(self, dto: UpdateDateBlockDTO) -> None:
        if dto.value < self._settings.date_block:
            raise ValueError("Нельзя уменьшить дату блока")

        self._settings.date_block = dto.value

    def save_settings(self, file_name: str = "settings.json") -> None:
        self._repository.save_settings(self._settings)

    @property
    def settings(self) -> Settings:
        return self._settings

    @settings.setter
    def settings(self, value: Settings) -> None:
        self._settings = value
        self._repository.save_settings(value)
