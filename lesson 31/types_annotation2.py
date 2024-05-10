def add_two_numbers(x: int, y: int) -> int:
    return x + y


add_two_numbers(5, 'hello')
# types_annotation2.py:5: error: Argument 2 to "add_two_numbers" has incompatible type "str"; expected "int"
# Found 1 error in 1 file (checked 1 source file)

# аннотация типов позволяет избежать ошибок при вызове функции с неправильными типами аргументов