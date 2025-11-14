class Music:
    def __init__(self, music_title, music_artist, music_year, music_genre):
        self.music_title = music_title
        self.music_artist = music_artist
        self.music_year = music_year
        self.music_genre = music_genre
        self.rating = None

    def set_rating(self, rating):
        self.rating = rating
