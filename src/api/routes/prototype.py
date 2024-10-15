from src.core.services.prototype import PrototypeService
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.serializers.json_serializer import JsonSerializer
from flask import Blueprint, request

from src.api.routes.entity_factory.nomenclature_entity_factory import NomenclatureEntityFactory
from src.api.routes.entity_factory.nomenclature_group_entity_factory import NomenclatureGroupEntityFactory
from src.api.routes.entity_factory.recipe_entity_factory import RecipeEntityFactory
from src.api.routes.entity_factory.unit_entity_factory import UnitEntityFactory

__entity_factories = [
    NomenclatureEntityFactory(),
    RecipeEntityFactory(),
    UnitEntityFactory(),
    NomenclatureGroupEntityFactory()
]

prototype_service = PrototypeService()
json_serializer = JsonSerializer()

prototype_blueprint = Blueprint('/api/prototype', __name__, url_prefix='/api/prototype')

@prototype_blueprint.route('/<entity>', methods=['POST'])
def get_by_entity(entity):
    filters_data = request.json
    
    filters = json_serializer.deserialize_from_dict(filters_data, FilterItem)

    data = []

    for entity_factory in __entity_factories:
        if entity_factory.get_path_name() == entity:
            data = entity_factory.get_entity()
    
    return json_serializer.serialize_to_dict(prototype_service.get_by_filters(data, filters))
    
    
    