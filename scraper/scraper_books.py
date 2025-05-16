import requests
import re
from bs4 import BeautifulSoup
from scraper.book import Book

class BookScraper:
    BASE_URL = "https://books.toscrape.com/catalogue/"
    START_URL = "https://books.toscrape.com/index.html"

    def scrape_page(self, url: str) -> list:
        books = []
        response = requests.get(url)
        if response.status_code != 200:
            return books

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title = article.h3.a["title"]

            price_text = article.find("p", class_="price_color").text.strip()
            price_str = re.sub(r"[^\d.]", "", price_text)
            price = float(price_str)

            availability = article.find("p", class_="instock availability").text.strip()
            rating = article.p["class"][1]  # ex: ['star-rating', '3']

            book = Book(title, price, availability, rating)
            books.append(book)

        return books


    def scrape_all(self, pages=50) -> list:
        all_books = []
        all_books += self.scrape_page(self.START_URL)

        for i in range(2, pages + 1):
            url = f"{self.BASE_URL}page-{i}.html"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Page {i} non disponible. FIN SCRAPING")
                break
            books = self.scrape_page(url)
            all_books += books

        return all_books
