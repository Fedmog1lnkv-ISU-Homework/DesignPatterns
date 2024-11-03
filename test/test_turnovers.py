from datetime import datetime

from src.core.enums.filter_operation_type import FilterOperationType
from src.core.enums.trsndsction_type import TransactionType
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.store_transaction import StoreTransaction
from src.core.models.storehouse_model import StoreHouseModel
from src.core.models.unit_model import UnitModel
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
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
    dto.start_time = datetime.fromtimestamp(1729846800)
    dto.end_time = datetime.fromtimestamp(1729854000)

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
