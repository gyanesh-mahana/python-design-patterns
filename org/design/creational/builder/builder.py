"""
Solution to an anti-pattern called telescopic constructor
    -when developer uses excessive number of constructors to solve a problem

Problem
1. Excessive number of constructors

Scenario
* Building cars
* Build individual Part and then assemble them together to form a car

Solution
4 roles
1. Director
2. Abstract Builder - interfaces
3. Concrete Builder - implements the interfaces
4. Product - object being built
"""


class Director:
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tyres()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract builder"""

    def __str__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLark(Builder):
    """Concrete Builder"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tyres(self):
        self.car.tyres = "Regular tyres"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Mustang(Builder):
    """Concrete Builder"""

    def add_model(self):
        self.car.model = "Mustang"

    def add_tyres(self):
        self.car.tyres = "Special tyres"

    def add_engine(self):
        self.car.engine = "Turbo Jet Engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tyres = None
        self.engine = None

    def __str__(self):
        return "{}|{}|{}".format(self.model, self.tyres, self.engine)


# create an abstract builder object
builder = SkyLark()
# builder = Mustang()

# create director with builder object
director = Director(builder)

# invoker the director method
director.construct_car()
car = director.get_car()
print(car)
