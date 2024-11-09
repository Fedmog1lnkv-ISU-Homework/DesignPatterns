
from src.core.models.nomenclature_model import Nomenclature
from src.core.services.dto.create_nomenclature import CreateNomenclatureDTO
from src.core.services.dto.store_turnover_dto import StoreTurnoverDTO
from src.core.services.dto.update_nomenclature import UpdateNomenclatureDTO
from src.core.services.nomenclature import NomenclatureManager
from src.core.services.recipe_manager import RecipeManager
from src.core.services.store_service import StoreManager
from src.infrastructure.serializers.json_serializer import JsonSerializer
from flask import Blueprint, request

store_service = StoreManager()
json_serializer = JsonSerializer()

nomenclature_blueprint = Blueprint('/api/nomenclature', __name__, url_prefix='/api/nomenclature')

nomenclature_manager = NomenclatureManager()


@nomenclature_blueprint.route('/<id>', methods=['GET'])
def get_nomenclature(id):
    result = nomenclature_manager.get_by_id(id)

    return json_serializer.serialize_to_dict(result)

@nomenclature_blueprint.route('/', methods=['PUT'])
def create_nomenclature():
    data = request.json

    dto = json_serializer.deserialize_from_dict(data, CreateNomenclatureDTO)

    result = nomenclature_manager.create(dto)

    return json_serializer.serialize_to_dict(result)

@nomenclature_blueprint.route('/<id>', methods=['PATCH'])
def update_nomenclature(id):
    data = request.json

    dto = json_serializer.deserialize_from_dict(data, UpdateNomenclatureDTO)
    
    dto.id = id

    result = nomenclature_manager.update(dto)

    return json_serializer.serialize_to_dict(result)

@nomenclature_blueprint.route('/<id>', methods=['DELETE'])
def delete_nomenclature(id):
    result = nomenclature_manager.delete(id)

    return json_serializer.serialize_to_dict(result)