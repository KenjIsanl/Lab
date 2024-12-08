import doctest


# TODO: описать класс


class Book:
    def __init__(self, title: str, genre: str):
        self.title = title
        self.genre = genre

    book_1 = Book("K", "Romance")
    book_2 = Book("L", "Romance")

    def _genre_valid(self) -> bool:
        valid_genres = ["Fantasy", "Mystery", "Romance", "Thriller", "Detective"]
        return self.genre in valid_genres

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    print(book_1.title, book_1.genre)
    print(book_2.title, book_2.genre)


# TODO: описать ещё класс
class Games:
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price

    def _title_valid(self) -> bool:
        valid_titles = ["Genshin", "HSR", "Stalker"]
        return self.title in valid_titles

    def calculate_discounted_price(self, discount: float) -> float:
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price


# TODO: и ещё один
class Computer:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def change_brand(self, new_brand: str) -> None:
        self.brand = new_brand

    def _model_valid(self) -> bool:
        valid_models = ["ASUS TUF", "HUAWEI"]
        return self.model in valid_models


if __name__ == "__main__":
    doctest.testmod()
