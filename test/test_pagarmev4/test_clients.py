from src.implementations.gateway.pagarmev4.pagarme_v4 import pagarmev4
def test_client_create():
    client =pagarmev4.clients.create({
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
  "birthday": "1985-01-01"})
    assert 'id' in client
    