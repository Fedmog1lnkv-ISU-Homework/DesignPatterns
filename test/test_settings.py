import os

from src.core.services.settings_manager import SettingsManager

test_dict = {
    "inn": "123456789012",  # 12 символов
    "account": "40702810123",  # 11 символов
    "correspondent_account": "38104000000",  # 11 символов (поправил на 11 для соответствия)
    "bic": "044525225",  # 9 символов
    "name": "Hello world",  # n символов
    "type_of_ownership": "hello"  # 5 символов
}


def test_is_singleton():
    """
    Проверка на 1 экземпляр класса
    """
    settings_manager1 = SettingsManager(settings_dict=test_dict)
    settings1 = settings_manager1.settings

    settings_manager2 = SettingsManager(settings_dict=test_dict)
    settings2 = settings_manager2.settings
    assert settings1 is settings2
    assert settings_manager1 is settings_manager2
    assert settings_manager1 == settings_manager2


def test_load_settings_from_json_from_another_dir():
    """
    Тест загрузки данных из json файла с другим местоположением
    """
    settings_manager = SettingsManager(os.path.join("new_test_settings.json"))

    settings = settings_manager.settings
    assert settings.inn == "122820179885"
    assert settings.account == "74070284010"
    assert settings.correspondent_account == "81022301045"
    assert settings.bic == "225044525"
    assert settings.name == "ООО Рога и Копыта from TEST"
    assert settings.type_of_ownership == "TESTC"
