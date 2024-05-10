class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Meow')


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Woof')


tom = Cat('Tom')
scratch = Cat('Scratch')
leo = Cat('Leo')
scooby = Dog('Scooby')
spike = Dog('Spike')
snoopy = Dog('Snoopy')

list_of_animals = [tom, scratch, leo, scooby, spike, snoopy]

for animal in list_of_animals:
    animal.speak()
