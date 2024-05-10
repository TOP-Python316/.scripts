# Абстрактный класс - это класс, который не предназначен для создания
# объектов напрямую.
# Это класс-шаблон для других классов, он определяет абстрактные методы,
# которые нужно реализовать в дочерних классах

# Абстрактный метод - это метод, который определяется в абстрактном классе,
# но не имеет реализации.
# Это как бы шаблон для метода, который нужно реализовать в дочерних классах.

# Abstract Base Classes
from abc import ABC, abstractmethod


# мы создали абстракцию Фигура
# если у класса есть хотя бы один абстрактный метод,
# то этот класс является абстрактным
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# s = Shape()
# >>>: Can't instantiate abstract class Shape with abstract methods area, perimeter


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius
    

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length
    

c = Circle(5)
s = Square(5)