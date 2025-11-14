from patterns.iterator import MediaIterator
from patterns.observer import Subject

class MediaLibrary(Subject):
    def __init__(self):
        super().__init__()
        self._media_list = []

    def add_media(self, media):
        self._media_list.append(media)
        self.notify(media)

    def remove_media(self, media):
        self._media_list.remove(media)
        self.notify(media)

    def filter_by_genre(self, genre):
        return [m for m in MediaIterator(self._media_list) if m.get_genre() == genre]

    def __iter__(self):
        return MediaIterator(self._media_list)
