import json
from pprint import pprint
from random import randint
import datetime


# не все объекты можно легко перевести
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

data = json.loads(str_json)  # десериализация
# for item in data['response']['items']:
#     del item['id']
#     item['likes'] = randint(1, 100)
#     item['is_online'] = True
#     item['is_banned'] = False
#     item['mail'] = None
#     item['now'] = datetime.datetime.now()


# new_str_json = json.dumps(data, indent=2)  # сериализация
# >>>: TypeError: Object of type datetime is not JSON serializable


# нужно преобразовать объект даты в один из базовых типов
for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(1, 100)
    item['is_online'] = True
    item['is_banned'] = False
    item['mail'] = None
    item['now'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # преобразование объекта даты в строку

new_str_json = json.dumps(data, indent=2)  # сериализация
pprint(new_str_json)
# ('{\n'
#  '  "response": {\n'
#  '    "count": 32363,\n'
#  '    "items": [\n'
#  '      {\n'
#  '        "first_name": "Sonya",\n'
#  '        "last_name": "Kargina",\n'
#  '        "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",\n'
#  '        "likes": 80,\n'
#  '        "is_online": true,\n'
#  '        "is_banned": false,\n'
#  '        "mail": null,\n'
#  '        "now": "2024-04-21 12:49:17"\n'
#  '      },\n'
#  '      {\n'
#  '        "first_name": "Slava",\n'
#  '        "last_name": "Kholod",\n'
#  '        "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg",\n'
#  '        "likes": 40,\n'
#  '        "is_online": true,\n'
#  '        "is_banned": false,\n'
#  '        "mail": null,\n'
#  '        "now": "2024-04-21 12:49:17"\n'
#  '      }\n'
#  '    ]\n'
#  '  }\n'
#  '}')
print(type(data['response']['items'][0]['now']))
# >>>: <class 'str'>

# JSON часто нужно сохранять в файле
with open('new_json.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

with open('new_json_indent.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


# чтение JSON из файла
with open('new_json_indent.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(d)