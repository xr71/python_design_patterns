import pytest
import time
import random

## two unrelated, parallel, or orthongonal implementations
# one is implementation specific
# one is implementation agnostic


class DrawingCircleOne(object):

    def draw_circle(self, x, y, radius):
        print(f"Drawing a circle at {x} and {y} with a radius of {radius}")

class DrawingCircleTwo(object):

    def draw_circle(self, x, y, radius):
        print(f"API TWO is going to draw a circle at {x} and {y} with a radius of {radius}")


class Circle(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):

        self._radius *= percent


circle1 = Circle(3,2,5, DrawingCircleOne())
circle1.draw()
circle1.scale(1.5)
circle1.draw()

