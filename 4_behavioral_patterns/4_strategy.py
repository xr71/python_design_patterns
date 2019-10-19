import pytest

# there is often a need for dynamically changing the behavior of an object

# abstract strategy class comes with a set of default behavior
# a concrete class of that strategy can come with new behaviors

# types module

import types

class Strategy():

    def __init__(self, function=None):
        self.name = "default strategy"

        # if a reference to a function is provided, update the execute method

        if function:
            self.execute = types.MethodType(function, self)


    def execute(self):
        print(f"{self.execute} is used")


s = Strategy()
print(s)
s.execute()


def strategy_one(self):
    print(f"{self.name} is the strategy used")

s1 = Strategy(function=strategy_one)
s1.name = "Strategy 1"
s1.execute()
