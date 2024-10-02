from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.recipe import Recipe
from src.core.models.unit_model import UnitModel
from src.core.models.unit_value import UnitValue
from src.core.services.start_manager import StartManager
from src.infrastructure.data_sources.recipes_data_source import RecipesDataSource
from src.infrastructure.serializers.json_serializer import JsonSerializer


def test_nomenclature():
    group = NomenclatureGroup.create_group()
    unit_base = UnitModel("грамм", 1.0)
    unit = UnitModel("килограмм", 1000.0, unit_base)
    n = Nomenclature("name1", group, unit)

    serializer = JsonSerializer()

    n_json = serializer.serialize(n)
    n_deserialized = serializer.deserialize(n_json, Nomenclature)

    assert n == n_deserialized
    assert n.name == n_deserialized.name
    assert n.units == n_deserialized.units
    assert n.group == n_deserialized.group


def test_unit_value():
    base_range = UnitModel("грамм", 1)
    new_range = UnitModel("кг", 1000, base_range)
    value = UnitValue(3, new_range)

    serializer = JsonSerializer()
    value_json = serializer.serialize(value)
    value_deserialized = serializer.deserialize(value_json, UnitValue)

    assert value == value_deserialized
    assert value.unit == value_deserialized.unit
    assert value.value == value_deserialized.value
    

def test_reciept():
    data_source = RecipesDataSource()
    StartManager()
    recieps = data_source.get_all()

    serializer = JsonSerializer()
    recipes_json = serializer.serialize(recieps)
    recipes_deserialized = serializer.deserialize(recipes_json, Recipe)

    assert recieps == recipes_deserialized
