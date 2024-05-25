from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован
class IImplementor(ABC):
    @abstractmethod
    def operation_impl(self):
        pass


# Конкретные реализации интерфейса IImplementor
class ConcreteImplementorA(IImplementor):
    def operation_impl(self):
        print("ConcreteImplementorA: OperationImpl")


class ConcreteImplementorB(IImplementor):
    def operation_impl(self):
        print("ConcreteImplementorB: OperationImpl")


# Базовый класс, реализующий интерфейс и содержащий ссылку на объект-реализацию
class Abstraction:
    def __init__(self, implementor: IImplementor):
        self._implementor = implementor

    def operation(self):
        self._implementor.operation_impl()


# Конкретные классы, реализующие дополнительную функциональность и наследующие базовый класс
class RefinedAbstractionA(Abstraction):
    def operation(self):
        print("RefinedAbstractionA: Before")
        super().operation()
        print("RefinedAbstractionA: After")


class RefinedAbstractionB(Abstraction):
    def operation(self):
        print("RefinedAbstractionB: Before")
        super().operation()
        print("RefinedAbstractionB: After")


# Пример использования
if __name__ == "__main__":
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()
    abstraction_a = RefinedAbstractionA(implementor_a)
    abstraction_b = RefinedAbstractionB(implementor_b)
    abstraction_a.operation()
    abstraction_b.operation()
