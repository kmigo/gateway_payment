from abc import ABC,abstractclassmethod

class Clients(ABC):
    @abstractclassmethod
    def create(self,data):
        pass
    @abstractclassmethod
    def get(self,data):
        pass
    @abstractclassmethod
    def update(self,data):
        pass
    @abstractclassmethod
    def all(self,data):
        pass