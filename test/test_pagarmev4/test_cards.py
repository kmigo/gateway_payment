from src.implementations.gateway.pagarmev4.pagarme_v4 import pagarmev4

def test_create_cards(data_card):
    
    res = pagarmev4.cards.create(data_card)
    assert 'id' in res
    assert 'date_created' in res
    

def test_get_all_cards():
    
    res = pagarmev4.cards.all({'holder_name':"APRO"})
    assert isinstance(res,list)
    
    res = pagarmev4.cards.all({"customer_id":"13736000"})
    assert isinstance(res,list)
    assert len(res) >= 1

    res = pagarmev4.cards.all({"customer_id":"131736000"})
    assert isinstance(res,list)
    assert len(res) <= 0
