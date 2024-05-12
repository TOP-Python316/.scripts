class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message='Зарплата не входит в диапазон от 0 до 1000'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'
    

salary = int(input('Введите ваша зарплата: '))
if not 0 < salary < 1000:
    raise SalaryNotInRangeError(salary)