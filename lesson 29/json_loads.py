# JSON - JavaScript Object Notation
# десериализация
import json
from pprint import pprint


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

print(type(str_json))
# >>>: <class 'str'>

print()
data = json.loads(str_json)  # десериализация
print(type(data))
# >>>: <class 'dict'>
pprint(data)
# {'response': {'count': 32363,
#               'items': [{'first_name': 'Sonya',
#                          'id': 287350527,
#                          'last_name': 'Kargina',
#                          'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'},
#                         {'first_name': 'Slava',
#                          'id': 341523166,
#                          'last_name': 'Kholod',
#                          'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]}}

print()
pprint(data['response'])

print()
print(data['response']['count'])
print()
pprint(data['response']['items'])
# [{'first_name': 'Sonya',
#   'id': 287350527,
#   'last_name': 'Kargina',
#   'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'},
#  {'first_name': 'Slava',
#   'id': 341523166,
#   'last_name': 'Kholod',
#   'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]
pprint(type(data['response']['items']))
# >>>: <class 'list'>

print()
for item in data['response']['items']:
    print(type(item))
    pprint(item)
# <class 'dict'>
# {'first_name': 'Sonya',
#  'id': 287350527,
#  'last_name': 'Kargina',
#  'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'}
# <class 'dict'>
# {'first_name': 'Slava',
#  'id': 341523166,
#  'last_name': 'Kholod',
#  'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}

print()
for item in data['response']['items']:
    print(f'{item["first_name"]} {item["last_name"]}')
# Sonya Kargina
# Slava Kholod