
import ascending

def test_ascending():
    assert ascending.ascending([32,68,6,89,6,86],6) == [6,6,32,68,86,89]
    assert ascending.ascending([-76,68,234,-7,678,0], 6) == [-76,-7,0,68,234,678]