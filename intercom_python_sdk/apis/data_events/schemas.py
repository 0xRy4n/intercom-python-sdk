"""
# Data Events API Schemas

`apis/data_events/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the
`apis/data_events/models.py` module.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/the-data-event-model
"""

# External
import marshmallow
from marshmallow import fields

# From Current API
from . import models as da_models

# From Current Package
from ...core.schema_base import SchemaBase


class DataEventSummarySchema(SchemaBase):
    """ Schema for a summary of data events.

    Attributes:
        type (str): The type of data event.
        event_name (str): The name of the event.
        count (int): The number of times the event has occurred.
    """
    type = fields.Str()
    event_name = fields.Str()
    count = fields.Int()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return da_models.DataEventSummary(**data)


class DataEventSchema(SchemaBase):
    """ Schema for a data event.

    Attributes:
        type (str): The type of data event.
        event_name (str): The name of the event.
        created_at (int): The unix timestamp of when the event occurred.
        user_id (str): The user id of the user who triggered the event.
        id (str): The unique identifier for this data event.
        intercom_user_id (str): The intercom user id of the user who triggered the event.
        email (str): The email of the user who triggered the event.
        metadata (dict): The metadata associated with the event.
    """
    type = fields.Str()
    event_name = fields.Str()
    created_at = fields.Int()
    user_id = fields.Str()
    id = fields.Str()
    intercom_user_id = fields.Str()
    email = fields.Str()
    metadata = fields.Dict()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return da_models.DataEvent(**data)


class DataEventListSchema(SchemaBase):
    """ Schema for a list of Data Events.

    Attributes:
        type (str): The type of data event.
        events (list): A list of data events.
    """
    type = fields.Str()
    events = fields.List(fields.Nested(DataEventSchema))

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return da_models.DataEventList(**data)
