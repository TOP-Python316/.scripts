import json
from pprint import pprint
from random import randint


str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""

# удалить в каждом элементе ключ id и заменить его на ключ likes
data = json.loads(str_json)  # десериализация

for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(0, 1000)

pprint(data)

print()
new_json = json.dumps(data)  # сериализация
print(new_json)

print('Ниже будет json с параметром indent=2'.center(50, '-'))
new_json = json.dumps(data, indent=2)  # сериализация
print(new_json)
# {
#   "response": {
#     "count": 32363,
#     "items": [
#       {
#         "first_name": "Sonya",
#         "last_name": "Kargina",
#         "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",
#         "likes": 366
#       },
#       {
#         "first_name": "Slava",
#         "last_name": "Kholod",
#         "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg",
#         "likes": 22
#       }
#     ]
#   }
# }