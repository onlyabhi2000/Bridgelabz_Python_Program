# super() --> it is an buildin method , which helps toc clal the parents methods in child class without rewriting the code of parent class
# It is mainly used in inheritance to extend or reuse the functionality of the base class without rewriting code.”


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from Parent class."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class's __init__ method
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the parent class's greet method
        return f"{parent_greeting} I am {self.age} years old from Child class."