class Person:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}"


class AddressBook:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        if not self.is_duplicate(person):
            self.people.append(person)
            print("Person added successfully.")
        else:
            print("Duplicate person found, cant add")

    def is_duplicate(self, person):
        for p in self.people:
            if p.first_name.lower() == person.first_name.lower() and p.last_name.lower() == person.last_name.lower():
                return True
        return False

    def edit_person(self, first_name, last_name, **kwargs):
        for p in self.people:
            if p.first_name.lower() == first_name.lower() and p.last_name.lower() == last_name.lower():
                for key, value in kwargs.items():
                    if hasattr(p, key):
                        setattr(p, key, value)
                print("Person details updated.")
                return
        print("Person not found.")

    def delete_person(self, first_name, last_name):
        for p in self.people:
            if p.first_name.lower() == first_name.lower() and p.last_name.lower() == last_name.lower():
                self.people.remove(p)
                print("Person removed.")
                return
        print("Person not found.")

    def sort_people(self, by="first_name"):
        self.people.sort(key=lambda x: getattr(x, by))
        print(f"Sorted by {by}.")

    def search(self, **kwargs):
        results = self.people
        for key, value in kwargs.items():
            results = [p for p in results if getattr(p, key).lower() == value.lower()]
        return results

    def display(self):
        for p in self.people:
            print(p)



ab = AddressBook()

p1 = Person("Abhi", "SmiSharmath", "wasepur", "Dhanbad", "Jharkhand", "62704", "9876567894")
p2 = Person("Dogesh", "Ji", "kanke", "Aurangabad", "Bihar", "62705", "9875678")

ab.add_person(p1)
ab.add_person(p2)
##shoild get dublicate
ab.add_person(p1)  
print("get - -->All People:")
ab.display()

print("after Sorting by First Name:")
ab.sort_people("first_name")
ab.display()

print("Search---->:")
results = ab.search(address="wasepur")
for r in results:
    print(r)
