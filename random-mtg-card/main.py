import requests

payload = 'https://scryfall.com/search?q=cmc%3D8&as=text'

requesty = requests.get(payload)

print(requesty.text)