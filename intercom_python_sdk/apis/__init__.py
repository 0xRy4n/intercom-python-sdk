"""
# Intercom Python SDK APIs

This directory contains the various API modules for the Intercom Python SDK.
Each API is implemented in it's own directory, and contains three files:

- `api.py` : Contains the API class, which is used to make API calls.
- `models.py` : Contains the model classes, which are used to represent objects returned from the API.
- `schemas.py` : Contains the schema classes, which are used to represent objects sent to the API (marshmallow).

It is not intended in most cases for you to interact with these modules directly. Instead, to access an API client,
you can use the `intercom_python_sdk.intercom.Intercom` object, which provides a convenient interface for accessing all the
available APIs. 

Alternatively, to access a specific API client, you can use the `intercom_python_sdk.core.api_base.create_api_client` function 
to build an API client interface. 

APIs can be enabled in the `Intercom` object via the `tags_to_api` module.
"""

from .tags_to_api import tags_to_api_dict
