"""
Offers a family of interchangeable algorithms to a client

Problem:
1. There is a need of dynamically changing behavior of object

Scenario
* Abstract strategy with a default set of behaviors
* Concrete strategy classes with new behaviors - dynamically replacing the default methods with new one

Solution
* Python allows adding methods dynamically by importing types module

"""
import types


class Strategy:
    """The Strategy pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another function is required
        """The Default method that prints the name of the strategy being used"""
        print("{} is being used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Create our default strategy object
s0 = Strategy()
# Execute default strategy
s0.execute()

# Create first variation of our default strategy
s1 = Strategy(strategy_one)
# Set the name of Stratgey
s1.name = "First Variation Strategy"
# Execute the first variation of default strategy
s1.execute()

# Create second variation of our default strategy
s2 = Strategy(strategy_two)
# Set the name of Stratgey
s2.name = "Second Variation Strategy"
# Execute the second variation of default strategy
s2.execute()
