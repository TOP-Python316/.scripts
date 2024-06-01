from abc import ABC, abstractmethod


class SmartHomeController:

    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def send_command(self, command, device):
        for d in self._devices:
            if d != device:
                d.receive_command(command)


class Device(ABC):

    def __init__(self, controller):
        self._controller = controller
        controller.add_device(self)

    def send_command(self, command):
        self._controller.send_command(command, self)

    @abstractmethod
    def receive_command(self, command):
        pass


class AirConditioner(Device):

    def __init__(self, controller):
        super().__init__(controller)

    def receive_command(self, command):
        if command == 'on':
            print('Air conditioner is on')
        elif command == 'off':
            print('Air conditioner is off')


class Light(Device):

    def __init__(self, controller):
        super().__init__(controller)

    def receive_command(self, command):
        if command == 'on':
            print('Light is on')
        elif command == 'off':
            print('Light is off')


if __name__ == '__main__':
    controller = SmartHomeController()
    air_conditioner = AirConditioner(controller)
    light = Light(controller)
    air_conditioner.send_command('on')
    light.send_command('off')