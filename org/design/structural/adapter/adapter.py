"""
Problem
1. Incompatible interfaces

Scenario
* Korean: speak_korean()
* British: speak_english()
* Client: speak() - uniform interface

Solution:
* translates method name between client and server code

Bridges and Decorator are related to the Adapter design pattern
"""


class Korean:
    """Korean Speaker"""

    def __init__(self):
        self.name = "Korean"

    @staticmethod
    def speak_korean():
        return "An-neyong?"


class British:
    """English Speaker"""

    def __init__(self):
        self.name = "British"

    @staticmethod
    def speak_english():
        return "Hello!"


class Adapter:
    """Translates the generalized method name to individualized method name"""

    def __init__(self, obj, **adapted_method):
        """Change the namer of the method"""
        self._object = obj

        # Add a new dictionary item that establishes the mapping between generic and specific method
        # For Example, speak() will be translated to speak_korean() or speak_english()
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes!"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create Korean object
korean = Korean()

# Create British object
british = British()

# Append the objects to the object list
# objects.append(korean)
# objects.append(british)
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for o in objects:
    print("{} says '{}'\n".format(o.name, o.speak()))
