from marshmallow import Schema, fields, post_load, ValidationError
import json

class IntercomErrorObjectSchema(Schema):
    code = fields.Str()
    message = fields.Str()
    field = fields.Str()

    @post_load
    def make_intercom_error_object(self, data, **kwargs):
        return IntercomErrorObject(**data)

class IntercomErrorListSchema(Schema):
    type = fields.Str()
    errors = fields.List(fields.Nested(IntercomErrorObjectSchema))

    @post_load
    def make_intercom_error_list(self, data, **kwargs):
        return IntercomErrorList(**data)

class IntercomErrorObject:
    def __init__(self, code, message, field = None):
        self.code = code
        self.message = message
        self.field = field

    def __str__(self):
        return f"Code: {self.code}, Message: {self.message}, Field: {self.field}"


class IntercomErrorList(Exception):
    def __init__(self, type, errors):
        self.type = type
        self.errors = errors
        error_messages = "\n".join([str(error.message) for error in errors])
        super().__init__(f"Type: {type}\nErrors: {error_messages}")


def catch_api_error(response):
    if 200 <= response.status_code < 300:
        return response

    try:
        data = response.json()
        parsed_data = IntercomErrorListSchema().load(data)
        
        raise IntercomErrorList(parsed_data.type, parsed_data.errors) # type: ignore
    
    except Exception:
        raise Exception(f"Got an unexpected response from the API: {response.text}")
