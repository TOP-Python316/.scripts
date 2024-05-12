print(1)
print(2)
try:
    print(3)
    print(1/0)
    print(4)
except ZeroDivisionError:
    print('Ошибка деления на ноль')
print(5)

print('------------------')

print(1)
print(2)
try:
    print(3)
    print(1/0)
    print(4)
except ArithmeticError:
    print('Произошла какая-то арифметическая ошибка')
print(5)

print('------------------')

print(1)
print(2)
try:
    print(3)
    print(1/0)
    print(4)
except ArithmeticError as e:
    print(f'Error {e}', type(e))
print(5)