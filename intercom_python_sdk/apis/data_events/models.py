"""
# Data Events API Models

`apis/data_events/models.py`

This module contains models used to interact with the Intercom Admins API [1].
These models provide object oriented interfaces for the schemas defined in `apis/data_attributes/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
"""
# Built-ins
from typing import (
    Optional,
    List,
    TYPE_CHECKING,
)

# From Current Package
from ...core.model_base import ModelBase

if TYPE_CHECKING:
    from .api import DataEventsAPI


class DataEventSummary(ModelBase):
    def __init__(self, *args, **kwargs):
        self.__event_name = kwargs.get('event_name', '')
        self.__count = kwargs.get('count', '')
        self.__first = kwargs.get('first', '')
        self.__last = kwargs.get('last', '')

    # Properties

    @property
    def event_name(self) -> str:
        return self.__event_name

    @property
    def count(self) -> str:
        return self.__count

    @property
    def first(self) -> str:
        return self.__first

    @property
    def last(self) -> str:
        return self.__last


class DataEvent(ModelBase):
    def __init__(self, *args, **kwargs):
        self.__type__ = kwargs.get('type', 'event')
        self.__event_name__ = kwargs.get('event_name', '')
        self.__created_at__ = kwargs.get('created_at')
        self.__id__ = kwargs.get('id', '')
        self.__intercom_user_id__ = kwargs.get('intercom_user_id', '')
        self.__email__ = kwargs.get('email', '')
        self.__metadata__ = kwargs.get('metadata', {})
        self._api_client: 'DataEventsAPI' = kwargs.get('api_client')  # type: ignore

    # Properties

    @property
    def api_client(self) -> 'DataEventsAPI':
        return self._api_client

    @api_client.setter
    def api_client(self, value: 'DataEventsAPI'):
        self._api_client = value

    @property
    def type(self) -> str:
        """ The type of the object. """
        return self.__type__

    @property
    def event_name(self) -> str:
        """ The name of the data event. """
        return self.__event_name__

    @property
    def created_at(self) -> Optional[int]:
        """ The timestamp of the data event. """
        return self.__created_at__

    @property
    def id(self) -> str:
        """ The ID of the data event. """
        return self.__id__

    @property
    def intercom_user_id(self) -> str:
        """ The Intercom user ID of the user associated with the data event. """
        return self.__intercom_user_id__

    @property
    def email(self) -> str:
        """ The email of the user associated with the data event. """
        return self.__email__

    @property
    def metadata(self) -> dict:
        """ The metadata associated with the data event. """
        return self.__metadata__


class DataEventList(ModelBase):
    """ List of Data Events.

    It is iterable and indexable like a list (will delegate to the `events` attribute).
    """
    def __init__(self, *args, **kwargs):
        self.__type__ = kwargs.get('type', '')
        self.__events__ = kwargs.get('events', [])

    # Properties

    @property
    def type(self) -> str:
        """ The type of the object. """
        return self.__type__

    @property
    def events(self) -> List[DataEvent]:
        """ A list of Data Event objects. """
        return self.__events__

    # Dunder Overrides

    def __iter__(self):
        return iter(self.events)

    def __getitem__(self, index):
        return self.events[index]

    def __len__(self):
        return len(self.events)
