""" 
# Teams API

`apis/teams/api.py`

This module contains the HelpCenterAPI class, which defines a client for the Teams API.
It is used to interact with the Intercom Help Center API [1] as defined in the Intercom API Reference [2].

---
[1] https://developers.intercom.com/intercom-api-reference/reference/listallteams
[2] https://github.com/intercom/Intercom-OpenAPI
"""


# Built-ins
import functools
from typing import Union, cast

# External
from uplink import (
    get, put, post,
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query,delete
)

# From Current API
from .schemas import (
    TeamSchema,
    AdminPriorityLevelSchema,
    TeamListSchema,
)

from .models import (
    Team,
    AdminPriorityLevel,
    TeamList,
    
)

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error

@response_handler(catch_api_error)
class TeamsAPI(APIBase):
    URI = "/teams/"

    @returns(TeamListSchema(many=False)) # type: ignore 
    @get("")
    def get_all_teams(self):
        """ Get all Teams.

        Returns:
            TeamList: A list of all Teams.
        """
        pass

    
    @returns(TeamSchema(many=False)) # type: ignore
    @get("{team_id}")
    def get_team_by_id(self, team_id: Union[str, int]):
        """ Get a Team by ID.

        Args:
            team_id (Union[str, int]): The ID of the Team.

        Returns:
            Team: The Team with the given ID.
        """
        pass
    

    


