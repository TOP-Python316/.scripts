def first_function():
    print('Начало работы функции first_function')
    try:
        second_function()
    except Exception as ex:
        print(f'Обработано исключение: {ex}')
    print('Конец работы функции first_function')


def second_function():
    print('Начало работы функции second_function')
    third_function()
    print('Конец работы функции second_function')


def third_function():
    print('Начало работы функции third_function')
    1/0
    print('Конец работы функции third_function')

print(1)
print(2)
first_function()
print(3)