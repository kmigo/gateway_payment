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
    def all(self,data):
        assert 'size' in data
        assert 'page' in data
        res = request('GET',self.base_url+f'/recipients',headers=self.headers,params=data)
        return res
    def get(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('GET',self.base_url+f'/recipients/{recipient_id}',headers=self.headers)
        return res
    def update(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('PUT',self.base_url+f'/recipients/{recipient_id}',headers=self.headers,json=data)
        return res

class ClientsPagarmev5(Clients):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
    def create(self,data):
        res = request('POST',self.base_url+f'/customers',headers=self.headers,json=data)
        return res
    def all(self,data):
        assert 'page' in data
        assert 'size' in data
        res = request('GET',self.base_url+f'/customers',headers=self.headers,params=data)
        return res
    
    def get(self,data):
        assert 'customer_id' in data
        customer_id = data.pop('customer_id')
        res = request('GET',self.base_url+f'/customers/{customer_id}',headers=self.headers)
        return res
    
    def update(self,data):
        assert 'customer_id' in data
        customer_id = data.pop('customer_id')
        res = request('PUT',self.base_url+f'/customers/{customer_id}',headers=self.headers,json=data)
        return res
        
    
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
        raise NotImplemented
    def find_all(self,data):
        raise NotImplemented
    def find_by(self,data):
        assert 'order_id' in data
        order_id =data['order_id']
        res = request('GET',self.base_url+f'/orders/{order_id}',headers=self.headers,json=data)
        return res
    def find_all(self,data):
        raise NotImplemented
    def get_all_refounds(self,data):
        raise NotImplemented
    def refund(self,data):
        raise NotImplemented
    def update_payment_test(self,data):
        raise NotImplemented


class PagarmeV5(GatewayPayment):
    def __init__(self) -> None:
        super().__init__()
        import os
        key_private=os.environ.get('payment_key')
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