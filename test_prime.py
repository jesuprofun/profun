import pytest 
from prime import *

def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(97) == True
    assert is_prime(1) == False
    assert is_prime(-10) == False
    assert is_prime(1000) == False
    
    with pytest.raises(TypeError):
        is_prime(None)
    
    with pytest.raises(TypeError):
        is_prime(21.234)

    with pytest.raises(TypeError):
        is_prime("profun")


