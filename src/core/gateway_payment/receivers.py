from abc import ABC,abstractclassmethod

class Receivers(ABC):
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