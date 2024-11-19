from flask import Blueprint, request

from src.core.enums.event_type import EventType
from src.core.services.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.services.settings_manager import SettingsManager
from src.core.services.store_service import StoreManager
from src.di.manager import settings_manager
from src.di.observer_manager import observer_manager
from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.utils.observer.event import Event

settings_blueprint = Blueprint('/api/settings', __name__, url_prefix='/api/settings')

store_manager = StoreManager()

json_serializer = JsonSerializer()


@settings_blueprint.route('', methods=['GET'])
def get_settings():
    return settings_manager.settings.to_json()


@settings_blueprint.route('/date_block', methods=['POST'])
def update_date_block():
    filters_data = request.json

    dto = json_serializer.deserialize_from_dict(filters_data, UpdateDateBlockDTO)

    if dto.value < settings_manager.settings.date_block:
        return 'Date block cannot be less than current date block', 400

    store_manager.update_turnovers_by_date_block(dto.value)

    settings_manager.update_date_block(dto)
    settings_manager.save_settings()

    return settings_manager.settings.to_json()


@settings_blueprint.route('/dump', methods=['POST'])
def dump():

    event = Event()
    event.type = EventType.DUMP_DATA

    observer_manager.notify(event)
