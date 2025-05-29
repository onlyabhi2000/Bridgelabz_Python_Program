# Abstraction is one of the important principles of object-oriented programming.
#  It refers to a programming approach by which only the relevant data about an object is exposed, hiding all the other details.
#  This approach helps in reducing the complexity and increasing the efficiency of application development.

##Note## --> there is no build in class in python to achieve Abstract class
# But can achiev suing a module class ABC

## Abstract class : Method tha has a declaration but does not have an implementaion
## Concete class : Normal method which conatins the implementation

### Note : we cant create the object of a Abstract class

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    ## different implementation for d/t class so abstract class
    def mileage(self):
        pass
    

    ## same implementaion for all classes so concrete method
    def color(self):
        print("white")


class Tata(Car):
    def mileage(self):
        print("Mileage is 25kmpl")



class Mahindra(Car):
    def mileage(self):
        print("Milege is 20kmpl")


##we cant create the object of a Abstract class
car_obj = Car()
print(car_obj)

tata_obj = Tata()
mahindra_obj = Mahindra()




    

