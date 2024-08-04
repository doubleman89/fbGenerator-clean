import pytest

from generator.domain.unit import Unit
from tests.domain.entity_examples import units

len_units = len(units)

@pytest.mark.parametrize("iteration", range(len_units))
def test_unit_model_init(iteration ):
    unit_dict = units[iteration]
    unit1 = Unit.from_dict(unit_dict)
    unit2 = Unit.from_dict(unit_dict)

    assert unit1.to_dict() == unit_dict
    assert unit1 == unit2

    