
from setuptools import setup, find_packages
setup(
    name="gateway-payment",
    version="0.01",
    packages=["gateway_payment","gateway_payment.src"],
    include_package_data=True,
    description="Utilitários para gateways de pagamento",
    author="Patrick Soares",
    author_email="tk_patrick@hotmail.com",
    package_dir={"gateway_payment": ""},
    install_requires=[
        "requests",
        "pagarme-python==4.0.2",
        "pydantic",
        "python-dotenv",
        "pytest"

    ],
    python_requires=">=3.9.16",
)
