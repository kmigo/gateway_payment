from src.implementations.gateway.pagarmev5.pagarme_v5 import pagarmev5
payload = {
    "customer": {
        "phones": {"home_phone": {
                "country_code": "55",
                "area_code": "21",
                "number": "000000000"
            }},
        "name": "Tony Stark",
        "email": "avengerstark@ligadajustica.com.br",
        "type": "individual",
        "document": "03154435026",
        "document_type": "cpf"
    },
    "items": [
        {
            "amount": 2990,
            "description": "Chaveiro do Tesseract",
            "quantity": 1,
            "code": 123
        }
    ],
    "payments": [
        {
            "credit_card": {
                "card": {
                    "number": "4000000000000010",
                    "holder_name": "Tony Stark",
                    "exp_month": 1,
                    "exp_year": 25,
                    "cvv": "351"
                },
                "installments": 1,
                "statement_descriptor": "AVENGERS"
            },
            "payment_method": "credit_card"
        }
    ]
}
print(pagarmev5.payment.create(payload))