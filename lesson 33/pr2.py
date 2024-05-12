# Создайте абстрактный класс Employee, имеющий абстрактный метод calculate_salary().
# 
# Реализуйте два класса HourlyEmployee и SalariedEmployee, унаследованные от Employee,
# реализующие метод calculate_salary() для расчета заработной платы по часам и окладу соответственно.
# 
# Класс HourlyEmployee при инициализации должен создавать атрибуты hours_worked и hourly_rate. 
# 
# Класс SalariedEmployee при инициализации должен создавать только атрибут monthly_salary. 


from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass


class HourlyEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Код для проверки

hourly_employee = HourlyEmployee(100, 25)
assert hourly_employee.hours_worked == 100
assert hourly_employee.hourly_rate == 25
assert hourly_employee.calculate_salary() == 2500

salaried_employee = SalariedEmployee(4000)
assert salaried_employee.monthly_salary == 4000
assert salaried_employee.calculate_salary() == 4000
print('Good')