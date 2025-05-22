class Dog:
    def __init__(self , name , age):
        self.name = name 
        self.age = age

    def description(self):
        return f"dog name is {self.name} and dog age is {self.age}"
    
    def sound(self , sound):
        return f"dog name {self.name} has sound {sound} "
    


dog_obj_1 = Dog('sheru' , 5)
dog_obj_2 = Dog('dogesh' , 3)

print(dog_obj_1.description())
print(dog_obj_2.sound("bho bho"))

# print(dog_obj_1)


