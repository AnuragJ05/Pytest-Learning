import pytest

@pytest.mark.parametrize("num,output",[(1,5),(5,10),(3,15)])
def test_multiple_of_5_check(num,output):
    assert num * 5 == output