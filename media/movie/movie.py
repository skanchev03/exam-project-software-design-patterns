class Movie:
    def __init__(self, movie_title, movie_director, movie_year, movie_genre):
        self.movie_title = movie_title
        self.movie_director = movie_director
        self.movie_year = movie_year
        self.movie_genre = movie_genre
        self.rating = None

    def set_rating(self, rating):
        self.rating = rating
