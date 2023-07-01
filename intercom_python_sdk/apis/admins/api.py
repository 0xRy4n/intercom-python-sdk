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

import functools
from typing import Union

# External Packages
from uplink import (
    get,
    put,
    post,
    returns,
    Body,
    error_handler,
    response_handler
)

# From Current API
from .schemas import AdminSchema, TeamPriorityLevelSchema
from .models import Admin, TeamPriorityLevel

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error

class AdminsAPI(APIBase):
    URI = "/admins"

    @returns(AdminSchema(many=False)) # type: ignore
    @get("/me")
    def me(self):
        """ Get the current admin user. 
        
        Returns:
            Admin: The current admin user.
        """

    @response_handler(catch_api_error)
    @put("/{admin_id}/away")
    def __set_away(self, admin_id: Union[str, int], **away: Body):
        """ Set the away status of an admin. Internal method.

        Args:
            admin_id (str, int) The ID of the admin.
            away_mode (dict): The away mode to set.
                - away_mode_enabled (bool): Whether away mode is enabled (required).
                - away_mode_reassign (bool): Whether to reassign conversations (required).
        """

    def set_away_mode(self, admin_id: Union[str, int], away: bool, reassign: bool = True):
        """ Set the away status of an admin. Convenience method.
            
        Args:
            admin_id (str, int) The ID of the admin.
            - away (bool): Whether away mode is enabled (required).
            - reassign (bool): Whether to reassign conversations (required). Defaults to True.

        Returns:
            Admin: The updated admin.
        """
        return self.__set_away(
            admin_id,
            away_mode_enabled=away,
            away_mode_reassign=reassign
        )