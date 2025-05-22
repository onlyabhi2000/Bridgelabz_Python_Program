### class : A class is a blueprint for how to define something. It doesn’t actually contain any data.

### While the class is the blueprint, an ```instance ```is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint
anymore. It’s an actual dog with a name, like Miles, who’s four years old.

### Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.

### You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When you create a new class instance, then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object.


Example :
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


## self.name = name creates an attribute called name and assigns the value of the name parameter to it.
## self.age = age creates an attribute called age and assigns the value of the age parameter to it.