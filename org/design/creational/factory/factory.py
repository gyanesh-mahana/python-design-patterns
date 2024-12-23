""""
Problem
1. Uncertainties in types of objects
2. Decisions to be made at runtime regarding which class to be used

Scenario
* Pet shop
* Originally selling dogs
* now decides to sell cat too
"""


class Dog:
    """Basic Dog class"""

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Woof!"


class Cat:
    """Basic Cat class"""

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))  # Uses a dictionary of objects to solve the problem at runtime
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
