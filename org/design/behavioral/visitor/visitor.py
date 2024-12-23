"""
Allows adding new features to the existing class hierarchy without changing it

Problem:
1. Adding new Operations to
2. Existing Classes with minimal changes
3. All dynamically done

Scenario
* House class
* HVAC specialist - Visitor type 1
* Electricians - Visitor Type 2

Solution
* New Operations to be performed on
* Various elements of an existing class hierarchy
* Visitors can also provide operations on a composite object

"""


class House(object):  # The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        visitor.visit(self)  # Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)  # Note that we now have a reference to the electrician object

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract Visitor"""

    def __str__(self):
        """Simply return the class name when Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete Visitor: HVAC Specialist"""

    def visit(self, house):
        house.work_on_hvac(self)  # Note that the visit has reference to the HVAC Specialist object


class Electrician(Visitor):
    """Concrete Visitor: Electrician"""

    def visit(self, house):
        house.work_on_electricity(self)  # Note that the visit has reference to the HVAC Specialist object


# Create HVAC Specialist
hv = HvacSpecialist()

# Create Electrician
el = Electrician()

# Create a Home
home = House()

# Accept HVAC Specialist to home
home.accept(hv)

# Accept Electrician to home
home.accept(el)
