from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5

def test_update_bank_account(example_update_bank_account):
    res = pagarmev5.receivers.update_account_bank(example_update_bank_account)
    json = res.json()
    assert res.status_code == 200
    