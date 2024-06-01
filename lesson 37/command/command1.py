from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class ConcreteCommandA(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action_a()

    def undo(self):
        self._receiver.undo_a()


class ConcreteCommandB(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action_b()

    def undo(self):
        self._receiver.undo_b()


class Receiver:
    def action_a(self):
        print("Action A")

    def undo_a(self):
        print("Undo Action A")

    def action_b(self):
        print("Action B")

    def undo_b(self):
        print("Undo Action B")


class Invoker:
    def __init__(self):
        self._commands = []

    def execute_command(self, command: Command):
        command.execute()
        self._commands.append(command)

    def undo_command(self):
        if len(self._commands) > 0:
            command = self._commands.pop()
            command.undo()


if __name__ == "__main__":
    receiver = Receiver()
    invoker = Invoker()

    commands = [
        ConcreteCommandA(receiver),
        ConcreteCommandB(receiver),
        ConcreteCommandA(receiver),
    ]

    for command in commands:
        invoker.execute_command(command)

    invoker.undo_command()
    invoker.undo_command()