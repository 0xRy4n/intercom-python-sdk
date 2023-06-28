from .schemas import AdminSchema, TeamPriorityLevelSchema
from ..models import ModelMeta

class Admin(metaclass=ModelMeta):
    def __init__(self, *args, **kwargs):
        # Immutable Properties
        self.__type = kwargs.get('type')
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__email = kwargs.get('email')
        self.__job_title = kwargs.get('job_title')
        self.__has_inbox_seat = kwargs.get('has_inbox_seat')
        self.__team_ids = kwargs.get('team_ids')
        self.__avatar = kwargs.get('avatar')
        self.__team_priority_level = kwargs.get('team_priority_level')

        # Settable properties
        self.__away_mode_enabled = kwargs.get('away_mode_enabled')
        self.__away_mode_reassign = kwargs.get('away_mode_reassign')
    
    # Property Getters

    @property
    def type(self):
        return self.__type
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def job_title(self):
        return self.__job_title
    
    @property
    def has_inbox_seat(self):
        return self.__has_inbox_seat
    
    @property
    def team_ids(self):
        return self.__team_ids
    
    @property
    def avatar(self):
        return self.__avatar
    
    @property
    def team_priority_level(self):
        return self.__team_priority_level
    
    @property
    def away_mode_enabled(self):
        return self.__away_mode_enabled
    
    @property
    def away_mode_reassign(self):
        return self.__away_mode_reassign
    
    # Property Setters
    
    @away_mode_enabled.setter
    def away_mode_enabled(self, value):
        pass
    
    # Methods
    
    def set_away_mode(self, enabled: bool = True):
        pass

    def set_reassign_mode(self, enabled: bool = True):
        pass
