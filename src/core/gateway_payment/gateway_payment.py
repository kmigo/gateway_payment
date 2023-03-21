from abc import ABC
from src.core.gateway_payment.payment import Payment
from src.core.gateway_payment.cards import Cards
from src.core.gateway_payment.clients import Clients


class GatewayPayment(ABC):
    payment:Payment
    cards:Cards
    clients:Clients
    key:str
   
    