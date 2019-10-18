import pytest

# an object oriented way of providing global variables
# allow only instance from a class
##  this is very useful when you need an information cache from multiple systems
##  implementing modules 
# Borg design pattern

##  make class attributes global

class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)

        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP="HyperText Transfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
