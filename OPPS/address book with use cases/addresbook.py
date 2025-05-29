from person import Person

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def __str__(self):
        if not self.contacts:
            return f"AddressBook '{self.name}' has no contacts."
        return f"AddressBook '{self.name}' with {len(self.contacts)} contact:\n" + "\n".join(str(contact) for contact in self.contacts)

    def __repr__(self):
        return self.__str__()

    ##method to aff contact
    def add_contact(self, person):
        for contact in self.contacts:
            if contact.first_name.lower() == person.first_name.lower() and contact.last_name.lower() == person.last_name.lower():
                print("Contact already exists.")
                return
        self.contacts.append(person)
        print("Contact added.")

    ## method to delete an contact
    def delete_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

    ##method to edit an conytact
    def edit_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                new_address = input("New address: ").strip()
                new_city = input("New city: ").strip()
                new_state = input("New Satte: ").strip()
                new_zip = input("New zip Code: ").strip()
                new_phone = input("New phone: ").strip()
                new_email = input("New email: ").strip()

                if new_address:
                    contact.address = new_address
                if new_city:
                    contact.city = new_city
                if new_state:
                    contact.state = new_state
                if new_zip:
                    contact.zip_code = new_zip
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email

                print("Contact updated.")
                return
        print("Contact not found.")

    def search_contact(self, keyword):
        found = False
        for contact in self.contacts:
            if keyword.lower() in contact.first_name.lower() or keyword.lower() in contact.email.lower():
                print(contact)
                found = True
        if not found:
            print("No contact found with these details")

    def search_in_city(self, city):
        return [contact for contact in self.contacts if contact.city.lower() == city.lower()]

    def search_in_state(self, state):
        return [contact for contact in self.contacts if contact.state.lower() == state.lower()]

    def count_by_city(self):
        city_counts = {}
        for contact in self.contacts:
            city = contact.city
            city_counts[city] = city_counts.get(city, 0) + 1
        return city_counts

    def count_by_state(self):
        state_counts = {}
        for contact in self.contacts:
            state = contact.state
            state_counts[state] = state_counts.get(state, 0) + 1
        return state_counts

    def sort_by_name(self):
        return sorted(self.contacts, key=lambda x: (x.first_name.lower(), x.last_name.lower()))

    def sort_by_city(self):
        return sorted(self.contacts, key=lambda x: x.city.lower())

    def sort_by_state(self):
        return sorted(self.contacts, key=lambda x: x.state.lower())

    def sort_by_zip(self):
        return sorted(self.contacts, key=lambda x: x.zip_code)

    def show_all_contacts(self):
        if not self.contacts:
            print("No contacts-->")
        for contact in self.contacts:
            print(contact)
