import  source.shapes as shapes
import pytest
import math

# from source.shapes import Circle



class TestCircle:



    def setup_method(self, method):
        """
        What's method in setup_method(self, method)?
        Pytest passes the actual test function object to the setup/teardown method.

        You can access its name using method.__name__, which helps for logging or debugging.
        """
        print(f"Setting up method {method}")
        self.circle = shapes.Circle(10)


    def teardown_method(self,method):
        print(f"Tearing down {method}")
        del self.circle




    def test_one(self):
        assert True


    def test_area(self):
        expected_area = 3.141592653589793 * 10 * 10 
        assert self.circle.area() == math.pi * self.circle.radius **2


    def perimeter(self):
        result = self.circle.perimeter()
        expected_value = 2 *  math.pi * self.circle.radius
        assert result == expected_value
        