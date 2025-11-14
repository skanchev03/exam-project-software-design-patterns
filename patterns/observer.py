class Observer:
    def update(self, media):
        pass

class MediaObserver(Observer):
    def update(self, media):
        print(f"[Observer]New media added: {media.get_details()}")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, media):
        for observer in self._observers:
            observer.update(media)
