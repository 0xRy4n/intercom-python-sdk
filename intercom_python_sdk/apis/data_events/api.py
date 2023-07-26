"""
# Data Events API

`apis/data_events/api.py`

This module contains the Data EventsAPI class, which defines a client for the Data Events API.
It is used to interact with the Intercom Data Events API [1] as defined in the Intercom API Reference [2].

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/createdataevent
- [2] https://github.com/intercom/Intercom-OpenAPI
"""

# External
from uplink import (
    get, post,
    returns,
    response_handler,
    Body, Query
)

# From Current API
from .schemas import (
    DataEventSchema,
    DataEventsListSchema
)

from .models import (
    DataEventsList
)

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class DataEventsAPI(APIBase):
    """ Data Events API Client. """
    URI = "/events/"

    # Internal method required here so we can implement custom query parameter logic
    @returns(DataEventsListSchema())  # type: ignore
    @get("")
    def __list_all(self,
                   user_id: Query("user_id", str) = None,  # noqa # type: ignore
                   intercom_user_id: Query("intercom_user_id", str) = None,  # noqa # type: ignore
                   email: Query("email", str) = None,  # noqa #  type: ignore
                   type: Query("type", str) = "user",  # noqa # type: ignore
                   summary: Query("summary", bool) = False):  # noqa # type: ignore

        """ List all data events. Internal method for `list_all`."""

    def list_all(self,
                 user_id: str = "",
                 intercom_user_id: str = "",
                 email: str = "",
                 summary: bool = False) -> DataEventsList:

        """ List all data events.

        Args:
            user_id (str): The user id of the user who triggered the event.
            intercom_user_id (str): The intercom user id of the user who triggered the event.
            email (str): The email of the user who triggered the event.
            summary (bool): Whether to return a summary of the data events.

            _Requires at least one of `user_id`, `intercom_user_id`, or `email`._

        Returns:
            DataEventsList: A list of data events.
        """

        # Validate input
        if not any([user_id, intercom_user_id, email]):
            raise ValueError("At least one of `user_id`, `intercom_user_id`, or `email` must be provided.")

        return self.__list_all(user_id=user_id, intercom_user_id=intercom_user_id, email=email, summary=summary)

    @returns(DataEventSchema())  # type: ignore
    @post("")
    def submit(self, event: Body(type=DataEventSchema)):  # type: ignore
        """ Submit a new data event.

        Args:
            event (DataEventSchema): The data event to submit.
                Takes in a DataEventSchema object as defined in `apis/data_events/schemas.py`.

        Returns:
            DataEvent: The data event that was submitted.
        """
