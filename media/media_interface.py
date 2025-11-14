from abc import ABC, abstractmethod

class MediaInterface(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_creator(self):
        pass

    @abstractmethod
    def get_year(self):
        pass

    @abstractmethod
    def get_genre(self):
        pass

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def set_rating(self, rating):
        pass
