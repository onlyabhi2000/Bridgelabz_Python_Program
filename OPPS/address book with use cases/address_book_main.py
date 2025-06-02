from addresbook import AddressBook
from person import Person
import json
import csv

class AddressBookMain:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self):
        name = input("Enter name for the new address book: ").strip()
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
            return
        
        self.address_books[name] = AddressBook(name)
        print(f"Address book '{name}' created successfully.")

    def add_contact(self):
        book_name = input("Enter theaddress book name: ").strip()
        if book_name not in self.address_books:
            print(f"Address book '{book_name}' not found.")
            return
        
        person = Person.from_user_input()
        self.address_books[book_name].add_contact(person)

    def edit_contact(self):
        book_name = input("Enter address book name: ").strip()
        if book_name not in self.address_books:
            print(f"Address book '{book_name}' not found.")
            return
        
        first_name = input("Enter first name to edit: ").strip()
        last_name = input("Enter last name to edit: ").strip()
        self.address_books[book_name].edit_contact(first_name, last_name)

    def delete_contact(self):
        book_name = input("Enter address book name: ").strip()
        if book_name not in self.address_books:
            print(f"Address book '{book_name}' not found.")
            return
        
        first_name = input("Enter first name of contact to delete: ").strip()
        last_name = input("Enter last name of contact to delete: ").strip()
        self.address_books[book_name].delete_contact(first_name, last_name)

    def search_in_city(self):
        city = input("Enter city to search: ").strip()
        results = []
        for book in self.address_books.values():
            results.extend(book.search_in_city(city))
        
        self.display_search_results(results, f"Contacts in {city}")

    def search_in_state(self):
        state = input("Enter state to search: ").strip()
        results = []
        for book in self.address_books.values():
            results.extend(book.search_in_state(state))
        
        self.display_search_results(results, f"Contacts in {state}")

    def view_by_city_or_state(self):
        print("\n1. View by City")
        print("2. View by State")
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == '1':
            city = input("Enter city: ").strip()
            results = []
            for book in self.address_books.values():
                results.extend(book.search_in_city(city))
            self.display_search_results(results, f"Contacts in {city}")
        elif choice == '2':
            state = input("Enter state: ").strip()
            results = []
            for book in self.address_books.values():
                results.extend(book.search_in_state(state))
            self.display_search_results(results, f"Contacts in {state}")
        else:
            print("Invalid choice.")

    def count_by_city_or_state(self):
        print("\n1. Count by City")
        print("2. Count by State")
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == '1':
            counts = {}
            for book in self.address_books.values():
                book_counts = book.count_by_city()
                for city, count in book_counts.items():
                    counts[city] = counts.get(city, 0) + count
            
            print("\n count by city:")
            for city, count in counts.items():
                print(f"{city}: {count}")
        elif choice == '2':
            counts = {}
            for book in self.address_books.values():
                book_counts = book.count_by_state()
                for state, count in book_counts.items():
                    counts[state] = counts.get(state, 0) + count
            
            print("\n vount by state:")
            for state, count in counts.items():
                print(f"{state}: {count}")
        else:
            print("invalid_choice.")

    def sort_entries(self):
        book_name = input("Enter address book name: ").strip()
        if book_name not in self.address_books:
            print(f"Address book '{book_name}' not found.")
            return
        
        print("\nSort by:")
        print("1-->ame")
        print("2-->City")
        print("3-->State")
        print("4--> zip_code")
        choice = input("Enter your choice like 1or 2 or 3 or 4: ").strip()
        
        book = self.address_books[book_name]
        if choice == '1':
            sorted_contacts = book.sort_by_name()
        elif choice == '2':
            sorted_contacts = book.sort_by_city()
        elif choice == '3':
            sorted_contacts = book.sort_by_state()
        elif choice == '4':
            sorted_contacts = book.sort_by_zip()
        else:
            print("invalid_choice.")
            return
        
        print(f"\nSorted contacts in '{book_name}':")
        for person in sorted_contacts:
            print(person)

    def save_to_file(self):
        filename = input("Enter filename to save--> ").strip()
        if not filename:
            print("filename cant be empty.")
            return
        
        print("\nSave as:")
        print("1--> txt file")
        print("2--> csv file")
        print("3--? json file")
        choice = input("Enter 1 oe 2 or 3: ").strip()
        
        all_contacts = []
        for book in self.address_books.values():
            all_contacts.extend([person.to_dict() for person in book.contacts])
        
        try:
            if choice == '1':
                with open(f"{filename}.txt", 'w') as f:
                    for contact in all_contacts:
                        f.write(f"name: {contact['first_name']} {contact['last_name']}\n")
                        f.write(f"addres: {contact['address']}, {contact['city']}, {contact['state']} {contact['zip_code']}\n")
                        f.write(f"phone: {contact['phone']}\nEmail: {contact['email']}\n\n")
                print(f"info saved to {filename}.txt")
            elif choice == '2':
                with open(f"{filename}.csv", 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=all_contacts[0].keys())
                    writer.writeheader()
                    writer.writerows(all_contacts)
                print(f"indo saved to {filename}.csv")
            elif choice == '3':
                with open(f"{filename}.json", 'w') as f:
                    json.dump(all_contacts, f, indent=2)
                print(f"info saved to {filename}.json")
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_file(self):
        filename = input("Enter filename to load (without extension): ").strip()
        if not filename:
            print("Filename cannot be empty.")
            return
        
        print("\nLoad from:")
        print("1. Text File (Not supported - use CSV or JSON)")
        print("2. CSV File")
        print("3. JSON File")
        choice = input("Enter your choice (2-3): ").strip()
        
        try:
            if choice == '2':
                with open(f"{filename}.csv", 'r') as f:
                    reader = csv.DictReader(f)
                    contacts = [row for row in reader]
            elif choice == '3':
                with open(f"{filename}.json", 'r') as f:
                    contacts = json.load(f)
            else:
                print("Invalid choice.")
                return
            
            book_name = input("Enter address book name to add these contacts to: ").strip()
            if book_name not in self.address_books:
                self.address_books[book_name] = AddressBook(book_name)
            
            count = 0
            for contact in contacts:
                person = Person(
                    contact['first_name'],
                    contact['last_name'],
                    contact['address'],
                    contact['city'],
                    contact['state'],
                    contact['zip_code'],
                    contact['phone'],
                    contact['email']
                )
                if self.address_books[book_name].add_contact(person):
                    count += 1
            
            print(f"Successfully loaded {count} contacts into '{book_name}'.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def display_search_results(self, results, title):
        if not results:
            print(f"No {title.lower()} found.")
            return
        
        print(f"\n{title}:")
        for person in results:
            print(person)

    def display_all(self):
        if not self.address_books:
            print("No address books available.")
            return
        
        for book in self.address_books.values():
            print(book)

    def run(self):
        print("Welcome to Address Book Program")
        
        while True:
            print("\nMenu:")
            print("1. create new addess book")
            print("2. add")
            print("3. update teh contacts")
            print("4. delete the contacts")
            print("5. search in the city")
            print("6. search in the statee")
            print("7. view by city or statee")
            print("8. cpount by city or state")
            print("9. dort data")
            print("10. save the file")
            print("11. load it from the file")
            print("12. display all addressbook")
            print("13. exit")
            
            choice = input("Enter your choice : ").strip()
            
            if choice == '1':
                self.create_address_book()
            elif choice == '2':
                self.add_contact()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.search_in_city()
            elif choice == '6':
                self.search_in_state()
            elif choice == '7':
                self.view_by_city_or_state()
            elif choice == '8':
                self.count_by_city_or_state()
            elif choice == '9':
                self.sort_entries()
            elif choice == '10':
                self.save_to_file()
            elif choice == '11':
                self.load_from_file()
            elif choice == '12':
                self.display_all()
            elif choice == '13':
                print("Exiting!!!!!!!!!!!!!!!!!!!!!")
                break
            else:
                print("wrong choice , try again")

if __name__ == "__main__":
    app = AddressBookMain()
    app.run()