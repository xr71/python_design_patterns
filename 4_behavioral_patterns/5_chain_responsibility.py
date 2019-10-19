import pytest

# decouples processing from the request
# abstract handler
# concrete handlers check if they can handle the request and return True if handled

class Handler:
    def __init__(self, successor):
        self._successor = successor


    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        pass


class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10:
            print(f"Request {request} is being handled in handler 1")

            return True


class DefaultHandler(Handler):

    def _handle(self, request):

        print(f"End of chain, no handler for {request}")

        return True


class Client():

    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(successor=None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


requests = [1,2,3,4,5,30,13]
c = Client()

c.delegate(requests)

