class PersonAgeError(Exception):
    
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage
    
    def __str__(self):
        return f'Недопустимый возраст: {self.age}, должен быть в диапазоне от: {self.minage} до: {self.maxage}'


class Person:
    def __init__(self, name, age):
        self.name = name
        minage, maxage = 1, 150
        if minage < age < maxage:
            self.age = age
        else:
            raise PersonAgeError(age, minage, maxage)
            

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'
    

dude = Person('Maks', 34)
print(dude)


try:
    dude = Person('Maks', 151)
    print(dude)
except PersonAgeError as ex:
    print(ex)
