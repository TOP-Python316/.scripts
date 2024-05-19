"""Демонстратор выбирающей фабрики."""

from abc import ABC
from dataclasses import dataclass
from datetime import date, datetime as dt
from decimal import Decimal as dec
from random import choice
from pathlib import Path
from sys import path


def countable_nouns(number: int, nouns: tuple[str, str, str]) -> str:
    """Подставляет существительное с окончанием в зависимости от согласуемого числительного."""
    digits_nouns = (
        {1: nouns[0]}
        | dict.fromkeys((2, 3, 4), nouns[1])
        | dict.fromkeys((5, 6, 7, 8, 9, 0, 11, 12, 13, 14), nouns[2])
    )
    last_digit, two_last_digits = number % 10, number % 100
    return digits_nouns.get(two_last_digits) or digits_nouns[last_digit]


@dataclass
class Person(ABC):
    name: str
    birthdate: date

    @property
    def age(self) -> int:
        return (date.today() - self.birthdate).days // 365

    def __str__(self):
        age = self.age
        noun = countable_nouns(age, ('год', 'года', 'лет'))
        return f'{self.name}: {age} {noun}'


@dataclass
class Employee(Person):
    """
    Описывает сотрудника.
    
    Целевой класс.
    """
    position: str
    income: dec
    
    def __str__(self):
        return (
            super().__str__() +
            f', {self.position} ({self.income:.2f})'
        )


@dataclass
class Candidate(Person):
    """
    Описывает соискателя.
    
    Целевой класс.
    """
    cv: bytes = None
    expert1: bool = False
    expert2: bool = False
    final: bool = False
    
    def __bool__(self):
        return self.expert1 and self.expert2 and self.final
    
    def __str__(self):
        return (
            super().__str__() +
            f', {self.expert1}/{self.expert2}/{self.final}'
        )


class Factory:
    """
    Определяет правила приёма кандидата, этапы проведения собеседований и найм кандидата в качестве сотрудника.
    
    Класс фабрики.
    """
    def __init__(self, age_min: int = 18, age_max: int = 58):
        self.age_min = age_min
        self.age_max = age_max
        self._choices: list[bool] = [False, True]
    
    @staticmethod
    def create_candidate(name: str, birthdate: str) -> Candidate:
        """Создаёт соискателя, настраивая его атрибуты и загружая файл резюме из каталога с данным скриптом."""
        person = Candidate(
            name,
            dt.strptime(birthdate, '%d.%m.%Y').date()
        )
        with open(Path(path[0]) / 'cv.pdf', 'rb') as filein:
            person.cv = filein.read()
        return person
    
    def tech_meeting1(self, candidate: Candidate) -> None:
        candidate.expert1 = choice(self._choices)
    
    def tech_meeting2(self, candidate: Candidate) -> None:
        candidate.expert2 = choice(self._choices)
    
    def final_meeting(self, candidate: Candidate) -> None:
        candidate.final = choice((
            False,
            candidate.expert1 and candidate.expert2
        ))
    
    def hire_candidate(
            self,
            person: Candidate,
            position: str,
            income: str
    ) -> Employee | Candidate:
        """Если условия выполнены, то создаёт сотрудника. В противном случае возвращает переданного соискателя."""
        if self.age_min <= person.age <= self.age_max:
            if person:
                emp = Employee(
                    person.name,
                    person.birthdate,
                    position,
                    dec(income)
                )
                ...
                return emp
        return person

   
hr_department = Factory()

egor = hr_department.create_candidate('Егор', '05.05.1980')

hr_department.tech_meeting1(egor)
hr_department.tech_meeting2(egor)
hr_department.final_meeting(egor)

egor = hr_department.hire_candidate(egor, 'Junior Python разработчик', '82540.00')
print(egor)
