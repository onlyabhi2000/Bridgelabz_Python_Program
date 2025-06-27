import math
import pytest
import source.shapes as shapes




@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(2,4)



def test_area(my_rectangle):
    assert my_rectangle.area() == 2*4


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2*(2+4)






# def test_area():
#     rectangle = shapes.Rectangle(2,4)
#     assert rectangle.area() == 2 *4


# def test_perimeter():
#     rectangle = shapes.Rectangle( 5,5)
#     assert rectangle.perimeter() == 2*(5+5)