
import prime

def test_is_prime():
    assert prime.is_prime(3) == True
    assert prime.is_prime(1) == False
    assert prime.is_prime(-10) == False
    assert prime.is_prime(1000) == False
    #assert prime.is_prime("profun") == False
    assert prime.is_prime(0) == False
    #assert prime.is_prime(1.231) == False
