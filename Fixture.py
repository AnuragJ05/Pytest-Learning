import math
import pytest

@pytest.fixture
def input_value():
    num = 25
    return num

@pytest.mark.num
def testnum_check(input_value):
    assert input_value == 25

@pytest.mark.num
def test_square_check(input_value):
    assert math.sqrt(input_value) == 5
