import pytest
from source import myfunc as mf
import time

###########  Function based tests  ###########
def test_add():
    result = mf.add(4,5)

    assert result == 9


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        mf.divide(10, 0)


def test_divide():
    result = mf.divide(10,2)
    assert result == 5

def test_add_string():
    result = mf.add("i like " , "burger")
    assert result == "i like burger"

###############################  parametrized and mark ###########################
####  marking  ####
@pytest.mark.slow
def test_slowtest():
    time.sleep(5)
    result = mf.divide(10,2)
    assert result == 5


@pytest.mark.skip(reason="this is currently broken")
def test_addtwo():
    assert mf.add(1,2)==3


@pytest.mark.xfail(reason="we cant divide a no with 0 , it will no work")
def test_dividezero():
    assert mf.divide(10,0)


#####  parametrized  #####

