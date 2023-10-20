"""
# Intercom Error Objects

`core/errors.py`

This module contains the IntercomErrorObject and IntercomErrorList classes, which
are custom exceptions for Intercom error objects. These models/schemas are implemented
as defined by the Intercom API Reference [1].

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/error-objects
"""
# Built-ins
from pprint import pformat
from typing import Any

# External
from marshmallow import (
    fields,
    post_load,
)

# From Current Package
from .schema_base import SchemaBase


class IntercomErrorObjectSchema(SchemaBase):
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
    request_id = fields.Str()

    @post_load
    def make_intercom_error_object(self, data, **kwargs):
        return IntercomErrorObject(**data)


class IntercomErrorListSchema(SchemaBase):
    """
    Schema for a list of Intercom error objects.

    Attributes:
        type (str): The type of the error.
        errors (List[IntercomErrorObjectSchema]): The list of errors.
    """
    type = fields.Str()
    errors = fields.List(fields.Nested(IntercomErrorObjectSchema))
    request_id = fields.Str()

    @post_load
    def make_intercom_error_list(self, data, **kwargs):
        return IntercomErrorList(**data)


class IntercomErrorObject:
    """ Custom exception for an Intercom error object. """

    def __init__(self, **kwargs: Any):
        self.code = kwargs.get("code", "")
        self.message = kwargs.get("message", "")

        if kwargs.get("field"):
            self.field = kwargs.get("field")

        if kwargs.get("request_id"):
            self.request_id = kwargs.get("request_id")

    def __str__(self):
        return f"\n{pformat(self.__dict__)}\n"

    def __repr__(self):
        return self.__str__()


class IntercomErrorList(Exception):
    """ Custom exception for a list of Intercom error objects. """
    def __init__(self, **kwargs):
        self.type = kwargs.get("type", "")
        self.errors = kwargs.get("errors", [])
        self.request_id = kwargs.get("request_id", None)

        super().__init__(f"Error Response from Intercom API. Request ID: {self.request_id}\n {pformat(self.__dict__)}")


def catch_api_error(response):  # type: ignore
    """ Catches API errors and raises them as as custom exceptions. """
    if 200 <= response.status_code < 300:
        return response

    data = response.json()
    error = IntercomErrorListSchema().load(data)

    print(response.content)

    raise error  # type: ignore
