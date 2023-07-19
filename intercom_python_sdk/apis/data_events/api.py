""" 
====================
Data Events API
====================
`apis/data_events/api.py`

This module contains the Data EventsAPI class, which defines a client for the Data Events API.
It is used to interact with the Intercom Data Events API [1] as defined in the Intercom API Reference [2].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/createdataevent
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
from typing import Union

# External
import marshmallow
from uplink import (
    get, put, post, 
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query
)

# From Current API
from .schemas import (
    DataEventSchema,
    DataEventsListSchema
)

from .models import (
    DataEvent,
    DataEventsList
)

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class DataEventsAPI(APIBase):
    URI = "/events/"

    # Internal method required here so we can implement custom query parameter logic
    @returns(DataEventsListSchema()) # type: ignore
    @get("")
    def __list_all(self, 
                   user_id: Query("user_id", str) = None, # type: ignore
                   intercom_user_id: Query("intercom_user_id", str) = None, # type: ignore
                   email: Query("email", str) = None, # type: ignore
                   type: Query("type", str) = "user", # type: ignore
                   summary: Query("summary", bool) = False): # type: ignore
        
        """ List all data events. Internal method for `list_all`."""

    
    def list_all(self, 
                 user_id: str = "", 
                 intercom_user_id: str = "",
                 email: str = "",
                 summary: bool = False):
        
        """ List all data events. Requires at least one of `user_id`, `intercom_user_id`, or `email`. """

        # Validate input
        if not any([user_id, intercom_user_id, email]):
            raise ValueError("At least one of `user_id`, `intercom_user_id`, or `email` must be provided.")

        return self.__list_all(user_id=user_id, intercom_user_id=intercom_user_id, email=email, summary=summary)
    

    @returns(DataEventSchema()) # type: ignore
    @post("")
    def submit(self, event: Body(type=DataEventSchema)): # type: ignore
        """ Submit a new data event. """


    