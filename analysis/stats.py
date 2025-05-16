import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def load_books(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    # Forcer le typage float pour le prix
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Supprimer les lignes avec un prix non valide
    df = df.dropna(subset=["price"])

    return df

def describe_prices(df: pd.DataFrame):
    print("Statistiques descriptives sur les prix :")
    print(df["price"].describe())

def availability_counts(df: pd.DataFrame):
    print("\nDisponibilité des livres :")
    disponibles = df["availability"].str.contains("In stock", case=False).sum()
    indisponibles = len(df) - disponibles
    print(f"Disponibles : {disponibles}")
    print(f"Indisponibles : {indisponibles}")

    print("\nNombre de livres par rating :")
    print(df["rating"].value_counts())

def summary_by_rating(df: pd.DataFrame):
    print("\nPrix moyen par niveau de rating :")
    print(df.groupby("rating")["price"].mean().sort_index())

def plot_price_histogram(df):
    plt.figure()
    df["price"].hist(bins=20)
    plt.title("Distribution des prix")
    plt.xlabel("Prix")
    plt.ylabel("Nombre de livres")
    plt.grid(True)
    plt.savefig("data/histogram_price.png")
    plt.close()

def plot_price_boxplot(df):
    plt.figure()
    plt.boxplot(df["price"])
    plt.title("Boxplot des prix")
    plt.ylabel("Prix")
    plt.savefig("data/boxplot_price.png")
    plt.close()

def plot_price_clusters(df):
    if "price_cluster" not in df.columns:
        print("Clustering non trouvé, price_clustering() d'abord.")
        return

    plt.figure()
    plt.scatter(df.index, df["price"], c=df["price_cluster"], cmap="Set1")
    plt.title("Clustering des livres par prix")
    plt.xlabel("Index")
    plt.ylabel("Prix")
    plt.savefig("data/clustering_price.png")
    plt.close()

def plot_cluster_distribution(df):
    if "price_cluster" not in df.columns:
        print("Clustering non trouvé, price_clustering() avant")
        return

    plt.figure()
    df.boxplot(column="price", by="price_cluster")
    plt.title("Boxplot des prix par cluster")
    plt.suptitle("")
    plt.xlabel("Cluster")
    plt.ylabel("Prix")
    plt.savefig("data/cluster_boxplot.png")
    plt.close()

def price_clustering(df, n_clusters=3):
    X = df[["price"]]
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    df["price_cluster"] = model.fit_predict(X)
    return df

def summary_by_cluster(df):
    if "price_cluster" not in df.columns:
        print("Clustering non trouvé, il faut appeler price_clustering() avant")
        return None
    return df.groupby("price_cluster")["price"].describe()
