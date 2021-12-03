import pytest


@pytest.mark.parametrize("check1,check2",[(1,2),(2,3),(4,5)])
class TestPractice:

    @pytest.mark.parametrize("name",["Anurag","Anurag Jain"])
    def test_name_check(self,name,check1,check2):
        assert "Anurag" in name and check1 < check2

    @pytest.mark.checkNum
    def test_compare_prarmeter(self,check1,check2):
        assert check1 < check2

    @pytest.mark.xfail
    def test_compare_xfail_prarmeter(self,check1,check2):
        assert check1 > check2