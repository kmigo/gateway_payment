
from setuptools import setup, find_packages

setup(
    name="gateway_payment",
    version="1.0.0",
    description="Utilitários para gateways de pagamento",
    author="Patrick Soares",
    author_email="tk_patrick@hotmail.com",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "requests",
        "colorama",
        "argparse>=1.4.0",
        "pagarme-python==4.0.2",
        "pydantic",
        "python-dotenv",
        "pytest"

    ],
    entry_points={
        "console_scripts": [
            "fsv=main:main"
        ]
    },
    python_requires=">=3.9.16",
)