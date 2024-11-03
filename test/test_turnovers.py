from datetime import datetime

from src.core.enums.filter_operation_type import FilterOperationType
from src.core.enums.trsndsction_type import TransactionType
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.store_transaction import StoreTransaction
from src.core.models.storehouse_model import StoreHouseModel
from src.core.models.unit_model import UnitModel
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager
from src.core.services.store_service import StoreManager
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.generators.start_store_transaction_generator import StoreTransactionGenerator


def test_store_generate():
    generator = StoreTransactionGenerator()
    items = generator.get_store_transactions()

    for item in items:
        assert isinstance(item, StoreTransaction)
        assert isinstance(item.nomenclature, Nomenclature)
        assert isinstance(item.storehouse, StoreHouseModel)
        assert isinstance(item.measure_unit, UnitModel)
        assert isinstance(item.count, float)
        assert isinstance(item.type, TransactionType)
        assert isinstance(item.date, datetime)


def test_store_turnover():
    StartManager()

    dto = StoreTurnoverDTO()
    dto.start_time = datetime.fromtimestamp(1729872000)
    dto.end_time = datetime.fromtimestamp(1729958400)

    filter_item = FilterItem()
    filter_item.key = "nomenclature.name"
    filter_item.value = "Сахар"
    filter_item.operation = FilterOperationType.EQUAL

    dto.filters = [filter_item]

    storage_service = StoreManager()
    res = storage_service.calculate_turnovers(dto)

    assert res is not None
    assert len(res) > 0

    for item in res:
        assert item.nomenclature.name == "Сахар"
        assert item.amount != 0

def test_store_turnover_calculated():
    StartManager()
    settings_manager = SettingsManager("settings.json")
    store_manager = StoreManager()

    update_date_block_dto = UpdateDateBlockDTO()

    update_date_block_dto.value = datetime.fromtimestamp(1729872000)

    settings_manager.update_date_block(update_date_block_dto)

    store_manager.init_store_turnovers_by_date_block()

    filter_nomenclature_name = FilterItem()
    filter_nomenclature_name.key = "nomenclature.name"
    filter_nomenclature_name.value = "Сахар"
    filter_nomenclature_name.operation = FilterOperationType.EQUAL

    filter_storehouse_name = FilterItem()
    filter_storehouse_name.key = "storehouse.name"
    filter_storehouse_name.value = "Main storehouse"
    filter_storehouse_name.operation = FilterOperationType.EQUAL

    dto = StoreTurnoverDTO()
    dto.end_time = datetime.fromtimestamp(1730303999)
    # dto.filters = [filter_nomenclature_name, filter_storehouse_name]

    start_time = datetime.now()
    res_1 = store_manager.get_turnovers(dto)
    end_time = datetime.now()

    print()
    print(f"Date block: {settings_manager.settings.date_block}, dto.end_date: {dto.end_time}, working time: {end_time - start_time}")

    update_date_block_dto.value = datetime.fromtimestamp(1730131199)

    store_manager.update_turnovers_by_date_block(update_date_block_dto.value)
    settings_manager.update_date_block(update_date_block_dto)

    start_time = datetime.now()
    res_2 = store_manager.get_turnovers(dto)
    end_time = datetime.now()

    print(
        f"Date block: {settings_manager.settings.date_block}, dto.end_date: {dto.end_time}, working time: {end_time - start_time}")

    assert res_1 is not None
    assert len(res_1) > 0

    assert len(res_1) == len(res_2)

    for item_1, item_2 in zip(res_1, res_2):
        assert item_1.nomenclature == item_2.nomenclature
        assert item_1.storehouse == item_2.storehouse
        assert item_1.unit == item_2.unit
        assert item_1.amount == item_2.amount



