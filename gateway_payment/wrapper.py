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
    @abstractclassmethod
    def capture(self,data):
        pass
    @abstractclassmethod
    def get_all_refounds(self):
        pass
    @abstractclassmethod
    def update_payment_test(id,data):
        pass

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

class GatewayPayment(ABC):
    payment:Payment
    cards:Cards
    clients:Clients
    key:str
    receivers:Receivers