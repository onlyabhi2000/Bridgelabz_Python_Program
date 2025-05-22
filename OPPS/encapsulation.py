## Encapsulation is a crucial OOP concept that refers to the idea of wrapping up data and its related methods into a single unit.
#  It limits direct access to variables and methods and prevents any unintentional or accidental modifications of data.
#  To avoid these unintended changes, a variable of an object can be changed only by the method of an object. These variables are called private variables. 





# Access Modifiers in Python Encapsulation --->
# At times, we might need to restrict access to certain variables or methods while programming.
# In such situations, we use access modifiers in Python encapsulation that limit the access of the class data members from outside the class.
# They protect the internal data of a class and instances associated with it. There are 3 types of access modifiers supported by encapsulation in Python.
# They are as follows: 

# Public Members- Member variables of a class are public by default, which means the data members and methods can be accessed outside or inside of a class.

# Private Members- The private data members are accessible only within a class and are denoted with a double underscore prefix before their name.

# Protected Members- These data members are accessible within a class and their subclasses and are denoted by a single underscore prefix before the name.


### Public Access Modifier
# class Dog:
#     def __init__(self , name , age):
#         self.name = name 
#         self.age = age

#     def description(self):
#         return f"dog name is {self.name} and dog age is {self.age}"
    
#     def sound(self , sound):
#         return f"dog name {self.name} has sound {sound} "
    
# ## accessing using method
# dog_obj=Dog('dogesh' , 10)
# print(dog_obj.description())

# ## accessing using object directly
# print(dog_obj.name)



####Private

class Dog:
    def __init__(self , name , age):
        self.name = name 
        self.__age = age

    def description(self):
        return f"dog name is {self.name} and dog age is {self.__age}"
    
    ## HAve to create the set and get method

    def set_age(self , new_age):
        self.__age = new_age


    def get_age(self):
        return self.__age
    
    
## accessing using method
dog_obj = Dog("dogesh", 10)
print(dog_obj.get_age())  

dog_obj.set_age(12)
print(dog_obj.get_age())  
# print(dog_obj.description())

## accessing using object directly

## if we try to access in this way then will get the attribute error
# print(dog_obj.__age)



