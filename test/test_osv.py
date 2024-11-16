import os
from datetime import datetime

from src.core.models.nomenclature_model import Nomenclature
from src.core.models.osv_model import OsvModel
from src.core.models.storehouse_model import StoreHouseModel
from src.core.services.dto.get_osv import GetOsvDTO
from src.core.services.osv_manager import OsvManager
from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager
from src.core.services.store_service import StoreManager


settings_manager = SettingsManager(os.path.join("settings.json"))
start_manager = StartManager()
store_manager = StoreManager()
osv_manager = OsvManager()

store_manager.init_store_turnovers_by_date_block()


def test_osv():

    dto = GetOsvDTO()

    dto.start_date = datetime.fromtimestamp(1729789200)
    dto.end_date = datetime.fromtimestamp(1730134800)

    data = osv_manager.get_by_dto(dto)

    assert len(data) > 0

    for item in data:
        assert isinstance(item, OsvModel)

        assert isinstance(item.end_date, datetime)
        assert isinstance(item.start_date, datetime)

        assert isinstance(item.start_amount, float)
        assert isinstance(item.end_amount, float)

        assert isinstance(item.storehouse, StoreHouseModel)
        assert isinstance(item.nomenclature, Nomenclature)
