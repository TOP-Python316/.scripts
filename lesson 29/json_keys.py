import json
from pprint import pprint
from random import randint


str_json = """
       {
         "first_name": "Sonya",
         "last_name": "Kargina",
         "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",
         "likes": 366
       }
"""

data = json.loads(str_json)  # десериализация
data['likes'] = randint(1, 100)
data['is_online'] = True
data['is_banned'] = False
data['mail'] = None

new_str_json = json.dumps(data, indent=2)  # сериализация
pprint(new_str_json)
# ('{\n'
#  '  "first_name": "Sonya",\n'
#  '  "last_name": "Kargina",\n'
#  '  "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",\n'
#  '  "likes": 95,\n'
#  '  "is_online": true,\n'
#  '  "is_banned": false,\n'
#  '  "mail": null\n'
#  '}')

# d = {
#   "first_name": "Sonya",
#   "last_name": "Kargina",
#   "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",
#   "likes": 366,
# }
# print(d)



