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
    
def test_base_unit():
    gramm =  UnitModel("грамм", 1)
    killogram = UnitModel("кг", 1000, gramm)
    
    gramm_value = UnitValue(10, gramm)
    killogram_value = UnitValue(0.1, killogram)

    kilogramm_to_base = killogram_value.to_base()
    assert kilogramm_to_base.value == 100  # 0.1 кг = 100 грамм
    assert kilogramm_to_base.unit == gramm  # Базовая единица - грамм

    value_from_base = UnitValue.from_base(100, killogram)
    assert value_from_base.value == 0.1  # 100 грамм = 0.1 кг
    assert value_from_base.unit == killogram

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
