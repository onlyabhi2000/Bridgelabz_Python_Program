import re
regex = {
    'first_name': r'^[A-Za-z]+$',
    'last_name': r'^[A-Za-z]+$',
    'address': r'^[A-Za-z0-9\s,.-]+$',
    'city': r'^[A-Za-z]+$',
    'state': r'^[A-Za-z]+$',
    'zip_code': r'^\d{6}$',
    'phone': r'^\+?\d{10,13}$',
    'email': r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
}

def validate_person_data(person):
    for field, pattern in regex.items():
        value = getattr(person, field, "")
        if not re.fullmatch(pattern, value):
            return False
    return True

def validate_input(method):
    def inner(self):
        book_name = input("Enter the address book name: ").strip()
        if book_name not in self.address_books:
            print(f"Address book '{book_name}' not found.")
            return
        
        person = self.get_person_data()
        if person and validate_person_data(person):
            self.address_books[book_name].add_contact(person)
            print("Contact added.")
            return True
            
        else:
            print("Contact cant be added , as it fails the validations")
    return inner




