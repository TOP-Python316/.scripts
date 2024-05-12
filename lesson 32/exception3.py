def second_function():
    print('Начало работы функции second_function')
    1/0
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
# >>>: Traceback (most recent call last):
# >>>:   File "/home/maks/Work/top-academy/python 316/.scripts/lesson 32/exception3.py", line 15, in <module>
# >>>:     first_function()
# >>>:   File "/home/maks/Work/top-academy/python 316/.scripts/lesson 32/exception3.py", line 9, in first_function
# >>>:     second_function()
# >>>:   File "/home/maks/Work/top-academy/python 316/.scripts/lesson 32/exception3.py", line 3, in second_function
# >>>:     1/0
# >>>: ZeroDivisionError: division by zero


