from pprint import pprint


# публичный (public)
# защищённый (protected)
# приватный (private)

# public
# _protected
# __private
# __magic__


# публичный
class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def __str__(self):
        return f'BankAccount(name={self.name}, balance={self.balance}, passport={self.passport})'


account = BankAccount('Bob', 100, '12345')
print(account)
print(account.balance)
print(account.passport)
print(account.name)
# >>>: BankAccount(name=Bob, balance=100, passport=12345)
# >>>: 100
# >>>: 12345
# >>>: Bob


# _защищённый

class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self._balance = balance
        self._passport = passport

    def __str__(self):
        return f'BankAccount(name={self.name}, balance={self._balance}, passport={self._passport})'


account = BankAccount('Bob', 100, '12345')
print(account)
print(account._balance)
print(account._passport)
print(account.name)
# >>>: BankAccount(name=Bob, balance=100, passport=12345)
# >>>: 100
# >>>: 12345
# >>>: Bob


# __приватный

class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        return f'BankAccount(name={self.name}, balance={self.__balance}, passport=**{self.__passport[2:]})'


account = BankAccount('Bob', 100, '12345')
print(account.print_private_data())
# >>>: BankAccount(name=Bob, balance=100, passport=**345)
# print(account.__balance)
# >>>: AttributeError: 'BankAccount' object has no attribute '__balance'
# print(account.__passport)
# >>>: AttributeError: 'BankAccount' object has no attribute '__passport'
# account.__balance = 10000000
# print(account.print_private_data())

pprint(dir(account))
# ['_BankAccount__balance',
#  '_BankAccount__passport',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'name']

