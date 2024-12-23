"""
Proxy is handy when creating highly resourceful object

Problem
1. Postpone the object creation unless absolutely necessary
2. Find a placeholder to create an object when necessary

Scenario
* Producer - create an instance of Producer [at any given time fixed number of producer objects are present]
* Artist - It is a proxy who checks if the producer becomes available for a guest

Solutions
* Clients - interact with the proxy most of the time until the resource intensive object becomes available
* Proxy - responsible for creating the resource intensive objects

Adapter and Decorator are related to Proxy Design Pattern
"""
import time


class Producer:
    """Define the 'resource-intensive' object to instantiate! """

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Define the 'relatively less resource-intrensive' proxy to instantiate"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            # If the Producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)
            # Make the producer meet the guest
            self.producer.meet()
        else:
            # Otherwise don't instatntiate the producer
            time.sleep(2)
            print("Producer is busy!")


# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce  Producer is available
p.produce()

# Change the status to occupied
p.occupied = 'Yes'

# Make the Producer to produce
p.produce()
