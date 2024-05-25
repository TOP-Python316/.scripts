# Сложная система, состоящая из нескольких подсистем
class SubsystemA:
    def operation1(self):
        print("SubsystemA: Operation1")

    def operation2(self):
        print("SubsystemA: Operation2")


class SubsystemB:
    def operation1(self):
        print("SubsystemB: Operation1")

    def operation2(self):
        print("SubsystemB: Operation2")


class SubsystemC:
    def operation1(self):
        print("SubsystemC: Operation1")

    def operation2(self):
        print("SubsystemC: Operation2")


# Класс-фасад, предоставляющий единообразный интерфейс к сложной системе
class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self):
        print("Facade: Operation")
        self._subsystem_a.operation1()
        self._subsystem_b.operation2()
        self._subsystem_c.operation1()


# Пример использования
if __name__ == "__main__":
    facade = Facade()
    facade.operation()
