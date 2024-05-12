# 1 / 0
# a + b
# int('hello')

try:
    print(1)
    1 / 0
    a + b
    int('hello')
    print(2)
except ZeroDivisionError:
    print('Деление на ноль')
except ValueError:
    print('Неверное значение')
except NameError:
    print('Переменная не определена')
else:
    print('Все хорошо, исключений не было.')
finally:
    print('Конец программы! ЭТОТ БЛОК ВЫПОЛНЯЕТСЯ ВСЕГДА')
