from src.core.gateway_payment.gateway_payment import GatewayPayment,Payment,Cards,Clients,Receivers
from requests import request
import base64


class ReceiversPagarmev5(Receivers):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
    def create(self,data):
        res = request('POST',self.base_url+f'/recipients',headers=self.headers,json=data)
        return res
    def all(self,data):pass
    def get(self,data):pass
    def update(self,data):pass

class ClientsPagarmev5(Clients):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
    def create(self,data):
        res = request('POST',self.base_url+f'/customers',headers=self.headers,json=data)
        return res
    def all(self,data):pass
    def get(self,data):pass
    def update(self,data):pass
    
class CardPagarmeV5(Cards):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
    def create(self,data):
        customer_id = data.pop('customer_id')
        res = request('POST',self.base_url+f'/customers/{customer_id}/cards',headers=self.headers,json=data)
        return res
     
    def update(self,data):
        pass

    
    def get_card(self,data):
        pass

    
    def all(self,data={}):
        pass

    
    def delete(self,data):
        pass

    
    def refresh(self,data):
        pass

    
    def token(self,data):
        pass


class PaymentPagarmeV5(Payment):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
        
    def create(self,data):
        res = request('POST',self.base_url+'/orders',headers=self.headers,json=data)
        return res
    def capture(self,data):
        pass
    def find_all(self,data):pass
    def find_by(self,data):pass
    def find_all(self,data):pass
    def get_all_refounds(self,data):pass
    def refund(self,data):pass
    def update_payment_test(self,data):pass


class PagarmeV5(GatewayPayment):
    def __init__(self) -> None:
        super().__init__()
        key_private="sk_test_xDw9nAxfv7HVykdX"
        usrPass = bytes(f"{key_private}:",'UTF-8')
        b64Val = base64.b64encode(usrPass).decode('utf-8')
        self.headers={"Authorization": "Basic %s" % b64Val,
                "accept": "application/json",
    "content-type": "application/json"
                 }
        self.base_url = 'https://api.pagar.me/core/v5'
        self.payment = PaymentPagarmeV5(self)
        self.clients = ClientsPagarmev5(self)
        self.cards = CardPagarmeV5(self)
        self.receivers = ReceiversPagarmev5(self)

pagarmev5 = PagarmeV5()