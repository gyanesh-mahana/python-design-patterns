"""
Problem
1. Creating identical objects individually - expensive in terms of computing power
2. Cloning - Alternative

Scenario
* Mass production
* Same color, same options and so on

Solution
* Create a prototypical instance first
* Clone it whenever you need a replica
"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}  # create a dictionary object - objects to be cloned

    def register_object(self, name, obj):
        """Register the object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister the object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{}|{}|{}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object("Skylark", c)
c1 = prototype.clone("Skylark")
print(c1)

for i in range(0, 100):
    ci = prototype.clone("Skylark")
    print("copy ", i + 1, " is:", ci)
