import pytest
from source import myfunc as mf
from source.myfunc import add
import time

def test_add():
    result = mf.add(4,5)

    assert result == 9


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        mf.divide(10, 0)


def test_divide():
    result = mf.divide(10,2)
    assert result == 5



### parametrized ###

@pytest.mark.parametrize("a ,b , expected_result" , [(2,4, 6),(1 ,9 , 10)])
def test_parametrized_add( a, b , expected_result):
    assert add(a, b) == expected_result