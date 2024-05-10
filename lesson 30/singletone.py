# одиночка
# singleton

# обеспечиает, что класс имеет только один экземпляр и предоставляет глобальную точку доступа к этому экземпляру
# используется для предоставления общего доступа к файловым и сетевым ресурсам
# может быть местом хранения конфигурации или констант
# часто используется для логгирования

# черты
# 1. гарантрирует, что у класса один экземпляр
# 2. глобальный доступ. ЭК Одиночка предоставляет доступ к своим методам и атрибутам из любой точки программы
# 3. ленивая инициальизация. ЭК Одиночка создаётся только один раз (при первом вызове), что означает, что его создание можно отложить до реальной необходимости.


# в простейшем виде выглядит так:
# class Singleton:
#     _instance = None

#     def __new__(cls):

#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)

#         return cls._instance


class Singleton:
    _instance = None

    def __new__(cls):

        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
    
s1 = Singleton()
s2 = Singleton()
s3 = Singleton()
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
# >>>: {}
# >>>: {}
# >>>: {}

s1.param = 'test_param'
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
# >>>: {'param': 'test_param'}
# >>>: {'param': 'test_param'}
# >>>: {'param': 'test_param'}

print(id(s1))
print(id(s2))
print(id(s3))
print(s1._instance)
# >>>: 139857457184336
# >>>: 139857457184336
# >>>: 139857457184336
# >>>: <__main__.Singleton object at 0x7f331a0dfe50>