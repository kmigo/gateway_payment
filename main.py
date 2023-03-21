from src.implementations.gateway.pagarmev4.pagarme_v4 import pagarmev4

print(pagarmev4.cards.all({'holder_name':"APRO"}))