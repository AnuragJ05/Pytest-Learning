import pytest

@pytest.fixture
def input_value():
    num = 25
    return num

'''
(The tests will look for fixture in the same file. As the fixture is not found in the file,
 it will check for fixture in conftest.py file. On finding it, the fixture method is invoked 
 and the result is returned to the input argument of the test.)
'''