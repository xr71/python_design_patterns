# Factory
## for creating other objects
## useful in uncertaintities in types of objects
## decision to be made at runtime

import pytest

class Dog():
    """a simple dog"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"
    
def get_pet(pet="dog"):
    """
    The factory method for creating Pets
    """

    pets = dict(dog=Dog("Fido"))

    return pets[pet]

# now say we need a new class called Cat

class Cat():
    """a simple cat"""

    def __init__(self, name):
        self._name = name 

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """
    The factory method for creating Pets
    """

    pets = dict(dog=Dog("Fido"), cat=Cat("Odif"))

    return pets[pet]

def test_dog_speak():
    a_dog = Dog("Beethoven")
    retVal = a_dog.speak()
    assert retVal == "Woof!"

d = get_pet(pet="dog")
print(d.speak())

c = get_pet(pet="cat")
print(c.speak())