from bs4 import BeautifulSoup
import requests
# from csv import writer
# from tqdm import tqdm
import pandas as pd

keliones = []
# Iteruojame per visus puslapius
for i in range(1, 6):
    # Priskyriame mus dominantį puslapį
    url = f'https://www.kelioniulaikas.lt/keliones/autobusu/pazintines?page={i}'
    # Nuskaitome visą svetainę
    page = requests.get(url)

    # Visas HTML dokumentas patalpintas bus į kintamąjį soup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Paimame visas keliones į vieną konteinerį
    products = soup.find_all("article", class_="travel-grid")

    for product in products:
        titles = product.find("div", class_ = "content-title")
        title = titles.find("a").text
        countries = product.find("ul", class_="countries-list")
        country = countries.find("a", class_="address").text
        days = product.find("div", class_="marks")
        day = days.find_all("span")[1].text
        day = int(day[:-2])
        info1 = [title, country, day]
        # Iteruojame per datas ir kainas
        details = product.find_all("div", class_="row")
        for detail in details:
            dates = detail.find("div", class_="col-4 col-date").text
            prices = detail.find(class_="date-price").text
            # Nuimame valiutos (Euro) simbolį ir paverčiame tekstą į realų skaičių
            price = float(prices[:-1])
            ppd = price / day
            price_per_day = "{:.2f}".format(ppd)
            info2 = [dates, price, price_per_day]
            keliones.append(info1+info2)
            df = pd.DataFrame(keliones, columns=['Title','Country', 'Dates', 'Price, Euro', 'Days', 'Price per day, Eur'])
            df.to_excel('kelioniu_laikas.xlsx', index=False)


