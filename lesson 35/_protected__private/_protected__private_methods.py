class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.__balance = balance
        self.__passport = passport

    # get_balance = lambda self: self.__balance

    # get_passport = lambda self: self.__passport

    # set_balance = lambda self, new_balance: self.__balance = new_balance

    # set_passport = lambda self, new_passport: self.__passport = new_passport

    def public_call(self):
        print('работает публичный метод public_call')
        self.__print_private_data()

    def __print_private_data(self):
        print('работает приватный метод __print_private_data')
        print(f'BankAccount(name={self.name}, balance={self.__balance}, passport=**{self.__passport[2:]})')


account = BankAccount('Bob', 100, '12345')
account.public_call()

# account.__print_private_data()
# >>>: AttributeError: 'BankAccount' object has no attribute '__print_private_data'

# account.__balance
# >>>: AttributeError: 'BankAccount' object has no attribute '__balance'
# account.__passport
# >>>: AttributeError: 'BankAccount' object has no attribute '__passport'

account._BankAccount__print_private_data()
print(account._BankAccount__balance)
print(account._BankAccount__passport)

# >>>: работает приватный метод __print_private_data
# >>>: BankAccount(name=Bob, balance=100, passport=**345)
# >>>: 100
# >>>: 12345
