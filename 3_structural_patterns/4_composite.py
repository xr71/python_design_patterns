import pytest
import time
import random


## lets say we want to build a recursive tree structure
## each element of the tree can have sub-elements
## so this creates a sub sub model challenge

# solution
##  component - abstract
##  child - concrete
##  composite - maintains child objects by adding or removing them



# define the interface in the Component class

class Component:
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print(f"{self.name}")


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

        self.children = []

    def component_function(self):
        print(f"Composite name is {self.name}")

        for i in self.children:
            i.component_function()

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)


sub1 = Composite("submenu 1")
sub11 = Child("submenu 1 1")
sub1.append_child(sub11)

print(sub1)
sub1.component_function()


top = Composite("top menu")
sub2 = Composite("submenu 2")

top.append_child(sub2)
top.append_child(sub1)

top.component_function()


