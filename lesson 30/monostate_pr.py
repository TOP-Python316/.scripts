# класс FireSensor
# атрибуты:
#   battery_swap: когда поставлена батарейка
#   fireguard_inspection: когда была пожарная проверка
#   brand: фирма-производитель
# методы:
#   update_data: изменяет все три параметра
#   get_data: возвращает кортеж из трёх параметров


class FireSensor:

    __shared_dict = {}

    def __init__(self) -> None:
        self.__dict__ = FireSensor.__shared_dict

    def update_data(self, battery_swap, fireguard_inspection, brand) -> None:
        self.battery_swap = battery_swap
        self.fireguard_inspection = fireguard_inspection
        self.brand = brand

    def get_data(self) -> tuple:
        return tuple(self.__shared_dict.values())
    

sens1 = FireSensor()
sens2 = FireSensor()
print(sens1.__dict__)
print(sens2.__dict__)
print('-----------------')

sens1.battery_swap = '28.04.2024'
sens2.fireguard_inspection = '01.01.1970'
sens3 = FireSensor()
sens3.brand = 'Philips'
print(sens1.__dict__)
print(sens2.__dict__)
print(sens3.__dict__)
print('-----------------')


sens3.update_data('01.01.2024', '10.10.2010', 'Samsung')
print(sens1.__dict__)
print(sens2.__dict__)
print(sens3.__dict__)
print('-----------------')

sens4 = FireSensor()
print(sens4.get_data())
print('-----------------')

sens4.expiration_date = '31.12.2027'
print(sens1.__dict__)
print(sens2.__dict__)
print(sens3.__dict__)
print(sens4.__dict__)
