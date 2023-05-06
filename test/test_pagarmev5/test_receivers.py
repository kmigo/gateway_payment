from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_receiver(example_create_receiver):
    res = pagarmev5.receivers.create(example_create_receiver)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json


def test_get_all_receivers():
    res = pagarmev5.receivers.all({'size':10,'page':1})
    json = res.json()
    assert res.status_code == 200
    assert 'data' in json
    assert len(json['data']) > 1

def test_update_receiver():
    data ={
        'recipient_id':'re_clh92csax0h3l019tjux0jjl2',
        'description':"novo",
        "type":"individual"
    }
    res = pagarmev5.receivers.update(data)
    json = res.json()
    assert res.status_code == 200
    assert json['description'] == data['description']

def test_get_receiver():
    recipient_id = 're_clh92csax0h3l019tjux0jjl2'
    res = pagarmev5.receivers.get({
        'recipient_id':recipient_id
    })
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json
