from typing import Protocol


class Animal(Protocol):
    def walk(self) -> None:
        pass

    def speak(self) -> None:
        pass


class Dog:
    def walk(self):
        print('Walking')

    def speak(self) -> None:
        print('Woof')


def make_noise(animal: Animal) -> None:
    animal.speak()

d = Dog()
make_noise(d)