from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_number, color):
        self.vehicle_number = vehicle_number
        self.color = color

    @abstractmethod
    def get_type(self):
        pass



    

class Car(Vehicle):
    def get_type(self):
        return "car"

class Bike(Vehicle):
    def get_type(self):
        return "biike"
