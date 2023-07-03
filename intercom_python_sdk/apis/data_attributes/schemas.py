"""
====================
Data Attributes API Schemas
====================
`apis/data_attributes/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the 
`apis/data_attributes/models.py` module.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/the-data-attribute-model
"""

# External
import marshmallow
from marshmallow import Schema, fields

# From Current API
from .models import (
    DataAttribute,
    DataAttributeList,
)


class DataAttributeSchema(Schema):
    """
    This schema represents a Data Attribute on Intercom.

    Attributes:
        name (str): The name of the Data Attribute. (Required)
        model (str): The model of the Data Attribute. (Required)
        data_type (str): The data type of the Data Attribute. (Required)
        type (str): The type of the Data Attribute.
        id (int): The ID of the Data Attribute.
        full_name (str): The full name of the Data Attribute.
        label (str): The label of the Data Attribute.
        description (str): The description of the Data Attribute.
        options (List[str]): The options of the Data Attribute.
        api_writeable (bool): True if the Data Attribute is API writeable, False otherwise.
        ui_writeable (bool): True if the Data Attribute is UI writeable, False otherwise.
        custom (bool): True if the Data Attribute is custom, False otherwise.
        archived (bool): True if the Data Attribute is archived, False otherwise.
        admin_id (str): The ID of the admin who created the Data Attribute.
        created_at (int): The timestamp of when the Data Attribute was created.
        updated_at (int): The timestamp of when the Data Attribute was updated.
    """
    name = fields.Str(required=True)
    model = fields.Str(required=True)
    data_type = fields.Str(required=True)
    type = fields.Str()
    id = fields.Int()
    full_name = fields.Str()
    label = fields.Str()
    description = fields.Str()
    options = fields.List(fields.Str())
    api_writeable = fields.Bool()
    ui_writeable = fields.Bool()
    custom = fields.Bool()
    archived = fields.Bool()
    admin_id = fields.Str()
    created_at = fields.Int()
    updated_at = fields.Int()

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def make_data_attribute(self, data, **kwargs):
        return DataAttribute(**data)

    

class DataAttributeListSchema(Schema):
    """
    This schema represents a list of Data Attributes on Intercom.

    Attributes:
        type (str): The type of the Data Attribute list.
        data (List[DataAttributeSchema]): The list of Data Attributes.
        pages (PagesSchema): The pagination information for the Data Attribute list.
    """
    type = fields.Str()
    data = fields.List(fields.Nested(DataAttributeSchema(unknown = marshmallow.EXCLUDE)))

    @marshmallow.post_load
    def make_data_attribute_list(self, data, **kwargs):
        print(data)
        return DataAttributeList(**data)
