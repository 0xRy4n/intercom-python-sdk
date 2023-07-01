"""
=====================
Intercom Error Objects
=====================
`core/errors.py`

This module contains the IntercomErrorObject and IntercomErrorList classes, which are custom exceptions for Intercom error objects.
These models/schemas are implemented as defined by the Intercom API Reference [1].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/error-objects
"""
# Built-ins
import json

# External
from marshmallow import (
    Schema, 
    fields, 
    post_load, 
    ValidationError
)


class IntercomErrorObjectSchema(Schema):
    """
    Schema for an Intercom error object.

    Attributes:
        code (str): The code of the error.
        message (str): The message of the error.
        field (str): The field of the error (optional).
    """
    code = fields.Str()
    message = fields.Str()
    field = fields.Str()

    @post_load
    def make_intercom_error_object(self, data, **kwargs):
        return IntercomErrorObject(**data)

class IntercomErrorListSchema(Schema):
    """
    Schema for a list of Intercom error objects.

    Attributes:
        type (str): The type of the error.
        errors (List[IntercomErrorObjectSchema]): The list of errors.
    """
    type = fields.Str()
    errors = fields.List(fields.Nested(IntercomErrorObjectSchema))

    @post_load
    def make_intercom_error_list(self, data, **kwargs):
        return IntercomErrorList(**data)

class IntercomErrorObject:
    """ Custom exception for an Intercom error object. """
    def __init__(self, code, message, field = None):
        self.code = code
        self.message = message
        self.field = field

    def __str__(self):
        return f"Code: {self.code}, Message: {self.message}, Field: {self.field}"


class IntercomErrorList(Exception):
    """ Custom exception for a list of Intercom error objects. """
    def __init__(self, type, errors):
        self.type = type
        self.errors = errors
        error_messages = "\n".join([str(error.message) for error in errors])
        super().__init__(f"Type: {type}\nErrors: {error_messages}")


def catch_api_error(response):  # sourcery skip: raise-specific-error
    """ Catches API errors and raises them as as custom exceptions. """
    # TODO: Fix IntercomErrorList raising.
    if 200 <= response.status_code < 300:
        return response

    try:
        data = response.json()
        parsed_data = IntercomErrorListSchema().load(data)

        raise IntercomErrorList(parsed_data.type, parsed_data.errors) # type: ignore

    except Exception as e:
        raise Exception(
            f"Got an unexpected response from the API: {response.text}"
        ) from e
