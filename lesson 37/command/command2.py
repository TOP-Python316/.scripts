from abc import ABC, abstractmethod


class Light:
    def __init__(self, name):
        self._name = name
        self._state = False

    def turn_on(self):
        self._state = True
        print(f"{self._name} is turned on")

    def turn_off(self):
        self._state = False
        print(f"{self._name} is turned off")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_on()

    def undo(self):
        self._light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_off()

    def undo(self):
        self._light.turn_on()


class RemoteControl:
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
    living_room_light = Light("Living room")
    kitchen_light = Light("Kitchen")

    remote_control = RemoteControl()

    commands = [
        LightOnCommand(living_room_light),
        LightOnCommand(kitchen_light),
        LightOffCommand(living_room_light),
    ]

    for command in commands:
        remote_control.execute_command(command)

    remote_control.undo_command()
    remote_control.undo_command()