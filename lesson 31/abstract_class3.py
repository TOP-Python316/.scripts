from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Bird(Animal):
    def speak(self):
        print('Chirp')  


dog = Dog('Spot', 5, 'Labrador')
cat = Cat('Garfield', 3, 'Persian')
bird = Bird('Tweety', 2, 'Parrot')

for animal in [dog, cat, bird]:
    animal.speak()