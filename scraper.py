import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]

    data.append([name, price, rating])

# Save to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])
    writer.writerows(data)

print("✅ Data scraped and saved to products.csv")
