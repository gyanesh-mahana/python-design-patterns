"""
Problem
1. New feature to an existing object
2. Dynamic changes
3. Not using subclassing

Scenario
* "Hello World!"
* <blink> "Hello World!" </blink>
"""

from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docs
    @wraps(function)
    # Define the inner function
    def decorator():
        # return value of the function being decorated
        ret = function()
        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply decorator here

@make_blink
def hello_world():
    """Original Function!"""
    return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is same
print(hello_world.__name__)

# CHeck if the function documentation is same
print(hello_world.__doc__)
