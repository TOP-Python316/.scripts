from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован
class ISubject(ABC):
    @abstractmethod
    def request(self):
        pass


# Конкретная реализация интерфейса ISubject
class RealSubject(ISubject):
    def request(self):
        print("RealSubject: Request")


# Класс-прокси, реализующий интерфейс ISubject и выступающий в роли посредника между клиентом и объектом
class Proxy(ISubject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        # Выполнение дополнительной функциональности перед вызовом метода request объекта
        print("Proxy: Before")
        self._real_subject.request()
        # Выполнение дополнительной функциональности после вызова метода request объекта
        print("Proxy: After")


# Пример использования
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
