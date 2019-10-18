import pytest

# Builder creation pattern is a solution to an anti-pattern
# prevents building complex objects using too many constructors

##  like building a complex car, you need to source completed components first
##  Builder solution: director --> interfaces
##  Director - Abstract builder - Concrete Builder - Product

# focus is reducing complexity through divide and conquer

class Director():

    def __init__(self, builder=None):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car   

class Builder():
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):

    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"

class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} {self.tires} {self.engine}"


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
