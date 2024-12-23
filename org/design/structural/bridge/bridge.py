"""
Helps untangle unnecessary class hierarchy

Problem
1. Unrelated,  parallel, or orthogonal abstractions
2. One - implementation specific and
3. Other - implementation independent

Scenario:
* Implementation-independent circle abstraction (properties of a circle)
* Implementation-dependent circle abstraction (how to draw a circle)

Solution:
* Separate the abstraction into two different class hierarchies

Abstract-Factory and Adapter patterns are related to Bridge Design pattern

"""


class DrawingAPIOne(object):
    """Implementation specific abstraction: concrete class one"""

    @staticmethod
    def draw_circle(x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation specific abstraction : concrete class two"""

    @staticmethod
    def draw_circle(x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
    """Implementation independent abstraction"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation specific abstraction taken care by another function"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation independent function"""
        self._radius *= percent


# Build the first circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# draw a Circle
circle1.draw()
# Build the second circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# draw second Circle
circle2.draw()
circle1.scale(10)
circle2.scale(20)
circle1.draw()
circle2.draw()
