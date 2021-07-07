"""Package configuration."""
from setuptools import setup

setup(
    name="ldapldifgen",
    version="0.1",
    install_requires=["click"],
    requires = [
        "setuptools",
        "wheel"
    ],
    entry_points={
        'console_scripts': [
            'ldapldifgen = src.generator:main'
        ]
    },
)