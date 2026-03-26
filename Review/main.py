from models.vehicle import Car, Bike
from models.parking_lot import ParkingLot

def main():
    lot = ParkingLot(5)

    car1 = Car("1111", "White")
    car2 = Car("2222", "Black")
    bike1 = Bike("3333", "Red")

    lot.park_vehicle(car1)
    lot.park_vehicle(car2)
    lot.park_vehicle(bike1)

    lot.remove_vehicle("1111")
    # lot.remove_vehicle("5555")
    lot.remove_vehicle("1111")
    lot.park_vehicle(Car("1111", "Silver"))

if __name__ == "__main__":
    main()
