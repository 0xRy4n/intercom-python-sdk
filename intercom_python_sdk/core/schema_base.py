"""
# Schema Base Classes

`core/schema_base.py`

Extensible schemas applicable to all APIS.
"""
# External
import marshmallow


class SchemaBase(marshmallow.Schema):
    """
    Base schema for all API schemas.
    """

    class Meta:
        """
        Defines Meta options for schemas.

        See https://marshmallow.readthedocs.io/en/stable/marshmallow.schema.html#marshmallow.schema.Schema.Meta
        """
        unknown = marshmallow.EXCLUDE  # Exclude unknown fields from deserialization
