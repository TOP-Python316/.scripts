from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def primitive_operation1(self):
        pass

    @abstractmethod
    def primitive_operation2(self):
        pass

    def template_method(self):
        self.primitive_operation1()
        self.primitive_operation2()


class ConcreteClass1(AbstractClass):

    def primitive_operation1(self):
        print('ConcreteClass1 primitive operation 1')

    def primitive_operation2(self):
        print('ConcreteClass1 primitive operation 2')


class ConcreteClass2(AbstractClass):

    def primitive_operation1(self):
        print('ConcreteClass2 primitive operation 1')

    def primitive_operation2(self):
        print('ConcreteClass2 primitive operation 2')


if __name__ == '__main__':
    cc1 = ConcreteClass1()
    cc1.template_method()
    cc2 = ConcreteClass2()
    cc2.template_method()