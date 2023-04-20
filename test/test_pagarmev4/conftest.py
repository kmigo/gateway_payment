import pytest

card_success='4000000000000010'
card_not_autorized = '4000000000000028'
card_success_proccessing_refound ='4000000000000077'
card_proccessing_failed ='4000000000000044'
card_success_processing_success = '4000000000000036'
card_success_processing_cancel ='4000000000000051'
card_paid_chargeback ='4000000000000069'


@pytest.fixture()
def user_data_create():
    return {
    "external_id": "#123456789",
  "name": "João das Neves",
  "type": "individual",
  "country": "br",
  "email": "joaoneves@norte.com",
  "documents": [
    {
      "type": "cpf",
      "number": "11111111111"
    }
  ],
  "phone_numbers": [
    "+5511999999999",
    "+5511888888888"
  ],
  "birthday": "1985-01-01"}

@pytest.fixture()
def data_card():
    return {
        "card_expiration_date": "1122", 
    "card_number": "4018720572598048",
    "card_cvv": "123", 
    "card_holder_name": "Aardvark Silva"
    }

@pytest.fixture()
def user_paid():
    
    return 