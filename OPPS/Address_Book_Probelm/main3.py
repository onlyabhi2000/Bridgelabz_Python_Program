class Person:
    def __init__(self , name , email , phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
    def __repr__(self):
        return self.__str__()

class AddressBook:
    def __init__(self):
        self.contacts = []

    #method to add contacts
    def add_contact(self,contact):
        if not contact in self.contacts:
            self.contacts.append(contact)
            return 

        else:
            print("conatct is already present")

    # method to remove the contacts

    def delete_contacts(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"{name} removed successfully"
        return f"{name} does not exist"
    
    def update_contact(self,name , new_phone , new_email):
        for conatct in self.contacts:
            if conatct.name ==name:
                conatct.phone = new_phone
                conatct.email = new_email
                return "updated succesfully"
            return
        return "conatct does not exist"
    ##method to search
    def search_contact(self, keyword):
        result = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.email.lower():
                result.append(contact)

        if result:
            for data in result:
                print(data)
        else:
            print("No contacts found.")


        return result 

    def sort_by(self, sort_by):
        if sort_by == 'name':
            self.contacts.sort(key=lambda x: x.name)
        elif sort_by == 'phone':
            self.contacts.sort(key=lambda x: x.phone)
        else:
            print("Invalid sort criteria")







person1 = Person('abhi' ,'abhi@gmail' , 876545678)
person2 = Person('shek' , 'shek@gmail' , 987657)

address = AddressBook()

obj1 = address.add_contact(person1)
print(obj1)

# address.delete_contacts(person1)
# result = address.delete_contacts("abhi")
# print(result)



updated_result = address.update_contact("abhi", new_email="abhi_new@gmail.com", new_phone=999999999)
print(updated_result)


##search 
search_result = address.search_contact('abhi')
print("search_result---->",search_result)


##sortby name 
sort_result = address.sort_by('name')
print(sort_result)



for contact in address.contacts:
    print("conatctssss:",contact)




# print(person3.add_contact('sachin' , 'sachin@gmail' , 87656780))

