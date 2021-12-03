import math
import  pytest

@pytest.mark.parametrize("num1,num2",[(5,5),(1,1),(2,4)])
class TestClass:
    def test_num_check(self,num1,num2):
        assert num1==num2

    def test_square_root_check(self,num1,num2):
        assert math.sqrt(num1) == math.sqrt(num2)

    def test_cube_check(self,num1,num2):
        assert num1**3 == num2**3

@pytest.mark.parametrize("name",["Anurag","Jain","Calsoft"])
class TestClass2:
    def test_name_check(self,name):
        assert name in "Anurag Jain"

