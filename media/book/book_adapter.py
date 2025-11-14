from media.media_interface import MediaInterface

class BookAdapter(MediaInterface):
    def __init__(self, book):
        self.book = book

    def get_title(self):
        return self.book.book_title

    def get_creator(self):
        return self.book.book_author

    def get_year(self):
        return self.book.book_year

    def get_genre(self):
        return self.book.book_genre

    def get_rating(self):
        return self.book.rating

    def get_details(self):
        return f"Book: {self.get_title()}, Author: {self.get_creator()}, Genre: {self.get_genre()}, Year: {self.get_year()}, Rating: {self.get_rating()}"

    def set_rating(self, rating):
        self.book.rating = rating
