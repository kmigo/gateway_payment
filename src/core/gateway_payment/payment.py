from abc import ABC,abstractclassmethod

class Payment(ABC):
    @abstractclassmethod
    def create(self,data):
        pass

    @abstractclassmethod
    def find_by(self,data):
        pass
    @abstractclassmethod
    def refund(self,data):
        pass
    @abstractclassmethod
    def find_all(self):
        pass
