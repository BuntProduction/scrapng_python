class Book:
    def __init__(self, title: str, price: float, availability: str, rating: str):
        self.title = title
        self.price = price
        self.availability = availability
        self.rating = rating

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "rating": self.rating
        }

    def __str__(self):
        return f"{self.title} | {self.price}€ | {self.availability} | {self.rating}"
