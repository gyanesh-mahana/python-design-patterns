"""
maintain tree data structure to represent part-whole relationship

Problem
1. Recursive tree data structure
2. Menu>sub-menu> sub-sub-menu>...

Scenario
* Menu
* Submenu

Solution
* Three major elements
    Component (abstract class)
    Child (concrete class - inherit from Component)
    Composite (concrete class - inherit from Component, maintains Child object by adding and removing from tree data structure)
"""


class Component(object):
    """Abstract Class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Component.__init__(*args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print("{}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Component.__init__(*args, **kwargs)

        # This is where we store the name of the composite object!
        self.name = args[0]

        # This is where we keep our child item!
        self.children = []

    def append_child(self, child):
        """Method to add new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove child item"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of composite object!
        print("{}".format(self.name))

        # Iterate though the children and invoke their component function
        for child in self.children:
            child.component_function()


# Build a composite submenu1
sub1 = Composite("submenu1")

# Create a new child sub_subMenu 11
sub11 = Child("sub_submenu11")

# Create a new child sub_subMenu 12
sub12 = Child("sub_submenu12")

# Add the sub_subMenu 11 to subMenu 1
sub1.append_child(sub11)

# Add the sub_subMenu 12 to subMenu 1
sub1.append_child(sub12)

# Build a top level composite menu
top = Composite("top_menu")

# Build a composite submenu2
sub2 = Composite("submenu2")

# Add the submenu1 to top menu
top.append_child(sub1)

# Add the submenu2 to top menu
top.append_child(sub2)

top.component_function()

sub1.component_function()

sub1.remove_child(sub11)

top.component_function()

sub1.component_function()
