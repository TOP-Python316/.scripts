from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class ConcreteIterator:
    def __init__(self, aggregate):
        self._aggregate = aggregate
        self._cursor = 0

    def has_next(self):
        return self._cursor < len(self._aggregate._items)

    def next(self):
        item = self._aggregate._items[self._cursor]
        self._cursor += 1
        return item


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


class ConcreteAggregate:
    def __init__(self):
        self._items = []

    def create_iterator(self):
        return ConcreteIterator(self)

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)


if __name__ == "__main__":
    aggregate = ConcreteAggregate()

    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())