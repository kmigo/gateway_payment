from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_create_card(example_create_card):
    res= pagarmev5.cards.create(example_create_card)
    json = res.json()
    assert res.status_code == 200
    assert 'id' in json

def test_edit_card():pass
    #card_ZQovawRhyphVmjNB