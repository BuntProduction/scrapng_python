from scraper.scraper_books import BookScraper
from scraper.exporter import export_books_to_csv
from analysis.stats import (
    load_books,
    describe_prices,
    availability_counts,
    summary_by_rating,
    plot_price_histogram,
    plot_price_boxplot,
    price_clustering,
    plot_price_clusters,
    plot_cluster_distribution,
    summary_by_cluster
)
from scraper.scraper_custom import scrape_amazon_webcam_titles, export_titles_to_csv

def main():
    '''
    # Scraping des livres
    scraper = BookScraper()
    print("Lancement du scraping des livres...")
    books = scraper.scrape_all(pages=50)
    print(f"Nombre total de livres récupérés : {len(books)}")

    # Export livres
    books_path = "data/books.csv"
    export_books_to_csv(books, books_path)

    # Analyse livres
    df_books = load_books(books_path)
    describe_prices(df_books)
    availability_counts(df_books)
    summary_by_rating(df_books)

    # Visualisations
    plot_price_histogram(df_books)
    plot_price_boxplot(df_books)

    # Clustering livres
    df_books = price_clustering(df_books)
    plot_price_clusters(df_books)
    plot_cluster_distribution(df_books)

    # Résumé par cluster
    summary = summary_by_cluster(df_books)
    print("\nRésumé statistique par cluster :")
    print(summary)
    '''


#############################
## Scraping de webcams sur Amazon (titres uniquement)
#############################

    amazon_url = "https://www.amazon.fr/s?k=webcam"
    max_titles = 1000
    max_pages = 20

    webcam_titles = scrape_amazon_webcam_titles(amazon_url, max_titles=max_titles, max_pages=max_pages)

    print("\nTitres récupérés :")
    for i, title in enumerate(webcam_titles, 1):
        print(f"{i}. {title}")

    export_titles_to_csv(webcam_titles)

if __name__ == "__main__":
    main()
