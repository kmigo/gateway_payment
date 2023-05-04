from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_client(example_create_client):
    res = pagarmev5.clients.create(example_create_client)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json