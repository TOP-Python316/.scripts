# Создать класс Customer, который содержит:
# 
# метод __init__, 
#     принимающий на вход имя пользователя и необязательный аргумент баланс его счета(по умолчанию 0). 
#     Эти значения необходимо сохранить в атрибуты name и balance;
#  
# статический метод check_type, 
#     принимающий на вход одно значение. 
#     Если оно не является числом (не принадлежит классу int или float) необходимо вызывать исключение TypeError('Банк работает только с числами').
#     Это все, метод check_type должен только вызывать исключение в случае неправильного типа, возвращать она ничего не должна
#  
# метод withdraw, 
#     принимающий на вход значение для списания. 
#     Необходимо сперва проверить переданное значение на тип при помощи метода check_type. 
#     Если исключений не возникло, необходимо проверить что у покупателя достаточно средств на балансе. 
#     Если денег хватает, то необходимо уменьшить баланс. 
#     Если средств не хватает, нужно вызвать исключение ValueError('Сумма списания превышает баланс')
#  
# метод deposit,
#     принимающий на вход значение для зачисления на баланс.
#     При помощи метода check_type проверьте, что передано число.
#     Если исключений не возникло, увеличьте значение баланса покупателя на указанную сумму.

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        if not Customer.check_type(value):
            if value > self.balance:
                raise ValueError('Сумма списания превышает баланс')
        self.balance -= value

    def deposit(self, value):
        if not self.check_type(value):
            self.balance += value

# Код для проверки

bob = Customer('Bob Odenkirk')
# bob.deposit('hello') # TypeError: Банк работает только с числами
bob.deposit(200)
print(bob.balance)  # 200
bob.withdraw(300)  # ValueError: Сумма списания превышает баланс
bob.withdraw(150)
print(bob.balance)  # 50