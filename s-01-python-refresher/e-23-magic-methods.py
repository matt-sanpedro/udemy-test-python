# in python, methods with two underscores on both sides called magic methods
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # GOAL: print a nice and easy to read string for users
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        # GOAL: to be unambiguous
        # returns a more information-rich, or official, string representation of an object
        return f"<Person(\"{self.name}\", {self.age}) at unique ID: {id(self)}>"

bob = Person("Bob", 35)
print(bob)
print(bob.__repr__())
