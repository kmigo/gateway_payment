from src.core.gateway_payment.gateway_payment import GatewayPayment,Payment,Cards,Clients
from requests import request
import base64
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

pagarmev5 = PagarmeV5()