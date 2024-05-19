class Fridge:
    def __init__(self, *products: str):
        self.camera: list[str] = list(products)

    def __iter__(self):
        return self.camera.__iter__()

    def __getitem__(self, index):
        return self.camera[index]

    def put(self, *products: str):
        self.camera.extend(products)

    def __repr__(self):
        return '\n'.join(self.camera)


fridge = Fridge('Молоко 3.2%', 'Хлеб белый', 'Масло', 'Колбаса')

fridge
# >>>: Молоко 3.2%
# >>>: Хлеб белый
# >>>: Масло
# >>>: Колбаса
fridge[1]
# >>>: 'Хлеб белый'
fridge[3]
# >>>: 'Колбаса'
fridge.put('авокадо', 'бананы')
fridge
# >>>: Молоко 3.2%
# >>>: Хлеб белый
# >>>: Масло
# >>>: Колбаса
# >>>: авокадо
# >>>: бананы
for product in fridge:
    print(product)
# >>>: Молоко 3.2%
# >>>: Хлеб белый
# >>>: Масло
# >>>: Колбаса
# >>>: авокадо
# >>>: бананы