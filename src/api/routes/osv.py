from datetime import datetime

from flask import Blueprint, request

from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.core.services.dto.get_osv import GetOsvDTO
from src.core.services.osv_manager import OsvManager


json_serializer = JsonSerializer()

osv_blueprint = Blueprint('/api/osv', __name__, url_prefix='/api/osv')

osv_manager = OsvManager()


@osv_blueprint.route('', methods=['GET'])
def get():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    storehouse_id = request.args.get('storehouse_id')

    dto = GetOsvDTO()
    dto.start_date = datetime.fromtimestamp(int(start_date))
    dto.end_date = datetime.fromtimestamp(int(end_date))
    if storehouse_id is not None:
        dto.storehouse_id = storehouse_id

    result = osv_manager.get_by_dto(dto)

    return json_serializer.serialize_to_dict(result)

