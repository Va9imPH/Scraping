import requests
from bs4 import BeautifulSoup as bs

response = requests.get(
    url="https://voyagecosmetics.ru/catalog/novinki"
)

html = bs(response.content, "html.parser")
items = html.select(".col-md-4 > .product-thumb > .product-inner")

# collecting data from the first page
with open("new.txt", "a", encoding="utf-8") as file:
    for el in items:
        title = el.select(".product-title > a")
        file.write(title[0].text + "\n")

# page number
page = 2

# collecting data from other pages
with open("new.txt", "a", encoding="utf-8")as file:
    while True:
        response = requests.get(
                url="https://voyagecosmetics.ru/catalog/novinki" + f"?page={page}"
            )

        html = bs(response.content, "html.parser")
        items = html.select(".col-md-4 > .product-thumb > .product-inner")

        if len(items):
            for el in items:
                title = el.select(".product-title > a")
                file.write(title[0].text + "\n")

            page += 1
        else:
            break
