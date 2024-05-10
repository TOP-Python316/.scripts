# каждый из этих классов имеет одинаковый конструктор
# и метод speak с отличающащейся реализацией

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print('Woof')


class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print('Meow')


class Bird:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print('Chirp')


dog = Dog('Spot', 5, 'Labrador')
cat = Cat('Garfield', 3, 'Persian')
bird = Bird('Tweety', 2, 'Parrot')

for animal in [dog, cat, bird]:
    animal.speak()