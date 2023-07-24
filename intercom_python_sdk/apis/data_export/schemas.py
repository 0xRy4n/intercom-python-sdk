"""
====================
Data Export API Schemas
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
from . import models as dexport_models

# From Current Package
from ...core.schema_base import SchemaBase



class DataExportJobSchema(SchemaBase):
    job_identifier = fields.Str()
    status = fields.Str()
    download_expires_at = fields.Str()
    download_url = fields.Str()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return dexport_models.DataExportJob(**data)
    