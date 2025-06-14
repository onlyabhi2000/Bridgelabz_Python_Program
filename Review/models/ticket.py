from datetime import datetime

class ParkingTicket:
    ticket_count = 1 

    def __init__(self, vehicle, slot_id):
        self.ticket_id = ParkingTicket.ticket_count
        ParkingTicket.ticket_count += 1

        self.vehicle = vehicle
        self.slot_id = slot_id
        self.entry_time = datetime.now()





    def __str__(self):
        return (
            f"ticket id : {self.ticket_id}"
            f"slot: {self.slot_id}"
            f"Vehicle: {self.vehicle.vehicle_number}"
        )
