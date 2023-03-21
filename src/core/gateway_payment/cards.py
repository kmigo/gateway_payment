from abc import ABC,abstractclassmethod

class Cards(ABC):
    @abstractclassmethod
    def create(self,data):
        pass
    @abstractclassmethod
    def update(self,data):
        pass

    @abstractclassmethod
    def get_card(self,data):
        pass

    @abstractclassmethod
    def all(self,data={}):
        pass

    @abstractclassmethod
    def delete(self,data):
        pass

    @abstractclassmethod
    def refresh(self,data):
        pass

    @abstractclassmethod
    def token(self,data):
        pass