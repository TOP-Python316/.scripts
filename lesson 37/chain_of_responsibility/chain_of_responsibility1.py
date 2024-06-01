from abc import ABC, abstractmethod


class Handler(ABC):

    _next = None

    @abstractmethod
    def can_handle(self, request):
        pass

    @abstractmethod
    def handle(self, request):
        pass

    def set_next(self, handler):
        self._next = handler

    def _next_handler(self, request):
        if self._next is not None:
            self._next.handle(request)


class ConcreteHandler1(Handler):

    def can_handle(self, request):
        return request.type == 'type1'

    def handle(self, request):
        if self.can_handle(request):
            print('ConcreteHandler1 handled the request')
        else:
            self._next_handler(request)


class ConcreteHandler2(Handler):

    def can_handle(self, request):
        return request.type == 'type2'

    def handle(self, request):
        if self.can_handle(request):
            print('ConcreteHandler2 handled the request')
        else:
            self._next_handler(request)


class Client:

    def send_request(self, request):
        handler1 = ConcreteHandler1()
        handler2 = ConcreteHandler2()
        handler1.set_next(handler2)
        handler1.handle(request)


class Request:

    def __init__(self, type):
        self.type = type


if __name__ == '__main__':
    client = Client()
    request = Request('type1')
    client.send_request(request)
    request = Request('type2')
    client.send_request(request)
    request = Request('type3')
    client.send_request(request)