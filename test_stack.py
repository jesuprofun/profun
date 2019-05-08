from stack import *
import pytest

def test_push():
    s = Stack(None, 4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    #s.push('Profun')

    assert len(s.container) == 4

    with pytest.raises(Exception):
        s.push(4)

def test_pop():
    s = Stack(None, 4)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    s.push('Profun')
    assert s.pop() == 'Profun'

    assert len(s.container) == 2