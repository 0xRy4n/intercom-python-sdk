"""
    Intercom Python SDK

    The unofficial Intercom Python SDK.

    The version of the OpenAPI document: 2.9
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "intercom-python-sdk"
VERSION = "0.1.0-dev"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "setuptools",
    "uplink",
    "bs4",
    "marshmallow",
    "validator-collection",
    "faker",
    "requests"
]

setup(
    name=NAME,
    version=VERSION,
    description="Intercom Python SDK",
    author="Ryan Gordon",
    author_email="mail@ry4n.sh",
    url="https://github.com/0xRy4n/intercom-python-sdk.git",
    keywords=["Intercom", "Intercom API", "Intercom Python SDK", "Intercom Python API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    package_data={"": ["py.typed", "*.pyi"]},
    include_package_data=True,
    license="MIT",
    long_description="""\
    The unofficial Intercom Python SDK.
    """
)