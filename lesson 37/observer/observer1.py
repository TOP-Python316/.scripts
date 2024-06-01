from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):

    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserver(Observer):

    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self, subject):
        if subject == self._subject:
            sbj_state = self._subject.get_state()
            msg = f'ConcreteObserver: Subject state changed to {sbj_state}'
            print(msg)


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer1 = ConcreteObserver(subject)
    observer2 = ConcreteObserver(subject)
    subject.set_state('State 1')
    subject.set_state('State 2')
    subject.detach(observer1)
    subject.set_state('State 3')