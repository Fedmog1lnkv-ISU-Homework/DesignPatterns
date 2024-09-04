from src.core.services.settings_manager import SettingsManager

test_dict = {
    "inn": "123456789012",  # 12 символов
    "account": "40702810123",  # 11 символов
    "correspondent_account": "38104000000",  # 11 символов
    "bic": "044525225",  # 9 символов
    "name": "Hello world",  # n символов
    "type_of_ownership": "hello"  # 5 символов
}

if __name__ == "__main__":
    manager = SettingsManager()
    print(f"start settings:\n{manager.settings}")

    manager2 = SettingsManager()
    manager2.settings.name = "ООО Рога и Копыта 2.0"
    print()
    print(f"final settings:\n{manager.settings}")

    manager_from_dict = SettingsManager(settings_dict=test_dict)
    print()
    print(f"from dict settings:\n{manager_from_dict.settings}")
