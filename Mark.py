import math
import pytest

@pytest.mark.num
def testnum_check():
    num=25
    assert num==25
@pytest.mark.num
def test_square_check():
    num=25
    assert math.sqrt(num) == 6
@pytest.mark.str
def test_string_check():
    name="Anurag"
    assert name == "Anurag"

'''
pytest -k square .\Mark.py
	(execute the tests containing a string in its name)

pytest -m num .\Mark.py
	(execute the tests with marker)
'''
