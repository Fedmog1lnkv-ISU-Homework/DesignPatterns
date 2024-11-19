import json
import os

from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager

settings_manager = SettingsManager(os.path.join("settings.json"))
start_manager = StartManager()

def test_all_data_to_json():

    data = start_manager.all_data_to_json()

    entity_names = ["storehouse", "store_transaction", "nomenclature", "nomenclature_group", "recipe", "unit"]

    for entity_name in entity_names:
        assert len(data[entity_name]) > 0

def test_dump_data():

    start_manager.dump_data()

    filename = settings_manager.settings.dump_path

    data_from_dump = []

    full_name = f"{os.curdir}{os.sep}{filename}"
    with open(full_name, 'r', encoding='utf-8') as stream:
        data_from_dump = json.load(stream)

    data_to_dump = start_manager.all_data_to_json()

    assert len(data_from_dump) == len(data_to_dump)
    assert str(data_from_dump) == str(data_to_dump)




