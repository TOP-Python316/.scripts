"""Демонстратор простой фабрики."""


class Person:
    """
    Описывает человека с уникальным числовым идентификатором.

    Целевой класс.
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.name} ({self.id})'


class PersonFactory:
    """
    Создаёт и нумерует экземпляры класса Person используя атрибут экземпляра.

    Класс фабрики.
    """

    def __init__(self):
        self.id = 0

    def create_person(self, name: str) -> Person:
        self.id += 1
        return Person(self.id, name)
    

pf = PersonFactory()
p1 = pf.create_person('Egor')
p2 = pf.create_person('Alina')
p3 = pf.create_person('Giorgy')
p1
# >>>: <__main__.Person object at 0x7f5449a9ed70>
p2
# >>>: <__main__.Person object at 0x7f5449a9e920>
p3
# >>>: <__main__.Person object at 0x7f5449a9efe0>
print(p1, p2, p3, sep='\n')
# >>>: Egor (1)
# >>>: Alina (2)
# >>>: Giorgy (3)