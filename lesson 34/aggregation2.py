from datetime import date, datetime as dt, timedelta as td


class Product:

    _default_date_format: str = '%d.%m.%Y'

    def __init__(
            self, name: str,
            produced: date | str = date.today(),
            days_before_expire: int = 7
    ):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, self._default_date_format).date()
        self.produced: date = produced
        self.expired: date = self.produced + td(days=days_before_expire)

    def is_expired(self) -> bool:
        return self.expired < date.today()

    def __repr__(self):
        state = 'срок годности истек' if self.is_expired() else 'срок годности еще не истек'
        return f'{self.name} - {state}'


class Fridge:
    def __init__(self, *products: Product):
        self.camera: list[Product] = list(products)

    def __iter__(self):
        return self.camera.__iter__()

    def __getitem__(self, index):
        return self.camera[index]

    def put(self, *products: Product) -> None:
        self.camera.extend(products)

    def __repr__(self):
        return '\n'.join(repr(pr) for pr in self.camera)

    def clear_expired(self) -> None:
        """Удаляет из холодильника продукты с истекшим сроком годности"""
        for pr in self.camera.copy():
            if pr.is_expired():
                self.camera.remove(pr)

        # to_remove = []
        # for i, pr in enumerate(self.camera):
        #     if pr.is_expired():
        #         to_remove.append(i)
        # for i in reversed(to_remove):
        #     del self.camera[i]

        # self.camera = list(filter(lambda pr: not pr.is_expired(), self.camera))


kitchen = Fridge(
    Product('Молоко 3.2%', '17.05.2024'),
    Product('Хлеб белый', days_before_expire=3),
    Product('Масло', '17.05.1023', days_before_expire=10),
)


for product in sorted(kitchen, key=lambda pr: pr.expired):
    print(product.expired, product.name)

# >>>: 1023-05-27 Масло
# >>>: 2024-05-21 Хлеб белый
# >>>: 2024-05-24 Молоко 3.2%
kitchen
# >>>: Молоко 3.2% - срок годности еще не истек
# >>>: Хлеб белый - срок годности еще не истек
# >>>: Масло - срок годности истек
kitchen.clear_expired()
kitchen
# >>>: Молоко 3.2% - срок годности еще не истек
# >>>: Хлеб белый - срок годности еще не истек