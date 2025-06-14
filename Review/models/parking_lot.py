import heapq

from .slot import Slot
from .ticket import ParkingTicket

class ParkingLot:
    def __init__(self, total_slots):
        self.slots = []
        for i in range(1, total_slots + 1):
            slot = Slot(i)
            self.slots.append(slot)

        self.free_slots_heap = []
        for slot in self.slots:
            self.free_slots_heap.append(slot.slot_id)


        heapq.heapify(self.free_slots_heap)

        self.slot_map = {}
        for slot in self.slots:
            self.slot_map[slot.slot_id] = slot

        self.vehicle_slot_map = {}

        self.vehicle_ticket_map = {}


    def park_vehicle(self, vehicle):
        if not self.free_slots_heap:
            print("parking is full bow")
            return None



        slot_id = heapq.heappop(self.free_slots_heap)
        slot = self.slot_map[slot_id]
        slot.assign_vehicle(vehicle)

        self.vehicle_slot_map[vehicle.vehicle_number] = slot
        ticket = ParkingTicket(vehicle, slot_id)
        self.vehicle_ticket_map[vehicle.vehicle_number] = ticket

        print(f"vehiche parked at the {slot_id} slot")
        return ticket

    def remove_vehicle(self, vehicle_number):
        if vehicle_number not in self.vehicle_slot_map:
            print("no vehicle with this number")
            return

        slot = self.vehicle_slot_map.pop(vehicle_number)
        ticket = self.vehicle_ticket_map.pop(vehicle_number)

        slot.release()
        heapq.heappush(self.free_slots_heap, slot.slot_id)


        print(f" vwhicle {vehicle_number} removed .")
        print(f"Ticket Info:  {ticket}")
