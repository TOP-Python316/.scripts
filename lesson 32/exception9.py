try:
    print(1)
    1 / 0
    a + b
    int('hello')
    print(2)
except:
    print('Произошло какое-то исключение')
else:
    print('Все хорошо, исключений не было.')
finally:
    print('Конец программы! ЭТОТ БЛОК ВЫПОЛНЯЕТСЯ ВСЕГДА')