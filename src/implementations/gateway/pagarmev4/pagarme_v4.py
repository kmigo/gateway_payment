from src.core.gateway_payment.gateway_payment import GatewayPayment,Payment,Cards,Clients
import pagarme

class PaymentPagarmeV4(Payment):
    root:GatewayPayment
    
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.root = root
        
    def create(self,data):
        return pagarme.transaction.create(data)

    
    def find_by(self,data):
        return pagarme.transaction.find_by(data)
   
    def refund(self,id,data):
        return pagarme.transaction.refund(id,data)
   
    def find_all(self):
        return pagarme.transaction.find_all()
    
    def capture(self,id,data):
        return pagarme.transaction.capture(id,data)
   
    def get_all_refounds(self):
        return pagarme.refund.refunds()
    
    def update_payment_test(id,data):
        return pagarme.transaction.pay_bolet(data)

class CardsPaymentV4(Cards):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.root = root

    def create(self,data,id_customer=None):
        if id_customer:
            data['customer_id'] = id_customer
        return pagarme.card.create(data)
    
    def update(self,data):
        raise NotImplemented

  
    def get_card(self,data):
        return pagarme.card.find_by(data)

    def all(self,data={}):
        assert isinstance(data,dict), f'The type {type(data)} is not type of {type({})}'
        import requests
        from src.implementations.gateway.pagarmev4.models import CardFilter
        if data != {} : data = CardFilter(**data).dict(exclude_none=True)
        response = requests.request('GET','https://api.pagar.me/1/cards',headers={'content-type':'application/json'},params={**data,
                                                                                                                             'api_key':self.root.key
                                                                                                                             })
        return response.json()

    
    def delete(self,data):
        raise NotImplemented

   
    def refresh(self,data):
        raise NotImplemented

   
    def token(self,data):
        pass

class ClientsPagarmeV4(Clients):
    root:GatewayPayment
    def __init__(self,root:GatewayPayment) -> None:
        super().__init__()
        self.root = root

    def create(self,data):
        return pagarme.card.create(data)
    
    def get(self,data):
        pass
    
    def update(self,data):
        pass
    
    def all(self,data):
        pass


class PagarmeGatewayV4(GatewayPayment):
    key:str
    def __init__(self, key:str) -> None:
        super().__init__()
        self.key=key
        pagarme.authentication_key(key)
        self.payment = PaymentPagarmeV4(self)
        self.cards = CardsPaymentV4(self)
        self.clients = ClientsPagarmeV4(self)

pagarmev4=PagarmeGatewayV4('ak_test_K25D1A2mFSZ4sX6GatWv1ocF80hdCa')