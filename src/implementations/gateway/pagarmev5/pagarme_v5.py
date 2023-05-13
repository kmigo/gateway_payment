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
    def update_account_bank(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('PATCH',self.base_url+f'/recipients/{recipient_id}/default-bank-account',headers=self.headers,json=data)
        return res
    def get_balance(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('GET',self.base_url+f'/recipients/{recipient_id}/balance',headers=self.headers)
        return res
    def create_balance_withdrawal(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('POST',self.base_url+f'/recipients/{recipient_id}/withdrawals',headers=self.headers,json=data)
        return res
    def get_balance_withdrawal(self,data):
        assert 'recipient_id' in data
        assert 'withdrawals_id' in data
        recipient_id = data.pop('recipient_id')
        withdrawals_id = data.pop('withdrawals_id')
        res = request('GET',self.base_url+f'/recipients/{recipient_id}/withdrawals/{withdrawals_id}',headers=self.headers)
        return res
    def get_all_balance_withdrawal(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('GET',self.base_url+f'/recipients/{recipient_id}/withdrawals',headers=self.headers)
        return res
    def update_config_transference(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('PATCH',self.base_url+f'/recipients/{recipient_id}/transfer-settings',headers=self.headers,json=data)
        return res
    def update_automatic_anticipation_settings(self,data):
        assert 'recipient_id' in data
        recipient_id = data.pop('recipient_id')
        res = request('PATCH',self.base_url+f'/recipients/{recipient_id}/automatic-anticipation-settings',headers=self.headers,json=data)
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
        assert 'customer_id' in data
        assert 'card_id' in data
        customer_id = data.pop('customer_id')
        card_id=data.pop('card_id')
        res = request('DELETE',self.base_url+f'/customers/{customer_id}/cards/{card_id}',headers=self.headers,json=data)
        return res
    
    def get_card(self,data):
        assert 'customer_id' in data
        assert 'card_id' in data
        customer_id = data.pop('customer_id')
        card_id=data.pop('card_id')
        res = request('GET',self.base_url+f'/customers/{customer_id}/cards/{card_id}',headers=self.headers)
        return res

    
    def all(self,data={}):
        assert 'customer_id' in data
        customer_id = data.pop('customer_id')
        res = request('GET',self.base_url+f'/customers/{customer_id}/cards',headers=self.headers)
        return res
    
    def delete(self,data):
        assert 'customer_id' in data
        assert 'card_id' in data
        customer_id = data.pop('customer_id')
        card_id=data.pop('card_id')
        res = request('DELETE',self.base_url+f'/customers/{customer_id}/cards/{card_id}',headers=self.headers)
        return res
    
    def refresh(self,data):
        assert 'customer_id' in data
        assert 'card_id' in data
        customer_id = data.pop('customer_id')
        card_id=data.pop('card_id')
        res = request('POST',self.base_url+f'/customers/{customer_id}/cards/{card_id}/renew',headers=self.headers)
        return res
    
    def token(self,data):
        raise NotImplemented


class PaymentPagarmeV5(Payment):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.headers  = root.headers
        self.base_url = root.base_url
        
    def create(self,data):
        res = request('POST',self.base_url+'/orders',headers=self.headers,json=data)
        return res

    def find_all(self,data):
        res = request('GET',self.base_url+f'/orders',headers=self.headers,query=data)
        return res
    def find_by(self,data):
        assert 'order_id' in data
        order_id =data['order_id']
        res = request('GET',self.base_url+f'/orders/{order_id}',headers=self.headers)
        return res

    def refund(self,data):
        assert 'charge_id' in data
        assert 'amount' in data
        charge_id = data.pop('charge_id')
        res = request('DELETE',self.base_url+f'/charges/{charge_id}',headers=self.headers,json=data)
        return res
   


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