from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_receiver(example_create_receiver):
    res = pagarmev5.receivers.create(example_create_receiver)
    json = res.json()
    assert res.status_code == 200