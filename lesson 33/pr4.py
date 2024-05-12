# Необходимо реализовать код, отвечающий за обработку данных о тестировании конфигурации настольных компьютеров и ноутбуков,
# каждый из которых отличается моделью, процессором, памятью и производительностью.
# 
# Создайте базовый класс Computer с атрибутами model, processor и memory.
# Затем создайте два подкласса Desktop и Laptop, которые наследуют атрибуты и методы Computer и реализуют свои собственные версии метода run().
# В дополнение, создайте класс ComputerStore, который содержит список компьютеров и имеет метод run_tests(),
# вызывающий метод run() для каждого компьютера.
# 
# Используйте самописный декоратор для вывода результатов.


def performance_test(func):
    def wrapper(*args, **kwargs):
        print('Начинаем тест производительности...')
        result = func(*args, **kwargs)
        print('Тест производительности завершен.')
        return result
    return wrapper

class Computer:
    def __init__(self, model, processor, memory):
        self.model = model
        self.processor = processor
        self.memory = memory
    
    def run(self):
        pass

class Desktop(Computer):    
    @performance_test
    def run(self):
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

class Laptop(Computer):
    @performance_test
    def run(self):
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

class ComputerStore:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def run_tests(self):
        for computer in self.computers:
            computer.run()


# Пример использования:
store = ComputerStore()
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб"))
store.add_computer(Laptop("Dell Xtra", "Intel Core i5 13600K", "32 Гб"))
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))
store.run_tests()

# Вывод:
# Начинаем тест производительности...
# Запускаем настольный компьютер 'HP Legion' с процессором Intel Core i9-10900K и 64 Гб RAM.
# Тест производительности завершен.
# Начинаем тест производительности...
# Запускаем ноутбук 'Dell Xtra' с процессором Intel Core i5 13600K и 32 Гб RAM.
# Тест производительности завершен.
# Начинаем тест производительности...
# Запускаем настольный компьютер 'Lenovo SuperPad' с процессором AMD Ryzen 7 2700X и 16 Гб RAM.
# Тест производительности завершен.