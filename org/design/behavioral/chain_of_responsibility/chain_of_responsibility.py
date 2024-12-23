"""
Opens up various possibilities of processing for a given request. It decouples the request and its processing.

Problem:
1. One Request
2. Various types of processing depending on the request

Scenario
* Receive Integer value
* use Different handlers
* to find out its range

Solution
* Abstract Handler - stores the successor, to handle the request
* Concrete Handler - checks if it can handle the request, if the default handler cannot handle the request
"""


class Handler:  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Defines who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handles stop here
        # Otherwise , keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Implementation TBD")


class ConcreteHandler1(Handler):  # Inherits from Abstract handler
    """Concrete Handler 1"""

    def _handle(self, request):
        if 0 < request <= 5:  # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request is handled


class DefaultHandler(Handler):  # Inherits from Abstract handler
    """Default Handler"""

    def _handle(self, request):
        """If there is no handler available"""

        # No condition to check since this is the default handler
        print("End of chain, no handler for {}".format(request))
        return True  # Indicates that the request is handled


class Client:  # Using Handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):  # Send your request one at a time
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [1, 2, 3, 21, 34, 354]

# Send the requests
c.delegate(requests)
