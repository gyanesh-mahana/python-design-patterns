"""
Problem
1. The user expectation yields multiple, related objects

Scenario
* Pet Factory
    # Dog Factory - produce Dogs and related products
    # Cat Factory - produce Cats and related products

Solution
* Abstract factory - Pet factory (Abstract classes)
* Concrete factory - Dog factory and Cat factory (Often Singleton classes)
* Concrete Products - Dogs and Dog food, Cats and Cat foods
"""


class Dog:

    @staticmethod
    def speak():
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete class"""

    @staticmethod
    def get_pet():
        """return Dog object"""
        return Dog()

    @staticmethod
    def get_food():
        """return Dog food object"""
        return "Dog Food!"


class Cat:

    @staticmethod
    def speak():
        return "Meow!"

    def __str__(self):
        return "Cat"


class CatFactory:
    """Concrete class"""

    @staticmethod
    def get_pet():
        """return Cat object"""
        return Cat()

    @staticmethod
    def get_food():
        """return Cat food object"""
        return "Cat Food!"


class PetStore:
    """Abstract factory class"""

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Pet is '{}'!".format(pet))
        print("Pet speaks '{}'!".format(pet.speak()))
        print("Pet is '{}'!".format(pet_food))


# Create a concrete factory
factory = DogFactory()
# factory = CatFactory()

# Create a pet store
shop = PetStore(factory)

# Invoke utility method
shop.show_pet()
