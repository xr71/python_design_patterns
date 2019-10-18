import pytest

# Abstract Factory
##  imagine an abstract Pet factory
##  and a concrete factory that can instantiate dogs and cats
##  an abstract Product factory
##  a concrete factory that can produce cats and dogs food


class Dog():
    """
    return Dog object
    """
    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return "Dog"


class DogFactory():
    """
    Concrete factory 
    """

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog food"


class PetStore():
    """
    PetStore houses our Abstract Factory
    """

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()


        print(f"Our pet is {pet}")
        print(f"Our pet says hello with {pet.speak()}")
        print(f"Its food is {pet_food}")

# concrete factory
factory = DogFactory()

# create a pet store housing our abstract factory
store = PetStore(pet_factory=factory)

store.show_pet()
