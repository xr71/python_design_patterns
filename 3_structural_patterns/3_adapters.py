import pytest
import time
import random

# interfaces are incompatible
# between client and server

# we would like to use a generic method for the client to bridge

class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        print("An-neyong?")

class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        print("Hello?")


class Adapter:
    
    def __init__(self, object, **adapted_method):
        self._object = object

        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []
k = Korean()
b = British()

objects.append(Adapter(k, speak=k.speak_korean))
objects.append(Adapter(b, speak=b.speak_english))

print(objects)

for o in objects:
    o.speak()
