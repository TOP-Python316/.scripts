# class Car:

#     def _start_engine(self):
#         return "Engine's sound."

#     def run(self):
#         return self._start_engine()


# car = Car()

# print(car._start_engine())
# # >>>: Engine's sound.


from accessify import protected
from pprint import pprint


class Car:

    @protected
    def __start_engine(self):
        return "Engine's sound."

    def run(self):
        return self.__start_engine()


car = Car()

# print(car.start_engine())
# >>>: accessify.errors.InaccessibleDueToItsProtectionLevelException: Car.start_engine() is inaccessible due to its protection level

# print(car._Car__start_engine())
# >>>: AttributeError: 'Car' object has no attribute '_Car__start_engine'


# R
# camelCase
# snake_case
# Snake_Case
# UpperCamelCase
# strange.case
