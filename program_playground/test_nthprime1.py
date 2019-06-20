
from nthprime1 import *
import pytest

def test_is_prime():

    assert is_prime(3) == True
    assert is_prime(97) == True
    assert is_prime(379) == True
    assert is_prime(997) == True
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(3.7) == False
    assert is_prime('Profun') == False

def test_next_prime():

    assert next_prime(3, 4) == 13
    assert next_prime(4, 2) == 7
    assert next_prime(0, 5) == 11
    # assert next_prime(3, 4) == 10
