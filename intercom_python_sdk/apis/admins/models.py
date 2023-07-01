
"""
====================
Admins API Models
====================
`apis/admins/models.py`

This module contains models used to interact with the Intercom Admins API [1].
These models provide object oriented interfaces for the schemas defined in `apis/admins/schemas.py`.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/admins
"""
# Built-ins
from typing import Union, TYPE_CHECKING, Generic, TypeVar

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# We can use this to allow for type hinting without causing circular imports.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import AdminsAPI


class TeamPriorityLevel(ModelBase):
    """
    Represents a team priority level.

    Attributes:
        See the `TeamPriorityLevelSchema` definition in `apis/admins/schemas.py` for details.
    """
    
    def __init__(self, *args, **kwargs):
        self.__primary_team_ids = kwargs.get('primary_team_ids')
        self.__secondary_team_ids = kwargs.get('secondary_team_ids')
    
    @property
    def primary_team_ids(self):
        """
        Get the IDs of the primary teams.

        Returns:
            List[int]: The IDs of the primary teams.
        """
        return self.__primary_team_ids
    
    @property
    def secondary_team_ids(self):
        """
        Get the IDs of the secondary teams.

        Returns:
            List[int]: The IDs of the secondary teams.
        """
        return self.__secondary_team_ids


class Admin(ModelBase):
    """
    Represents an admin.

    Attributes:
        See the `AdminSchema` definition in `apis/admins/schemas.py` for details.

    Model-Specific Attributes:
        api_client (AdminsAPI): The API Client Instance. Injected via APIProxyInterface
    """
    
    def __init__(self, *args, **kwargs):
        self.__type: str  = kwargs.get('type', '')
        self.__id: str = kwargs.get('id', '')
        self.__name = kwargs.get('name', '')
        self.__email = kwargs.get('email', '')
        self.__job_title = kwargs.get('job_title', '')
        self.__has_inbox_seat = kwargs.get('has_inbox_seat', None)
        self.__team_ids = kwargs.get('team_ids', [])
        self.__avatar = kwargs.get('avatar', {})
        self.__team_priority_level = kwargs.get('team_priority_level', None)
        self.__away_mode_enabled = kwargs.get('away_mode_enabled', None)
        self.__away_mode_reassign = kwargs.get('away_mode_reassign', None)

    @property
    def api_client(self) -> 'AdminsAPI':
        """ Get the API Client Instance. """
        return self._api_client
    
    @api_client.setter
    def api_client(self, api_client: 'AdminsAPI'):
        self._api_client = api_client
    
    @property
    def type(self) -> str:
        """
        Get the type of the admin.

        Returns:
            str: The type of the admin. Empty if unset.
        """
        return self.__type
    
    @property
    def id(self) -> str:
        """
        Get the ID of the admin.

        Returns:
            str: The ID of the admin. Empty if unset.
        """
        return self.__id
    
    @property
    def name(self) -> str:
        """
        Get the name of the admin.

        Returns:
            str: The name of the admin. Empty if unset.
        """
        return self.__name
    
    @property
    def email(self) -> str:
        """
        Get the email of the admin.

        Returns:
            str: The email of the admin. Empty if unset.
        """
        return self.__email
    
    @property
    def job_title(self) -> str:
        """
        Get the job title of the admin.

        Returns:
            str: The job title of the admin. Empty if unset.
        """
        return self.__job_title
    
    @property
    def has_inbox_seat(self) -> Union[bool, None]:
        """
        Check if the admin has an inbox seat.

        Returns:
            bool: True if the admin has an inbox seat. None if unset.
        """
        return self.__has_inbox_seat
    
    @property
    def team_ids(self):
        """
        Get the IDs of the teams the admin belongs to.

        Returns:
            List[str]: The IDs of the teams the admin belongs to. Empty list if unset.
        """
        return self.__team_ids
    
    @property
    def avatar(self) -> dict:
        """
        Get the avatar URL of the admin.

        Returns:
            Dict: A dict containing the type and url of the avatar. Empty dict if unset.
                - type (str): A string with the value "avatar"
                - image_url (str): The URL of the avatar image.
        """
        return self.__avatar
    
    @property
    def team_priority_level(self) -> Union[TeamPriorityLevel, None]:
        """
        Get the team priority level of the admin.

        Returns:
            TeamPriorityLevel: The team priority level of the admin. None if unset.
            See `TeamPriorityLevel` in `apis/admins/models.py` for details.
        """
        return self.__team_priority_level
    
    @property
    def away_mode_enabled(self) -> Union[bool, None]:
        """
        Check if the admin's away mode is enabled.

        Returns:
            bool: True if the admin's away mode is enabled. None if unset.
        """
        return self.__away_mode_enabled
    
    @property
    def away_mode_reassign(self) -> Union[bool, None]:
        """
        Check if the admin's away mode reassign is enabled.

        Returns:
            bool: True if the admin's away mode reassign is enabled. None if unset.
        """
        return self.__away_mode_reassign
    
    @away_mode_enabled.setter
    def away_mode_enabled(self, value):
        """
        Set the admin's away mode to enabled or disabled.

        Args:
            value (bool): The value indicating whether the admin's away mode should be enabled or disabled.
        """
        pass
    
    def set_away(self, enabled: bool = True):
        """
        Set the admin's away mode.

        Reassignment setting kept as its current value. If it cannot be obtained, it will default to True.

        Args:
            enabled (bool, optional): Whether the admin's away mode should be enabled or disabled. Defaults to True.
        """
        reassign = self.away_mode_reassign or True
        self.api_client.set_away_by_id(self.id, away=enabled, reassign=reassign)

    def set_active(self, enabled: bool = False):
        """ Alias for set_away(enabled=False) """
        self.set_away(enabled=False)

    def set_reassign(self, enabled: bool = True):
        """
        Set the admin's away mode reassign.

        Away enabled setting kept as its current value. If it cannot be obtained, it will default to True.

        Args:
            enabled (bool, optional): Whether the admin's away mode reassign should be enabled or disabled. Defaults to True.
        """
        enabled = self.away_mode_enabled or True
        self.api_client.set_away_by_id(self.id, away=enabled, reassign=enabled)
        
