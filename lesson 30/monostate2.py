# моносостояние
# monostate
# borg

# обеспечивает одинаковый набор атрибутов с одинаковыми значениеями для всех ЭК

# в простейшем виде выглядит так:
# class ClassName:

#     __shared_dict = {}

#     def __init__(self) -> None:
#         self.__dict__ = ClassName.__shared_dict



class Cat:

    __shared_attributes = {
        'breed': None,
        'color': None
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attributes


tom = Cat()
scratch = Cat()

tom.color = 'black'

print(tom.__dict__)
print(scratch.__dict__)
# >>>: {'breed': None, 'color': 'black'}
# >>>: {'breed': None, 'color': 'black'}
print('-----------------')

scratch.breed = 'sphynx'

print(tom.__dict__)
print(scratch.__dict__)
# >>>: {'breed': 'sphynx', 'color': 'black'}
# >>>: {'breed': 'sphynx', 'color': 'black'}
print('-----------------')

scratch.age = 5

print(tom.__dict__)
print(scratch.__dict__)
# >>>: {'breed': 'sphynx', 'color': 'black', 'age': 5}
# >>>: {'breed': 'sphynx', 'color': 'black', 'age': 5}
print('-----------------')

matroskin = Cat()

print(tom.__dict__)
print(scratch.__dict__)
print(matroskin.__dict__)
print('-----------------')

simba = Cat()
del simba.age

print(tom.__dict__)
print(scratch.__dict__)
print(matroskin.__dict__)
print(simba.__dict__)
print('-----------------')

print(id(tom))
print(id(scratch))
print(id(matroskin))
print(id(simba))