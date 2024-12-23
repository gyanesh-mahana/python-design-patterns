"""
Allows a client to have sequential access to the elements of an aggregate object without exposing its underlying
structure

Problem:
1. The traversal interface of an aggregate object getting overcrowded

Scenario
* Our custom iterator based on a built-in Python iterator : zip()
* German counting words
* Only upto a certain point based on a client input

Solution
* Isolate access and traversal features from the aggregate object
* Provide an interface to access the elements of an aggregate object
* Keeps track of the objects being traversed
* make the aggregate object create an iterator for a client

Iterator design pattern is related to composite design pattern
"""


def count_to(count):
    """Custom Iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # our built-in iterator
    # creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a generator containing numbers in German
        yield number


# Test the iterator returned by our iterator
for num in count_to(4):
    print(num)
