# 5. Flight Booking System
# Scenario: Simulate a basic flight booking system where users can search flights, book them,
# and view booking details.
# Problem Requirements:
# ● Use Array to store available flight data.
# ● Store user bookings in a List.
# ● Use String operations to allow case-insensitive flight search.
# ● Use methods for searching, booking, and displaying bookings.



class Flight:
    def __init__(self, number, origin, destination, seats):
        self.number = number
        self.origin = origin
        self.destination = destination
        self.seats = seats

class BookingSystem:
    def __init__(self):
        self.flights = [
            Flight("A", "Dhanbad", "Chennai", 3),
            Flight("B", "Ranchi", "Bhutan", 2)
        ]
        self.bookings = []


    def search_flights(self, origin, destination):
        origin = origin.lower()
        destination = destination.lower()

        matching_flights = []
        for flight in self.flights:
            if flight.origin.lower() == origin and flight.destination.lower() == destination:
                matching_flights.append(flight)
        
        return matching_flights




def book_flight(self, name, flight_number):
    try:
        for f in self.flights:
            if f.number.lower() == flight_number.lower():
                if f.seats > 0:
                    f.seats -= 1
                    self.bookings.append((name, f.number))
                    print(f"{name} has booked flight {f.number}")
                    return
                else:
                    print("seTSe NOT available")
                    return
        print("no flights")
        
    except:
        print("error")


booking_obj1 = BookingSystem()
for f in booking_obj1.search_flights("Dhanbad", "Chennai"):
    print(f"from {f.number}: {f.origin} to {f.destination}, Seats: {f.seats}")

booking_obj1.book_flight("abhi", "A")
booking_obj1.show_bookings()







