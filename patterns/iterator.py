class MediaIterator:
    def __init__(self, media_list):
        self._media_list = media_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._media_list):
            result = self._media_list[self._index]
            self._index += 1
            return result
        raise StopIteration
