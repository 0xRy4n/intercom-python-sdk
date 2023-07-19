"""
====================
Data Events API Schemas
====================
`apis/data_events/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the 
`apis/data_events/models.py` module.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/the-data-event-model
"""

# External
import marshmallow
from marshmallow import fields

# From Current API
from . import models as da_models

# From Current Package
from ...core.schema_base import SchemaBase


class DataEventSummarySchema(SchemaBase):
    type = fields.Str()
    event_name = fields.Str()
    count = fields.Int()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return da_models.DataEventSummary(**data)

class DataEventSchema(SchemaBase):
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


class DataEventsListSchema(SchemaBase):
    type = fields.Str()
    events = fields.List(fields.Nested(DataEventSchema))

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return da_models.DataEventsList(**data)
    



