from setuptools import setup

with open("README.rst", "r") as readme_fd:
    long_description = readme_fd.read()

setup(
    name="dynamorm",
    version="0.12.0",
    description="DynamORM is a Python object & relation mapping library for Amazon's DynamoDB service.",
    long_description=long_description,
    author="Evan Borgstrom",
    author_email="evan@borgstrom.ca",
    url="https://github.com/NerdWalletOSS/DynamORM",
    license="Apache License Version 2.0",
    python_requires=">=3.11",
    install_requires=["blinker>=1.9,<3.0", "boto3>=1.42.23,<2.0", "packaging>=25.0"],
    extras_require={
        "marshmallow": ["marshmallow>=3.0,<5.0"],
        "schematics": ["schematics>=2.1.0,<3.0"],
        "test": [
            "pytest>=7.0",
            "pytest-mock>=3.0",
            "python-dateutil>=2.8",
        ],
        "dev": [
            "pytest>=7.0",
            "pytest-mock>=3.0",
            "python-dateutil>=2.8",
            "black>=22.0",
            "tox>=4.0",
        ],
    },
    packages=["dynamorm", "dynamorm.types"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
    ],
)
