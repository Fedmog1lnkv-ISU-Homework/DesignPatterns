import json
import os
import sys

from src.core.models.settings import Settings


class SettingsRepository:
    """
    Репозиторий для управления настройками
    """

    def __init__(self, file_name: str):
        self._file_name = file_name

    def _load(self) -> Settings:
        try:
            project_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
            full_name = os.path.join(project_directory, self._file_name)

            with open(full_name, 'r', encoding="utf-8") as stream:
                data = json.load(stream)
                settings = Settings()

                fields = [attr for attr in dir(settings) if not attr.startswith("_")]

                for field in fields:
                    if field in data:
                        value = data[field]
                        setattr(settings, field, value)

                return settings

        except FileNotFoundError:
            print(f"Файл {self._file_name} не найден.")
            return Settings()

        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self._file_name}.")
            return Settings()

    def _save(self, settings: Settings) -> None:
        """
        Сохранить настройки в файл
        """
        try:
            full_name = f"{os.curdir}{os.sep}{self._file_name}"

            with open(full_name, 'w') as stream:
                json.dump(settings.to_json(), stream, indent=4)

        except IOError as e:
            print(f"Ошибка записи в файл {self._file_name}: {e}")

    def get_settings(self) -> Settings:
        """
        Получить настройки
        """
        return self._load()

    def save_settings(self, settings: Settings) -> None:
        """
        Сохранить настройки
        """
        self._save(settings)
