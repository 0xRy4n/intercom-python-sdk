"""
# Articles API Models

`apis/teams/models.py`

This module contains models used to interact with the Intercom Help Center API [1].
These models provide object oriented interfaces for the schemas defined in `apis/teams/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listallteams
"""


# External
from typing import List, TYPE_CHECKING

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import TeamsAPI


class AdminPriorityLevel(ModelBase):
    """
    This model represents a AdminPriorityLevel on Intercom.

    Attributes:
        primary_admin_ids (list): The IDs of the primary admins of the AdminPriorityLevel.
        secondary_admin_ids (list): The IDs of the secondary admins of the AdminPriorityLevel.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_admin_ids: List[int] = kwargs.get("primary_admin_ids", [])
        self.secondary_admin_ids: List[int] = kwargs.get("secondary_admin_ids", [])

    # Properties
    @property
    def api_client(self) -> 'TeamsAPI':
        return self._api_client

    @property
    def primary_admin_ids(self) -> List[int]:
        return self._primary_admin_ids

    @property
    def secondary_admin_ids(self) -> List[int]:
        return self._secondary_admin_ids

    @primary_admin_ids.setter
    def primary_admin_ids(self, primary_admin_ids: List[int]):
        self._primary_admin_ids = primary_admin_ids

    @secondary_admin_ids.setter
    def secondary_admin_ids(self, secondary_admin_ids: List[int]):
        self._secondary_admin_ids = secondary_admin_ids

    @api_client.setter
    def api_client(self, api_client: 'TeamsAPI'):
        self._api_client = api_client


class Team(ModelBase):
    """
    This model represents a Team on Intercom.

    Attributes:
        id (int): The ID of the Team.
        type (str): The type of the Team.
        name (str): The name of the Team.
        admin_ids (list): The IDs of the admins of the Team.
        admin_priority_level (dict): The priority level of the admins of the Team.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id: int = kwargs.get("id", None)
        self.type: str = kwargs.get("type", None)
        self.name: str = kwargs.get("name", None)
        self.admin_ids: List[int] = kwargs.get("admin_ids", [])
        self.admin_priority_level: AdminPriorityLevel = kwargs.get("admin_priority_level", None)

    # Properties
    @property
    def api_client(self) -> 'TeamsAPI':
        return self._api_client

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def name(self) -> str:
        return self._name

    @property
    def admin_ids(self) -> List[int]:
        return self._admin_ids

    @property
    def admin_priority_level(self) -> AdminPriorityLevel:
        return self._admin_priority_level

    @id.setter
    def id(self, id: int):
        self._id = id

    @type.setter
    def type(self, type: str):
        self._type = type

    @name.setter
    def name(self, name: str):
        self._name = name

    @admin_ids.setter
    def admin_ids(self, admin_ids: List[int]):
        self._admin_ids = admin_ids

    @admin_priority_level.setter
    def admin_priority_level(self, admin_priority_level: AdminPriorityLevel):
        self._admin_priority_level = admin_priority_level

    @api_client.setter
    def api_client(self, api_client: 'TeamsAPI'):
        self._api_client = api_client


class TeamList(ModelBase):
    """
    This model represents a TeamList on Intercom.

    Attributes:
        teams (list): The Teams of the TeamList.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.teams: List[Team] = kwargs.get("teams", [])

    # Properties
    @property
    def api_client(self) -> 'TeamsAPI':
        return self._api_client

    @property
    def teams(self) -> List[Team]:
        return self._teams

    @teams.setter
    def teams(self, teams: List[Team]):
        self._teams = teams

    @api_client.setter
    def api_client(self, api_client: 'TeamsAPI'):
        self._api_client = api_client
