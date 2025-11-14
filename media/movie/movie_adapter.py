from media.media_interface import MediaInterface

class MovieAdapter(MediaInterface):
    def __init__(self, movie):
        self.movie = movie

    def get_title(self):
        return self.movie.movie_title

    def get_creator(self):
        return self.movie.movie_director

    def get_year(self):
        return self.movie.movie_year

    def get_genre(self):
        return self.movie.movie_genre

    def get_rating(self):
        return self.movie.rating

    def get_details(self):
        return f"Movie: {self.get_title()}, Director: {self.get_creator()}, Genre: {self.get_genre()}, Year: {self.get_year()}, Rating: {self.get_rating()}"

    def set_rating(self, rating):
        self.movie.rating = rating
