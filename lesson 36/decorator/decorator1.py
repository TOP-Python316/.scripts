from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован
class IComponent(ABC):
    @abstractmethod
    def operation(self):
        pass


# Конкретная реализация интерфейса IComponent
class ConcreteComponent(IComponent):
    def operation(self):
        print("ConcreteComponent: Operation")


# Базовый класс-декоратор, реализующий интерфейс IComponent и содержащий ссылку на объект-компонент
class Decorator(IComponent):
    def __init__(self, component: IComponent):
        self._component = component

    def operation(self):
        self._component.operation()


# Конкретные классы-декораторы, реализующие дополнительную функциональность
class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("ConcreteDecoratorA: Before")
        super().operation()
        print("ConcreteDecoratorA: After")


class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("ConcreteDecoratorB: Before")
        super().operation()
        print("ConcreteDecoratorB: After")


# Пример использования
if __name__ == "__main__":
    component = ConcreteComponent()
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)
    decorator_b.operation()
