
from setuptools import setup, find_packages
setup(
    name="gateway-payment",
    version="1.0.0",
    packages=["gateway_payment.src.implementations.gateway"],
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
