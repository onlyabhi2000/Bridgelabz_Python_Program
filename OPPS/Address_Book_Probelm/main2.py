class Person:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

    def __eq__(self, other):  
        return self.name == other.name and self.phone_number == other.phone_number and self.email == other.email
    
class AddressBook:
    def __init__(self):
        self.contacts = []  
    def add_contact(self, person):
        if person not in self.contacts:
            self.contacts.append(person)
            print("Contact added successfully.")
        else:
            print("Contact already exists.")

    def add_multiple_contacts(self, people):
        for person in people:
            self.add_contact(person)

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone
                contact.email = new_email
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone_number or keyword.lower() in contact.email:
                results.append(contact)
        if results:
            for result in results:
                print(result)
        else:
            print("No contacts found.")

    def sort_contacts(self, sort_by):
        if sort_by == "name":
            self.contacts.sort(key=lambda x: x.name)
        elif sort_by == "phone":
            self.contacts.sort(key=lambda x: x.phone_number)
        elif sort_by == "email":
            self.contacts.sort(key=lambda x: x.email)
        else:
            print("Invalid sorting criteria.")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("Address book is empty.")

    def duplicate_contact(self, name):
        duplicates = []
        for contact in self.contacts:
            if contact.name == name:
                duplicates.append(contact)
        if duplicates:
            print("Duplicate contacts found:")
            for duplicate in duplicates:
                print(duplicate)
        else:
            print("No duplicate contacts found.")




# Assuming the Person and AddressBook classes are already defined above

# Create an instance of AddressBook
address_book = AddressBook()

# Create some Person instances
person1 = Person("Alice Smith", "123-456-7890", "alice@example.com")
person2 = Person("Bob Johnson", "987-654-3210", "bob@example.com")
person3 = Person("Charlie Brown", "555-123-4567", "charlie@example.com")
duplicate_person = Person("Alice Smith", "123-456-7890", "alice@example.com")

# Add single contacts
print("\nAdding single contacts:")
address_book.add_contact(person1)
address_book.add_contact(person2)

# Attempt to add a duplicate
print("\nAttempting to add a duplicate contact:")
address_book.add_contact(duplicate_person)


# Display all contacts
print("\nDisplaying all contacts:")
address_book.display_contacts()

# Edit a contact
print("\nEditing a contact:")
address_book.edit_contact("Bob Johnson", "111-222-3333", "newbob@example.com")

# Display contacts again
print("\nDisplaying all contacts after edit:")
address_book.display_contacts()

# Search for a contact
print("\nSearching for contacts with keyword 'alice':")
address_book.search_contact("alice")

# Sort contacts by name
print("\nSorting contacts by name:")
address_book.sort_contacts("name")
address_book.display_contacts()

# Check for duplicates
print("\nChecking for duplicate contacts by name 'Alice Smith':")
address_book.duplicate_contact("Alice Smith")

# Delete a contact
print("\nDeleting a contact:")
address_book.delete_contact("Charlie Brown")

# Display final contact list
print("\nFinal contact list:")
address_book.display_contacts()
