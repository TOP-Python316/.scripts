from abc import ABC, abstractmethod


# Интерфейс для работы с устройствами
class IDevice(ABC):
    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass


# Конкретные реализации интерфейса IDevice для различных типов устройств
class ConcreteDeviceA(IDevice):
    def enable(self):
        print("ConcreteDeviceA: Enable")

    def disable(self):
        print("ConcreteDeviceA: Disable")


class ConcreteDeviceB(IDevice):
    def enable(self):
        print("ConcreteDeviceB: Enable")

    def disable(self):
        print("ConcreteDeviceB: Disable")


# Базовый класс, реализующий интерфейс и содержащий ссылку на объект-реализацию
class Device:
    def __init__(self, device: IDevice):
        self._device = device

    def enable(self):
        self._device.enable()

    def disable(self):
        self._device.disable()


# Конкретные классы, реализующие дополнительную функциональность и наследующие базовый класс
class AdvancedDeviceA(Device):
    def enable(self):
        print("AdvancedDeviceA: Before")
        super().enable()
        print("AdvancedDeviceA: After")

    def disable(self):
        print("AdvancedDeviceA: Before")
        super().disable()
        print("AdvancedDeviceA: After")


class AdvancedDeviceB(Device):
    def enable(self):
        print("AdvancedDeviceB: Before")
        super().enable()
        print("AdvancedDeviceB: After")

    def disable(self):
        print("AdvancedDeviceB: Before")
        super().disable()
        print("AdvancedDeviceB: After")


# Пример использования
if __name__ == "__main__":
    device_a = ConcreteDeviceA()
    device_b = ConcreteDeviceB()
    advanced_device_a = AdvancedDeviceA(device_a)
    advanced_device_b = AdvancedDeviceB(device_b)
    advanced_device_a.enable()
    advanced_device_a.disable()
    advanced_device_b.enable()
    advanced_device_b.disable()
