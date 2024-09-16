from copy import deepcopy

import pytest

from src.core.exceptions.validation_exception import TypeValidationException
from src.core.models.unit_model import UnitModel
from src.core.models.unit_value import UnitValue


def test_convert():
    base_range = UnitModel("грамм", 1)
    new_range = UnitModel("кг", 1000, base_range)

    value = UnitValue(3, new_range)
    assert value.to_base() == UnitValue(3000, base_range)
    
    value = UnitValue.from_base(3000, new_range)
    assert value == UnitValue(3, new_range)

def test_validation():
    with pytest.raises(TypeValidationException):
        UnitModel('грамм', 'грамм')


def test_base_equals():
    u1 = UnitModel("грамм", 1)
    u2 = UnitModel("грамм", 1)

    assert u1 == u2


def test_base_no_equals():
    u1 = UnitModel("грамм", 1)
    u2 = deepcopy(u1)

    u2.name = 'кг'

    assert u1 != u2
