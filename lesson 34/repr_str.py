class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return f'Объект класса Cat с атрибутами name={self.name} и age={self.age}'
    
    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'


cat_fluffy = Cat(name='Fluffy', age=5)
print(cat_fluffy)
str(cat_fluffy)