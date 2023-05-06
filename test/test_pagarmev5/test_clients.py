from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_client(example_create_client):
    res = pagarmev5.clients.create(example_create_client)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json

def test_client_get():
    res = pagarmev5.clients.get({'customer_id':"cus_YB0QaMdsJ4CqQrNK"})
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json

def test_client_all():
    res = pagarmev5.clients.all({
        "name":"Tony Stark",
        "page":"1",
        "size":"10"
    })
    json = res.json()
    assert res.status_code == 200
    assert len(json['data']) >1

def test_client_update():
    res = pagarmev5.clients.update(
    {'customer_id':'cus_YB0QaMdsJ4CqQrNK',
     'name':'Tony Stark'
     }
    )
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json