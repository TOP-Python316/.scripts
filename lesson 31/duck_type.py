# если что-то выглядит как утка, плавает как утка, и крякает как утка, то скорее всего, это утка.

my_collection = [
    {1, 3, 5, 7, 9},
    (1, 1, 1, 1, 1, 1, 1, 1),
    [1, 2, 3, 4, 5],
    'hello',
    {'name': 'Tom', 'lastname': 'Anderson'},
]

for item in my_collection:
    print(len(item))