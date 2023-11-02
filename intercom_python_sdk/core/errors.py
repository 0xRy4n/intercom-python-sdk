# Built-ins
from pprint import pformat
from typing import Any, List

# External
from marshmallow import fields, Schema, post_load, ValidationError

# From Current Package
# Assuming that the SchemaBase import is valid and it extends from marshmallow.Schema
from .schema_base import SchemaBase


class IntercomErrorObjectSchema(SchemaBase):
    """
    Schema for an Intercom error object.
    """
    code = fields.Str(required=True)
    message = fields.Str(required=True)
    field = fields.Str(missing=None)
    request_id = fields.Str(missing=None)

    @post_load
    def make_intercom_error_object(self, data, **kwargs):
        return IntercomErrorObject(**data)


class IntercomErrorListSchema(SchemaBase):
    """
    Schema for a list of Intercom error objects.
    """
    type = fields.Str(required=True)
    errors = fields.List(fields.Nested(IntercomErrorObjectSchema), required=True)
    request_id = fields.Str(missing=None)

    @post_load
    def make_intercom_error_list(self, data, **kwargs):
        return IntercomErrorList(**data)


class IntercomErrorObject(Exception):
    """ Custom exception for an Intercom error object. """
    def __init__(self, code: str, message: str, field: str = None, request_id: str = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.field = field
        self.request_id = request_id

    def __str__(self):
        return f"IntercomErrorObject(code={self.code}, message={self.message}, field={self.field}, request_id={self.request_id})"


class IntercomErrorList(Exception):
    """ Custom exception for a list of Intercom error objects. """
    def __init__(self, type: str, errors: List[IntercomErrorObject], request_id: str = None):
        message = f"Intercom API returned multiple errors: {pformat(errors)}"
        super().__init__(message)
        self.type = type
        self.errors = errors
        self.request_id = request_id


def catch_api_error(response):
    """ Catches API errors and raises them as custom exceptions. """
    if 200 <= response.status_code < 300:
        return response

    try:
        data = response.json()
    except ValueError:
        response.raise_for_status()

    try:
        error_list = IntercomErrorListSchema().load(data)
        raise error_list
    except ValidationError as e:
        raise ValueError(f"Error parsing error response: {e.messages}")