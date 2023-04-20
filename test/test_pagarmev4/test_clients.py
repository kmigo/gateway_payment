from src.implementations.gateway.pagarmev4.pagarme_v4 import pagarmev4
def test_client_create(user_data_create):
    client = pagarmev4.clients.create(user_data_create)
    assert 'id' in client
    