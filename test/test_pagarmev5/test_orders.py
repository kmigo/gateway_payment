from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_order(example_order_success):
    res = pagarmev5.payment.create(example_order_success)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json
    assert 'status' in json
    assert json['status'] == 'paid'

def test_create_order_and_refound(example_order_success):
    res = pagarmev5.payment.create(example_order_success)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json
    assert 'status' in json
    assert json['status'] == 'paid'
    
    charge_id = json['charges'][0]['id']
    payload = {'charge_id':charge_id}
    res_refound = pagarmev5.payment.refund(payload)
    json_refound = res_refound.json()
    assert res_refound.status_code == 200
    

   
    
    

def test_create_order_simple_p2p(example_order_success_p2p):
    res = pagarmev5.payment.create(example_order_success_p2p)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json
    assert 'status' in json
    assert json['status'] == 'paid'

def test_create_order_simple_p2p_split(example_order_success_p2p_split):
    res = pagarmev5.payment.create(example_order_success_p2p_split)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json
    assert 'status' in json
    assert json['status'] == 'paid'
    print(len(json['charges']))

def test_find_by():
    res = pagarmev5.payment.find_by({
        "order_id":'or_7k89rVVFnvuXm9Z2'
    })
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json

