class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.description}) - {self.price} $"


class Menu:
    def __init__(self):
        self._items = []

    def add_item(self, item: MenuItem):
        self._items.append(item)

    def remove_item(self, item: MenuItem):
        self._items.remove(item)

    def create_iterator(self):
        return MenuIterator(self)


class MenuIterator:
    def __init__(self, menu: Menu):
        self._menu = menu
        self._cursor = 0

    def has_next(self):
        return self._cursor < len(self._menu._items)

    def next(self):
        item = self._menu._items[self._cursor]
        self._cursor += 1
        return item

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration
        return self.next()


class Waiter:
    def __init__(self, menu: Menu):
        self._menu = menu

    def print_menu(self):
        iterator = self._menu.create_iterator()
        while iterator.has_next():
            print(iterator.next())


if __name__ == "__main__":
    menu = Menu()

    menu.add_item(MenuItem("Burger", "with cheese", 5.5))
    menu.add_item(MenuItem("Pizza", "margherita", 7.0))
    menu.add_item(MenuItem("Steak", "medium rare", 12.0))

    waiter = Waiter(menu)
    waiter.print_menu()

    # Использование итератора с циклом for
    iterator = menu.create_iterator()
    for item in iterator:
        print(item)