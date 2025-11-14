from media.media_interface import MediaInterface

class MusicAdapter(MediaInterface):
    def __init__(self, music):
        self.music = music

    def get_title(self):
        return self.music.music_title

    def get_creator(self):
        return self.music.music_artist

    def get_year(self):
        return self.music.music_year

    def get_genre(self):
        return self.music.music_genre

    def get_rating(self):
        return self.music.rating

    def get_details(self):
        return f"Music: {self.get_title()}, Artist: {self.get_creator()}, Genre: {self.get_genre()}, Year: {self.get_year()}, Rating: {self.get_rating()}"

    def set_rating(self, rating):
        self.music.rating = rating
