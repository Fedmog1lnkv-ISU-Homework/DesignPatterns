from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.store_service import StoreManager
from src.infrastructure.serializers.json_serializer import JsonSerializer
from flask import Blueprint, request

store_service = StoreManager()
json_serializer = JsonSerializer()

store_blueprint = Blueprint('/api/store', __name__, url_prefix='/api/store')


@store_blueprint.route('/turnover', methods=['POST'])
def get_turnovers():
    filters_data = request.json

    dto = json_serializer.deserialize_from_dict(filters_data, StoreTurnoverDTO)

    result = store_service.get_turnovers(dto)

    return json_serializer.serialize_to_dict(result)