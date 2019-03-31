
import mathlib
import pytest

@pytest.mark.parametrize("test_input,expected_output",
                         [
                             (5,25),
                                 (9,81),
                                 (10,100)
                         ])
def test_calc_square(test_input,expected_output):
    result = mathlib.calc_square(5)
    assert result == 25

