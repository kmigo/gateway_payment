
from setuptools import setup, find_packages

setup(
    name="gateway-payment",
    version="1.0.9",
    packages=['gateway_payment'],
    include_package_data=True,
    description="Utilitários para gateways de pagamento",
    author="Patrick Soares",
    author_email="tk_patrick@hotmail.com",
    install_requires=[
        "requests"
    ],
    python_requires=">=3.9.16",
)
