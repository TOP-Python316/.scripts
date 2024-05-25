from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован
class ITarget(ABC):
    @abstractmethod
    def request(self):
        pass


# Существующий класс, интерфейс которого необходимо адаптировать
class Adaptee:
    def specific_request(self):
        print("Adaptee: Specific Request")


# Класс-адаптер, реализующий интерфейс ITarget и адаптирующий интерфейс Adaptee
class Adapter(ITarget):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        self._adaptee.specific_request()


# Пример использования
if __name__ == "__main__":
    adaptee = Adaptee()
    target = Adapter(adaptee)
    target.request()