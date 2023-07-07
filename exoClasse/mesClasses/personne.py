from abc import ABC, abstractmethod

class Personne(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def modify(self):
        pass