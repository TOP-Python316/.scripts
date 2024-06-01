from abc import ABC, abstractmethod


class Approver(ABC):

    @abstractmethod
    def can_approve(self, request):
        pass

    @abstractmethod
    def approve(self, request):
        pass

    def set_next(self, approver):
        self._next = approver

    def _next_approver(self, request):
        if self._next is not None:
            self._next.approve(request)


class Director(Approver):

    def can_approve(self, request):
        return request.amount <= 10000

    def approve(self, request):
        if self.can_approve(request):
            print('Director approved the request')
        else:
            self._next_approver(request)


class VicePresident(Approver):

    def can_approve(self, request):
        return request.amount <= 50000

    def approve(self, request):
        if self.can_approve(request):
            print('Vice President approved the request')
        else:
            self._next_approver(request)


class President(Approver):

    def can_approve(self, request):
        return True

    def approve(self, request):
        print('President approved the request')


class Client:

    def send_request(self, request):
        director = Director()
        vice_president = VicePresident()
        president = President()
        director.set_next(vice_president)
        vice_president.set_next(president)
        director.approve(request)


class Request:

    def __init__(self, amount):
        self.amount = amount


if __name__ == '__main__':
    client = Client()
    request = Request(5000)
    client.send_request(request)
    request = Request(25000)
    client.send_request(request)
    request = Request(100000)
    client.send_request(request)