class Person:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"


    # def __eq__(self, other):
    #     if not isinstance(other, Person):
    #         return False
    #     return (self.first_name.lower() == other.first_name.lower() and 
    #             self.last_name.lower() == other.last_name.lower())

    # def __str__(self):
    #     return (f"Name: {self.first_name} {self.last_name}\n"
    #             f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
    #             f"Phone: {self.phone}\nEmail: {self.email}\n")

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_user_input(cls):
        print("\nEnter contact details:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        address = input("Address: ").strip()
        city = input("City: ").strip()
        state = input("State: ").strip()
        zip_code = input("ZIP Code: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        
        return cls(first_name, last_name, address, city, state, zip_code, phone, email)