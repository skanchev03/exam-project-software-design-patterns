class Book:
    def __init__(self, book_title, book_author, book_year, book_genre):
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.book_genre = book_genre
        self.rating = None

    def set_rating(self, rating):
        self.rating = rating
