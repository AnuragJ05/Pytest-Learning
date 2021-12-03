import pytest

@pytest.mark.xfail
def test_greater_than():
    num=10
    assert num>50

@pytest.mark.xfail
def test_less_than():
    num=10
    assert num<50

@pytest.mark.skip
def test_less_than_equal_to():
    num=10
    assert num<=50

@pytest.mark.skipif(25>0,reason='skip as 25>0')
def test_skip_if():
    assert 25 < 0