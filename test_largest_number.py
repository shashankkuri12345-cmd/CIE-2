from largest_number import largest

def test_largest():
    assert largest(10,20,30) == 30

def test_largest_zero():
    assert largest(0,0,0) == 0