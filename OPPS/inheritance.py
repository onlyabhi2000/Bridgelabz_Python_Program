# Inheritance is the process by which one class takes on the attributes and methods of another. 
# Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes.


## Syntax
# class Parent:
#     hair_color = "brown"

# class Child(Parent):
#     pass


class Dog:
    def __init__(self , name , age , breed):
        self.name = name 
        self.age = age
        self.breed = breed

    def description(self):
        return f"dog name is {self.name} and dog age is {self.age} and breed is {self.breed}"
    
    def sound(self , sound):
        return f"dog name {self.name} has sound {sound} "
    


dog_obj_1 = Dog('sheru' , 5 , 'German')
dog_obj_2 = Dog('dogesh' , 3 , 'Russian')

print(dog_obj_1.description())
print(dog_obj_2.sound("bho bho"))


class BullDog(Dog):
    pass


child_obj = BullDog('sheero' , 10 , 'bull dog')

print(child_obj.description())

print(isinstance(child_obj , Dog))


class GermanShefard(Dog):
    def sound(self, sound):
        return f"dog name {self.name}  has a sound like {sound}"

### Note : One thing to keep in mind about class inheritance is that changes to the parent class
#  automatically propagate to child classes. This occurs as long as the attribute or method being changed isn’t overridden in the child class.


## method overriding
obj_german = GermanShefard('germ' , 15 , 'german_shefard')
print(obj_german.sound("gerrr"))

