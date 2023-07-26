"""
# Admins API

`apis/admins/api.py`

This module contains the AdminsAPI class, which defines a client for the Admins API.
It is used to interact with the Intercom Admins API [1] as defined in the Intercom API Reference [2].

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/admins
- [2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
from typing import Union

# External
from uplink import (
    get, put,
    returns, json,
    response_handler,
    Body
)

# From Current API
from .schemas import (
    AdminSchema,
    AdminListSchema,
)
from .models import Admin, AdminList

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@json
@response_handler(catch_api_error)
class AdminsAPI(APIBase):
    """ Admins API Client. """
    URI = "/admins/"

    @returns(AdminSchema)  # type: ignore
    @get("/me")  # We are adding a leading slash here because we actually WANT to ignore the /admins URI in this case.
    def me(self):
        """ Get the current admin user.

        Returns:
            Admin: The current admin user.
        """

    @returns(AdminSchema)  # type: ignore
    @put("{admin_id}/away")
    def __set_away_by_id(self, admin_id: Union[str, int], data: Body(type=dict)):  # type: ignore
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
        return self.__set_away_by_id(admin_id, {"away_mode_enabled": away, "away_mode_reassign": reassign})

    @returns(AdminListSchema)  # type: ignore
    @get("")
    def list_admins(self):
        """ List all admins.

        Returns:
            AdminList: The list of admins.
        """

    @returns(AdminSchema)  # type: ignore
    @get("{admin_id}")
    def get_admin_by_id(self, admin_id: Union[str, int]):
        """ Get an admin by ID.

        Args:
            admin_id (Union[str, int]): The ID of the admin.

        Returns:
            Admin: The admin.
        """

    def get_admin_by_email(self, email: str) -> Union[Admin, None]:
        """ Get an admin by email.

        Args:
            email (str): The email of the admin.

        Returns:
            Admin: The matching Admin object. None if no match found.
        """
        admins_list = self.list_admins()
        admins_list.admins = [admin for admin in admins_list.admins if admin.email == email]  # type: ignore
        return admins_list.admins[0] if admins_list.admins else None

    def get_admins_by_team_id(self, team_id: Union[int, str]) -> AdminList:
        """ Get all admins by team ID.

        Args:
            team_id (Union[int, str]): The ID of the team.

        Returns:
            AdminList: The list of admins. None if no match found.
        """
        admins_list = self.list_admins()
        admins_list.admins = [admin for admin in admins_list.admins if team_id in admin.team_ids]  # type: ignore
        return admins_list
