import math

def testnum_check():
    num=25
    assert num==26

def test_square_check():
    num=25
    assert math.sqrt(num) == 6

def test_cube_check():
    num=25
    assert 25 == 5*5*5


'''
pytest --maxfail  2 .\MaxFail.py
'''