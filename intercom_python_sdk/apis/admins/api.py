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

# Built-ins
import functools
from typing import Union

# External
from uplink import (
    get, put, post, 
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query
)

# From Current API
from .schemas import AdminSchema, TeamPriorityLevelSchema
from .models import Admin, TeamPriorityLevel

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@json
@response_handler(catch_api_error)
class AdminsAPI(APIBase):
    URI = "/admins/"

    @returns(AdminSchema(many=False)) # type: ignore
    @get("me")
    def me(self):
        """ Get the current admin user. 
        
        Returns:
            Admin: The current admin user.
        """

    @returns(AdminSchema(many=False)) # type: ignore
    @put("{admin_id}/away")
    def __set_away_by_id(self, admin_id: Union[str, int], data: Body(type=dict)): # type: ignore
        """ Set the away status of an admin. Internal method for `set_away_by_id`."""

    def set_away_by_id(self, admin_id: Union[str, int], away: bool = True, reassign: bool = True):
        """ Set the away status of an admin. Convienience interface for `__set_away_by_id`.

        Args:
            admin_id (Union[str, int]): The ID of the admin.
            away_mode_enabled (bool): Whether the admin is away. Defaults to True.
            away_mode_reassign (bool): Whether to reassign conversations. Defaults to True.

        Returns:
            HTTPResponse: The response from the API.
        """
        return self.__set_away_by_id(admin_id, {"away_mode_enabled":away, "away_mode_reassign":reassign})