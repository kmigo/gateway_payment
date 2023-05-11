from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5


def test_update_bank_account(example_update_bank_account):
    res = pagarmev5.receivers.update_account_bank(example_update_bank_account)
    json = res.json()
    assert res.status_code == 200


def test_get_balance_account():
    res = pagarmev5.receivers.get_balance(
        {'recipient_id': 're_clhjel3cd02pg019tj9pb3bah'})
    json = res.json()
    assert res.status_code == 200


def test_create_balance_withdrawal():
    res = pagarmev5.receivers.create_balance_withdrawal(
        {"recipient_id": "re_clhjel3cd02pg019tj9pb3bah", "amount": 100})
    json = res.json()
    assert res.status_code == 412


def test_all_withdrawals():
    res = pagarmev5.receivers.get_all_balance_withdrawal(
        {'recipient_id': 're_clhjel3cd02pg019tj9pb3bah'})
    assert res.status_code == 200


def test_update_config():
    res = pagarmev5.receivers.update_config_transference(
        {
            "recipient_id": "re_clhjel3cd02pg019tj9pb3bah",
            "transfer_enabled": False,
            "transfer_interval": "Daily",
            "transfer_day": 0

        })
    assert res.status_code == 200

"""
def test_update_config_antecipation_automatic():
    res = pagarmev5.receivers.update_automatic_anticipation_settings(
        {
            "recipient_id": "re_clhjel3cd02pg019tj9pb3bah",
            "enabled": True,
            "type": "full",
            "volume_percentage": "50",
            "days": [
                1,
                3,
                5
            ],
            "delay": None
        }
    )
    assert res.json() == 200
"""