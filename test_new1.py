from new1 import *

def test_calc_total():
    result = calc_total(2, 3)
    assert result == 5

def test_calc_mul():
    ans = calc_mul(10, 2)
    assert ans == 20