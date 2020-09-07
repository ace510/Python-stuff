import requests
import bs4

payload = 'https://scryfall.com/random?q=cmc%3D8&as=text'

requesty = requests.get(payload)

print(requesty.text)