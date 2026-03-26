class Slot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.full = False
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.full = True

    def release(self):
        self.vehicle = None
        self.full = False
