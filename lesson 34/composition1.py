from typing import Literal


class Person:

    class Sex:
        __repr: dict[str, str] = {
            'male': 'm',
            'female': 'f',
        }

        def __init__(self, sex: Literal['male', 'female']):
            self.sex: str = sex

        def __repr__(self):
            return self.__repr[self.sex]

    def __init__(
            self,
            first_name: str,
            last_name: str,
            sex: Literal['male', 'female']
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = self.__class__.Sex(sex)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.sex}'


p = Person('John', 'Doe', 'male')
o = Person('Jane', 'Doe', 'female')


Person
# >>>: <class '__main__.Person'>
Person.Sex
# >>>: <class '__main__.Person.Sex'>
Person.Sex('male')
# >>>: m
Person.Sex('female')
# >>>: f
o
# >>>: Jane Doe f
p
# >>>: John Doe m