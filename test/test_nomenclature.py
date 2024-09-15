from copy import deepcopy

from src.core.models.nomenclature_group_model import NomenclatureGroup
from src.core.models.nomenclature_model import Nomenclature
from src.core.models.unit_model import UnitModel

n1_group = NomenclatureGroup.create_group()
n1_unit = UnitModel("грамм", 1.0)
n1 = Nomenclature("name1", n1_group.unique_code, n1_unit)

n2_group = NomenclatureGroup.create_group()
n2_unit = UnitModel("грамм", 1.0)
n2 = Nomenclature("name2", n2_group.unique_code, n2_unit)

def test_other_uuid_for_instances():
    assert n1.unique_code != n2.unique_code


def test_base_not_equals():
    n1 = Nomenclature("name1", n1_group.unique_code, n1_unit)
    n3 = Nomenclature("name1", n1_group.unique_code, n1_unit)
    assert n1 != n3


def test_base_equals():
    n1.name = "this"
    n3 = deepcopy(n1)
    n3.name = ''
    assert n1 == n3
