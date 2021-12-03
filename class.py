import math

class TestClass:
    def test_num_check(self):
        num=25
        assert num==25

    def test_square_check(self):
        num=25
        assert math.sqrt(num) == 5

    def test_cube_check(self):
        num=25
        assert 25 == 5*5*5


