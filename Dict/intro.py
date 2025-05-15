person = {"name " : "Abhishek" , "Age" : 21 , "is_active" : True}

#accessing the elements 
print(person["Age"])

#modify the elements 

person['Age'] = 25

print(person)

# add new elements 
person["city"] = 'Patna'

print(person)

# removing an element
person.pop("Age")
print(person)

#Looping in the disctionart 

for key in person:
    print(key)

for key in person:
    print (key , person[key])

for key , value in person.items():
    print(key , {value})