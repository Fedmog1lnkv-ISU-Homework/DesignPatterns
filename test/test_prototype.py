import pytest

from src.core.enums.filter_operation_type import FilterOperationType
from src.infrastructure.filter.item.item import FilterItem
from src.infrastructure.filter.operation_mapper.operation_mapper import FilterOperationTypeMapper
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.infrastructure.prototype.abstract.abstract import AbstractPrototype

@pytest.fixture
def nomenclature_generator():
    return StartNomenclatureGenerator()

@pytest.fixture
def mapper():
    return FilterOperationTypeMapper()

@pytest.fixture
def first_nomenclature(nomenclature_generator):
    return nomenclature_generator.get_nomenclatures()[0]

def test_like(nomenclature_generator, mapper):
    filter_nomenclature = FilterItem()
    filter_nomenclature.key = "name"
    filter_nomenclature.value = "мука"
    filter_nomenclature.operation = FilterOperationType.LIKE

    prot = AbstractPrototype(nomenclature_generator.get_nomenclatures(), mapper)
    res = prot.create([filter_nomenclature])

    assert len(res) > 0
    for item in res:
        assert "мука" in item.name

def test_equal(first_nomenclature, nomenclature_generator, mapper):
    filter_nomenclature = FilterItem()
    filter_nomenclature.key = "name"
    filter_nomenclature.value = first_nomenclature.name
    filter_nomenclature.operation = FilterOperationType.EQUAL

    prot = AbstractPrototype(nomenclature_generator.get_nomenclatures(), mapper)
    res = prot.create([filter_nomenclature])

    assert len(res) == 1
    assert res[0] == first_nomenclature
