""" 
====================
Admins API
====================
`apis/admins/api.py`

This module contains the AdminsAPI class, which defines a client for the Admins API.
It is used to interact with the Intercom Admins API [1] as defined in the Intercom API Reference [2].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/admins
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# External Packages
from uplink import get, returns

# From Current API
from .schemas import AdminSchema, TeamPriorityLevelSchema

# From Current Package
from ...core.configuration import Configuration
from ...core.api_base import APIBase

class AdminsAPI(APIBase):
    URI = "/admins"

    @returns(AdminSchema(many=False)) # type: ignore
    @get(f"{URI}/me")
    def me(self):
        """ Get the current admin user. """
        

