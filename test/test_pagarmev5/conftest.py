import pytest
import os
os.environ.setdefault('payment_key', "sk_test_xDw9nAxfv7HVykdX")


@pytest.fixture()
def example_order_success_p2p():
    return {
        "items": [
            {
                "amount": 2990,
                "description": "Chaveiro do Tesseract",
                "quantity": 1,
                "code": "1234"
            }
        ],
        "payments": [
            {
                "credit_card": {
                    "card": {
                        "cvv": "351"
                    },
                    "installments": 1,
                    "statement_descriptor": "AVENGERS",
                    "card_id": "card_1xvmvoBIrXtrWJj9"
                },
                "payment_method": "credit_card"
            }
        ],
        "customer_id": "cus_rRQ639VsOyhwM8xk"
    }


@pytest.fixture()
def example_order_success_p2p_split():
    return {
        "items": [
            {
                "amount": 2990,
                "description": "Chaveiro do Tesseract",
                "quantity": 1,
                "code": "1234"
            }
        ],
        "payments": [
            {
                "credit_card": {
                    "card": {
                        "cvv": "351"
                    },
                    "installments": 1,
                    "statement_descriptor": "AVENGERS",
                    "card_id": "card_1xvmvoBIrXtrWJj9"
                },
                "payment_method": "credit_card"
            }
        ],
        "split": [
            {
                "options": {
                    "charge_processing_fee": False,  # vai ser cobrado pelas taxas
                    "charge_remainder_fee": False,  # vai receber o restante da divisao
                    "liable": False  # é responsavel em caso de chargeback
                },
                "amount": 550,
                "type": "flat",  # float ou percent
                "recipient_id": "re_clhc3kxkr0fn2019tqkmr431w"
            }, {
                "options": {
                    "charge_processing_fee": True,
                    "charge_remainder_fee": True,
                    "liable": True
                },
                "recipient_id": "re_clh90m1e10h1r019tk5fh88uk",
                "type": "flat",
                "amount": 2440
            }
        ],
        "customer_id": "cus_rRQ639VsOyhwM8xk"
    }


@pytest.fixture()
def example_order_success():
    return {

  "items": [
    {
      "amount": 2990,
      "description": "Chaveiro do Tesseract",
      "quantity": 1,
      "code": "123"
    }
  ],
  "payments": [
    {
      "credit_card": {
        "card": {
          "cvv": "123"
        },
        "installments": 1,
        "statement_descriptor": "AVENGERS",
        "card_id": "card_1xvmvoBIrXtrWJj9"
      },
      "payment_method": "credit_card"
    }
  ],
  "customer_id": "cus_rRQ639VsOyhwM8xk"
}


@pytest.fixture()
def example_create_receiver():
    return {
        "name": "Teste campos",
        "email": "tstark@avengers.com",
        "description": "Recebedor tony stark",
        "document": "26224451990",
        "type": "individual",
        "default_bank_account": {
            "holder_name": "Tony Stark",
            "holder_type": "individual",
            "holder_document": "26224451990",
            "bank": "341",
            "branch_number": "1234",
            "branch_check_digit": "6",
            "account_number": "12345",
            "account_check_digit": "6",
            "type": "checking",
            "metadata": {
                "key": "value"
            }
        },
        "transfer_settings": {
            "transfer_enabled": False,
            "transfer_interval": "Daily",
            "transfer_day": 0
        },
        "automatic_anticipation_settings": {
            "enabled": True,
            "type": "full",
            "volume_percentage": "50",
            "delay": None
        },
        "metadata": {
            "key": "value"
        }
    }


@pytest.fixture()
def example_create_client():
    return {
        "name": "Tony Stark",
        "email": "tonystarkk@avengers.com",
        "code": "MY_CUSTOMER_001",
        "document": "93095135270",
        "type": "individual",
        "document_type": "CPF",
        "gender": "male",
        "address": {
            "line_1": "20, Rua boa paba, vale encantado",
            "line_2": "casa",
            "zip_code": "29113060",
            "city": "Vila Velha",
            "state": "ES",
            "country": "BR"
        },
        "birthdate": "05/03/1984",
        "phones": {
            "home_phone": {
                "country_code": "55",
                "area_code": "21",
                "number": "000000000"
            },
            "mobile_phone": {
                "country_code": "55",
                "area_code": "21",
                "number": "000000000"
            }
        },
        "metadata": {
            "company": "Avengers"
        }
    }


@pytest.fixture()
def example_update_bank_account():
    from datetime import datetime 
    now = datetime.now() 
    seconds_since_midnight = int((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds())

    return {
        "recipient_id": "re_clh9aem1t00z4019tk5t4qmje",
        "bank_account": {
            "holder_name": "Tony Stark",
            "holder_type": "individual",
            "holder_document": "26224451990",
            "bank": "342",
            "branch_number": "1234",
            "branch_check_digit": "6",
            "account_number": str(seconds_since_midnight),
            "account_check_digit": "6",
            "type": "checking",
            "metadata": {
                "meta_key": "meta_value"
            }
        }
    }


@pytest.fixture()
def example_create_card():
    return {
        "customer_id": "cus_YB0QaMdsJ4CqQrNK",
        "billing_address": {
            "line_1": "20, Rua boa paba, vale encantado",
            "line_2": "casa",
            "zip_code": "29113060",
            "city": "Vila Velha",
            "state": "ES",
            "country": "BR"
        },
        "options": {
            "verify_card": True
        },
        "number": "4000000000000010",
        "holder_name": "Tony Stark",
        "holder_document": "93095135270",
        "exp_month": 1,
        "exp_year": 30,
        "cvv": "351",
        "brand": "Mastercard",
        "label": ""
    }
