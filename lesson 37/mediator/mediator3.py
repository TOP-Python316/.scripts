from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str):
        self.name = name
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send(self, message: str):
        self._mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self.name}: {message}")


class Admin:
    def __init__(self, name: str):
        self.name = name
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send(self, message: str):
        self._mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self.name} (admin): {message}")

    def ban_user(self, user: User):
        self._mediator.ban_user(user)


class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, sender: User | Admin):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def add_admin(self, admin: Admin):
        pass

    @abstractmethod
    def ban_user(self, user: User):
        pass


class ChatMediator(Mediator):
    def __init__(self):
        self._users = []
        self._admins = []

    def send(self, message: str, sender: User | Admin):
        if isinstance(sender, User):
            for u in self._users:
                if u != sender:
                    u.receive(message)
            for a in self._admins:
                a.receive(message)
        elif isinstance(sender, Admin):
            for u in self._users:
                u.receive(message)
            for a in self._admins:
                if a != sender:
                    a.receive(message)

    def add_user(self, user: User):
        self._users.append(user)

    def add_admin(self, admin: Admin):
        self._admins.append(admin)

    def ban_user(self, user: User):
        self._users.remove(user)


if __name__ == "__main__":
    mediator = ChatMediator()

    user_1 = User("Alice")
    user_2 = User("Bob")
    admin_1 = Admin("Charlie")

    mediator.add_user(user_1)
    mediator.add_user(user_2)
    mediator.add_admin(admin_1)

    user_1.set_mediator(mediator)
    user_2.set_mediator(mediator)
    admin_1.set_mediator(mediator)

    user_1.send("Hi, everyone!")
    user_2.send("Hello, Alice!")
    admin_1.send("Welcome to our chat!")
    admin_1.ban_user(user_2)
    user_1.send("Bye, everyone!")