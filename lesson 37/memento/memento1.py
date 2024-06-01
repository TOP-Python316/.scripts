from abc import ABC, abstractmethod
from typing import Any


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state: Any):
        pass


class ConcreteMemento:
    def __init__(self, state: Any):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state: Any):
        self._state = state


class Originator:
    def __init__(self, state: Any):
        self._state = state

    def create_memento(self):
        return ConcreteMemento(self._state)

    def restore_from_memento(self, memento: Memento):
        self._state = memento.get_state()

    def set_state(self, state: Any):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: Memento):
        self._mementos.append(memento)

    def get_memento(self, index: int):
        return self._mementos[index]


if __name__ == "__main__":
    originator = Originator("Initial state")
    caretaker = Caretaker()

    print(f"Originator state: {originator.get_state()}")

    caretaker.add_memento(originator.create_memento())

    originator.set_state("State 1")
    print(f"Originator state: {originator.get_state()}")

    caretaker.add_memento(originator.create_memento())

    originator.set_state("State 2")
    print(f"Originator state: {originator.get_state()}")

    caretaker.add_memento(originator.create_memento())

    originator.restore_from_memento(caretaker.get_memento(1))
    print(f"Originator state: {originator.get_state()}")