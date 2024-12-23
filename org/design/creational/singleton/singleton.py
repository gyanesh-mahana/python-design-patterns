"""
Problem
1. Global variable in an object-oriented way
2. Borg - python concept (similar to Singleton)- allows multiple variables but with same state

Scenario
* An information cache
* Shared by multiple objects

Solution
* Module - All modules in python act as a singleton
    -Shared by multiple objects
* Borg Design Pattern
    -Computer networking acronyms
    - Spelled out versions
"""


class Borg:
    """Borg Design pattern"""
    _shared_data = {}  # attribute dictionary for global access

    def __init__(self):
        self.__dict__ = self._shared_data  # make an attribute dictionary


class Singleton(Borg):  # inherit Borg
    """The Singleton class"""

    def __init__(self, **kwargs):
        print("initialized!")
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # update the attribute dictionary - Concept of Abstract Mapping is being used

    def __str__(self):
        return str(self._shared_data)  # return attribute dictionary as string


# Create a singleton object and add first acronym

x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")

# print the object
print(x)
print(y)
