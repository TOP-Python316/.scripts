from enum import Enum
from pprint import pprint


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


pprint(list(Weekday))
# [<Weekday.MONDAY: 1>,
#  <Weekday.TUESDAY: 2>,
#  <Weekday.WEDNESDAY: 3>,
#  <Weekday.THURSDAY: 4>,
#  <Weekday.FRIDAY: 5>,
#  <Weekday.SATURDAY: 6>,
#  <Weekday.SUNDAY: 7>]

print(Weekday.MONDAY.name)
print(Weekday.MONDAY.value)
print(Weekday.TUESDAY.name)
print(Weekday.TUESDAY.value)
# MONDAY
# 1
# TUESDAY
# 2

weekday_dict = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
}


# Используйте dict, когда вам нужны динамические ключи и значения, или когда важна скорость доступа по ключу.
# Используйте enum, когда у вас есть фиксированный набор именованных констант, и вам важна читабельность и защита от ошибок.