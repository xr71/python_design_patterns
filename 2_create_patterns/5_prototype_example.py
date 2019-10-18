import pytest
import copy

# prototype class creation is useful when creating 
# many individual instances that are identical is too expensive

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)

        return obj

class Car:

    def __init__(self):
        self.name = "SkyLark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options}"

c = Car()
proto = Prototype()
proto.register_object("skylark", c)

c1 = proto.clone("skylark")
c2 = proto.clone("skylark")

print(c1)
print(c2)
