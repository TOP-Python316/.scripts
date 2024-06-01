from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def send(self, message, colleague):
        pass


class ConcreteMediator(Mediator):

    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def send(self, message, colleague):
        for c in self._colleagues:
            if c != colleague:
                c.receive(message)


class Colleague(ABC):

    @abstractmethod
    def receive(self, message):
        pass


class ConcreteColleague1(Colleague):

    def __init__(self, mediator):
        self._mediator = mediator
        mediator.add_colleague(self)

    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        print(f'ConcreteColleague1 received: {message}')


class ConcreteColleague2(Colleague):

    def __init__(self, mediator):
        self._mediator = mediator
        mediator.add_colleague(self)

    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        print(f'ConcreteColleague2 received: {message}')


if __name__ == '__main__':
    mediator = ConcreteMediator()
    colleague1 = ConcreteColleague1(mediator)
    colleague2 = ConcreteColleague2(mediator)
    colleague1.send('Hello')
    colleague2.send('Hi')