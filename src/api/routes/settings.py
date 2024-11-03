from flask import Blueprint, request

from src.core.services.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.services.settings_manager import SettingsManager
from src.core.services.store_service import StoreManager
from src.infrastructure.serializers.json_serializer import JsonSerializer

settings_blueprint = Blueprint('/api/settings', __name__, url_prefix='/api/settings')

settings_manager = SettingsManager()

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
