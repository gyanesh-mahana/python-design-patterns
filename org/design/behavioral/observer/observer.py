"""
Establishes one-to-many relationship between a subject and multiple observers

Problem:
1. Subject need to be monitored
2. Observer need to be modified, when there is a change in the Subject

Scenario
* Core temperature - reactor of a power plant
* Registered observer - need to be modified

Solution
* Abstract class - Subject
    operations - attach, detach, notify
* Concrete classes - Subject

Singleton is related to Observer design pattern
"""


class Subject:
    """ Represents what is being observed"""

    def __init__(self):
        self._observers = []  # Reference to the observers is stored
        # Note that this is one-to-many relation

    def attach(self, observer):
        # method to attach the observers in the list of observer
        if observer not in self._observers:
            self._observers.append(observer)  # add the observer to the observers' list

    def detach(self, observer):
        # method to detach the observer from the list of observers
        try:
            self._observers.remove(observer)  # remove the observer from the observers' list
        except ValueError:
            print("No Observer to the list to remove")
            pass

    def notify(self, modifier=None):
        # Notify all the observers about the change in the state of the Subject
        for observer in self._observers:
            if modifier != observer:  # Do not notify if the observer is modifier
                observer.update(self)  # alert the observer


class Core(Subject):  # Concrete class for Subject
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property  # getter to get the name of the core
    def name(self):
        return self._name

    @property  # getter to get the temperature of the core
    def temp(self):
        return self._temp

    @temp.setter  # setter to set the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:
    """Observer class"""

    def __init__(self):
        print("Viewer class initialized")

    def update(self, subject):
        print("Temperature Viewer:{} has Temperature {}".format(subject.name, subject.temp))


# Create the subjects
core1 = Core("Core 1")
core2 = Core("Core 2")

# Create observers
viewer1 = TempViewer()
viewer2 = TempViewer()
viewer3 = TempViewer()
viewer4 = TempViewer()
viewer5 = TempViewer()
viewer6 = TempViewer()

# Attach observers to the first core
core1.attach(viewer1)
core1.attach(viewer2)
core1.attach(viewer3)

core2.attach(viewer4)
core2.attach(viewer5)
core2.attach(viewer6)

# Change temperature of core 1
core1.temp = 80
core1.temp = 90
core1.temp = 100
core1.temp = 120
core1.temp = 190
