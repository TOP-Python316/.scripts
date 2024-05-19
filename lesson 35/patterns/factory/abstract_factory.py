from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass


class Table(ABC):
    @abstractmethod
    def eat_on(self) -> str:
        pass


class ModernChair(Chair):
    def sit_on(self) -> str:
        return "You are sitting on a modern chair."


class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "You are sitting on a Victorian chair."


class ModernTable(Table):
    def eat_on(self) -> str:
        return "You are eating on a modern table."


class VictorianTable(Table):
    def eat_on(self) -> str:
        return "You are eating on a Victorian table."


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


def client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()
    print(chair.sit_on())
    print(table.eat_on())


print("Client: Testing client code with the modern factory:")
modern_factory = ModernFurnitureFactory()
client_code(modern_factory)

print("\nClient: Testing the same client code with the Victorian factory:")
victorian_factory = VictorianFurnitureFactory()
client_code(victorian_factory)


# Объяснение работы
# Абстрактные классы продуктов: Chair и Table задают общие интерфейсы для стульев и столов. Они обеспечивают единообразие в методах, которые должны быть реализованы в конкретных продуктах.
# Конкретные классы продуктов: ModernChair, VictorianChair, ModernTable, VictorianTable реализуют методы абстрактных продуктов, предоставляя конкретную функциональность для разных стилей мебели.
# Абстрактная фабрика: FurnitureFactory определяет интерфейс для создания продуктов. Это позволяет клиентскому коду работать с различными фабриками без изменения логики создания продуктов.
# Конкретные фабрики: ModernFurnitureFactory и VictorianFurnitureFactory реализуют методы абстрактной фабрики, создавая конкретные продукты для современных и викторианских стилей.
# Клиентский код: Работает с абстрактной фабрикой и абстрактными продуктами, что позволяет легко переключаться между различными фабриками и продуктами.
# Таким образом, паттерн "Абстрактная фабрика" позволяет создавать семейства взаимосвязанных объектов без жесткой привязки к конкретным классам. Это делает код более гибким и легко расширяемым.
