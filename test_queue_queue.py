from queue_queue import *
import pytest

def test_push():
    q = Queue(None, 4)
    q.push(1)
    q.push(-1)
    q.push(1.02)
    q.push("profun")

    assert len(q) == 4

def test_out():
    q = Queue(None, 4)
    q.push(1)
    q.push(-1)
    q.push(1.02)
    q.push("profun")
    
    assert q.out() == 1
    assert q.out() == -1
    assert q.out() == 1.02
    #assert q.out() == "profun"
 

    #assert len(q) == 0

def test_contains():
    q = Queue(None, 4)

    q.push(7)
    q.push(-1)
    q.push(1.02)
    q.push("profun")

    for arg in range(4):
        assert 7 in q