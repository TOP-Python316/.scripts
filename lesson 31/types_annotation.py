x: int = 5
y: str = 'hello'
z: list = [1, 2, 3]
w: dict = {'name': 'Tom', 'lastname': 'Anderson'}
a: bool = True
b: float = 3.14
c: tuple = (1, 2, 3)


x = 'Hello world!'
# >>>: types_annotation.py:10: error: Incompatible types in assignment (expression has type "str", variable has type "int")
# >>>: Found 1 error in 1 file (checked 1 source file)
print(x)
# >>>: Hello world!