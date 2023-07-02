""" 
====================
Data Attributes API
====================
`apis/data_attributes/api.py`

This module contains the Data Attributes API class, which defines a client for the Data Attributes API.
It is used to interact with the Intercom Data Attributes API [1] as defined in the Intercom API Reference [2].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
from typing import Union

# External
from uplink import (
    get, put, post, 
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query
)

# From Current API
from .schemas import (
    DataAttributeSchema,
    DataAttributeListSchema
)

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@json
@response_handler(catch_api_error)
class DataAttributesAPI(APIBase):
    URI = "/data_attributes/"

    @returns(DataAttributeListSchema(many=True)) # type: ignore
    @get("")
    def list_all(self):
        """ List all data attributes. """

    @post("")
    def create(self, attribute: Body(type=DataAttributeSchema)): # type: ignore
        """ Create a new data attribute. """
    

    

