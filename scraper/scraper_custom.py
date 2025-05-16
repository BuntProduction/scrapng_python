import requests
from bs4 import BeautifulSoup
import time
import random
import os
import csv


def scrape_amazon_webcam_titles(base_url, max_titles=100, max_pages=5):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) "
            "Gecko/20100101 Firefox/113.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/"
    }

    titles = []
    page = 1

    while len(titles) < max_titles and page <= max_pages:
        paged_url = f"{base_url}&page={page}"
        print(f"Scraping page {page}...")
        response = requests.get(paged_url, headers=headers)

        if response.status_code != 200:
            print(f"Erreur {response.status_code} à la page {page}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        title_tags = soup.select("h2.a-size-base-plus span")

        if not title_tags:
            print(f"Aucun produit trouvé à la page {page}. Arrêt.")
            break

        new_titles = 0
        for tag in title_tags:
            title = tag.get_text(strip=True)
            if title and title not in titles:
                titles.append(title)
                new_titles += 1
            if len(titles) >= max_titles:
                break

        print(f"{new_titles} nouveaux titres ajoutés (total : {len(titles)})")

        if new_titles == 0:
            print("Aucun nouveau titre. -----------------FIN----------")
            break

        page += 1
        time.sleep(random.uniform(7, 15))  # Pause entre pages

    return titles


def export_titles_to_csv(titles, filepath="data/custom_products.csv"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title"])  # En-tête
        for title in titles:
            writer.writerow([title])

    print(f"{len(titles)} titres exportés dans {filepath}")
