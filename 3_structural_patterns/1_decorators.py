import pytest
from functools import wraps

def make_blink(function):

    @wraps(function)

    def decorator():

        ret = function()

        return "<blink>" + ret + "</blink>"
    return decorator

@make_blink
def hello_world():
    return "Hello World!"

print(hello_world())

