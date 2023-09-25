"""
# Help Center API Schemas

`apis/help_center/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the 
`apis/help_center/models.py` module.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listallcollections
"""

# External
import marshmallow
from marshmallow import fields

# From Current API
from . import models as help_center_models

# From Current Package
from ...core.schema_base import SchemaBase



class CollectionSchema(SchemaBase):
    id = fields.Str()
    type = fields.Str()
    workspace_id = fields.Str()
    name = fields.Str()
    description = fields.Str(allow_none=True)
    created_at = fields.Int()
    updated_at = fields.Int()
    url = fields.Str(allow_none=True)
    icon = fields.Str(allow_none=True)
    order = fields.Int()
    default_locale = fields.Str(allow_none=True)
    translated_content = fields.Dict(allow_none=True)
    parent_id = fields.Int(allow_none=True)

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return help_center_models.Collection(**data)


class CollectionListSchema(SchemaBase):

    type = fields.Str()
    data = fields.List(fields.Nested(CollectionSchema))
    total_count = fields.Int()
    pages = fields.Dict()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return help_center_models.CollectionList(**data)


class SectionSchema(SchemaBase):
    id = fields.Str()
    type = fields.Str()
    parent_id = fields.Int()
    workspace_id = fields.Str()
    name = fields.Str()
    created_at = fields.Int()
    updated_at = fields.Int()
    url = fields.Str()
    icon = fields.Str(allow_none=True)
    order = fields.Int()
    collection_id = fields.Str()
    default_locale = fields.Str(allow_none=True)
    translated_content = fields.Dict(allow_none=True)

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return help_center_models.Section(**data)


class SectionListSchema(SchemaBase):
    
        type = fields.Str()
        data = fields.List(fields.Nested(SectionSchema))
        total_count = fields.Int()
        pages = fields.Dict()
    
        @marshmallow.post_load
        def make(self, data, **kwargs):
            return help_center_models.SectionList(**data)
