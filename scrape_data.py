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
for product in products:
    titles = product.find("div", class_ = "content-title")
    title = titles.find("a").text
    print(title)

# lists = soup.find_all('div', class_="row")
# for list in lists:
#     title = list.find('div', class_="").text
#     print(title)
    # countries = list.find('a', class_="address").text
    # for country in countries:
    #     state = country.find('a', class_='address')
    
    # cells = soup.find_all('div', class_='content')
    # for cell in cells:
    # trukme = list.find('div', class_="marks").text
    # price = list.find('span', class_="date-price").text
    # Removing Euro mark and converting text to float
    # price = float(price[:-1])
    # title = list.find('div', class_="content-title").text
    # country = list.find('a', class_="address").text
    # date = list.find('div', class_="col-4 col-date").text
    # dates = list.find('div', class_="col-4 col-date").text
    # date = dates.find("div", class_="col-4 col-date")

       
    # print(countries)
    # print (title)
# with open('tours.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ["City", "info", "Price", "Data", "Description"]
#     thewriter.writerow(header)
#     for list in lists:
#         city = list.find('a', class_="link").text.replace('\n', '')
#         info = list.find('div', class_ = "info-block hidden-xs").text.replace('\n', '')
#         price = list.find('div', class_ = "price text-center pull-left").text.replace('\n', '')
#         description = list.find('div', class_="offer-description clearfix").text.replace('\n', '')
#         data = [city, info, price, description]
#         thewriter.writerow(data)

