import requests
import bs4

payload = 'https://scryfall.com/random?q=cmc%3D8'

requesty = requests.get(payload)

BeautySoup = bs4.BeautifulSoup(requesty.text,"html5lib")

print(BeautySoup.prettify())