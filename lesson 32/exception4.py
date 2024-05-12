def second_function():
    print('Начало работы функции second_function')
    try:
        1/0
    except:
        print('Внимание обработано исключение')
    print('Конец работы функции second_function')


def first_function():
    print('Начало работы функции first_function')
    second_function()
    print('Конец работы функции first_function')


print(1)
print(2)
first_function()
print(3)


# >>>: 1
# >>>: 2
# >>>: Начало работы функции first_function
# >>>: Начало работы функции second_function
# >>>: Внимание обработано исключение
# >>>: Конец работы функции second_function
# >>>: Конец работы функции first_function
# >>>: 3