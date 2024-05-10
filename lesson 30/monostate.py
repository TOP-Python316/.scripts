class Cat:

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

tom = Cat('pers', 'white')
scratch = Cat('siam', 'bald')

print(tom.__dict__)
print(scratch.__dict__)
# >>>: {'breed': 'pers', 'color': 'white'}
# >>>: {'breed': 'siam', 'color': 'bald'}

tom.color = 'black'
scratch.breed = 'sphynx'

print(tom.__dict__)
print(scratch.__dict__)
# >>>: {'breed': 'pers', 'color': 'black'}
# >>>: {'breed': 'sphynx', 'color': 'bald'}