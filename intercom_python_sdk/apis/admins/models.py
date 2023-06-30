
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

from ...core.model_base import ModelBase


class TeamPriorityLevel(ModelBase):
    """
    Represents a team priority level.

    Args:
        primary_team_ids (List[int]): The IDs of the primary teams.
        secondary_team_ids (List[int]): The IDs of the secondary teams.

    Attributes:
        Identical to the arguments.
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

    Args:
        type (str): The type of the admin.
        id (str): The ID of the admin.
        name (str): The name of the admin.
        email (str): The email of the admin.
        job_title (str): The job title of the admin.
        has_inbox_seat (bool): Whether the admin has an inbox seat or not.
        team_ids (List[str]): The IDs of the teams the admin belongs to.
        avatar (str): The avatar URL of the admin.
        team_priority_level (TeamPriorityLevel): The team priority level of the admin.
        away_mode_enabled (bool, optional): Whether the admin's away mode is enabled or not. Defaults to False.
        away_mode_reassign (bool, optional): Whether the admin's away mode reassign is enabled or not. Defaults to False.

    Attributes:
        Identical to the arguments.
    """
    
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type')
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__email = kwargs.get('email')
        self.__job_title = kwargs.get('job_title')
        self.__has_inbox_seat = kwargs.get('has_inbox_seat')
        self.__team_ids = kwargs.get('team_ids')
        self.__avatar = kwargs.get('avatar')
        self.__team_priority_level = kwargs.get('team_priority_level')
        self.__away_mode_enabled = kwargs.get('away_mode_enabled')
        self.__away_mode_reassign = kwargs.get('away_mode_reassign')
    
    @property
    def type(self):
        """
        Get the type of the admin.

        Returns:
            str: The type of the admin.
        """
        return self.__type
    
    @property
    def id(self):
        """
        Get the ID of the admin.

        Returns:
            str: The ID of the admin.
        """
        return self.__id
    
    @property
    def name(self):
        """
        Get the name of the admin.

        Returns:
            str: The name of the admin.
        """
        return self.__name
    
    @property
    def email(self):
        """
        Get the email of the admin.

        Returns:
            str: The email of the admin.
        """
        return self.__email
    
    @property
    def job_title(self):
        """
        Get the job title of the admin.

        Returns:
            str: The job title of the admin.
        """
        return self.__job_title
    
    @property
    def has_inbox_seat(self):
        """
        Check if the admin has an inbox seat.

        Returns:
            bool: True if the admin has an inbox seat, False otherwise.
        """
        return self.__has_inbox_seat
    
    @property
    def team_ids(self):
        """
        Get the IDs of the teams the admin belongs to.

        Returns:
            List[str]: The IDs of the teams the admin belongs to.
        """
        return self.__team_ids
    
    @property
    def avatar(self):
        """
        Get the avatar URL of the admin.

        Returns:
            str: The avatar URL of the admin.
        """
        return self.__avatar
    
    @property
    def team_priority_level(self):
        """
        Get the team priority level of the admin.

        Returns:
            TeamPriorityLevel: The team priority level of the admin.
        """
        return self.__team_priority_level
    
    @property
    def away_mode_enabled(self):
        """
        Check if the admin's away mode is enabled.

        Returns:
            bool: True if the admin's away mode is enabled, False otherwise.
        """
        return self.__away_mode_enabled
    
    @property
    def away_mode_reassign(self):
        """
        Check if the admin's away mode reassign is enabled.

        Returns:
            bool: True if the admin's away mode reassign is enabled, False otherwise.
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
    
    def set_away_mode(self, enabled: bool = True):
        """
        Set the admin's away mode.

        Args:
            enabled (bool, optional): Whether the admin's away mode should be enabled or disabled. Defaults to True.
        """
        pass

    def set_reassign_mode(self, enabled: bool = True):
        """
        Set the admin's away mode reassign.

        Args:
            enabled (bool, optional): Whether the admin's away mode reassign should be enabled or disabled. Defaults to True.
        """
        pass
