from bs4 import BeautifulSoup
import requests
from csv import writer

# Priskyriame mus dominantį puslapį
url = 'https://www.kelioniulaikas.lt/keliones/autobusu/pazintines'
# Nuskaitome visą svetainę
page = requests.get(url)

# Visas HTML dokumentas patalpintas bus į kintamąjį soup
soup = BeautifulSoup(page.content, 'html.parser')
# Paimame visas keliones į vieną konteinerį
products = soup.find_all("article", class_="travel-grid")
print(len(products))
