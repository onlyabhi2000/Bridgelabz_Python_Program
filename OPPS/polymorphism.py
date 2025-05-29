# polymorphism means the same function with the same name but different signatures and used in different ways and scenarios.
# The difference is primarily in the data types and number of arguments used in a function. 

class Shape():
    def area(self):
        raise NotImplementedError("Subclass shouod implement this")
    
class Square(Shape):
    def __init__(self , length , height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height
    

class Circle(Shape):
        def __init__(self , radius):
             self.radius = radius
        
        def area(self):
             return 3.14 *self.radius * self.radius
        
square_obj = Square(2,3)
print(square_obj.area())


circle_obj = Circle(5)
print(circle_obj.area())

print(circle_obj , square_obj)

