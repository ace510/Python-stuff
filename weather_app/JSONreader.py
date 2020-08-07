import json

with open('city.list.json', encoding="utf8") as f:
    data = json.load(f)

for i in data:
    if i['state'] == 'OR' and i['name'][0] == 'H':
        print(i)