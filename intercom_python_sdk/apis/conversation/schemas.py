"""
# Conversation API Schemas

`apis/Conversation/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the
`apis/data_attributes/models.py` module.

---
- [1] https://developers.intercom.com/docs/references/rest-api/api.intercom.io/Conversations/conversation/
"""

# External
import marshmallow
from marshmallow import fields

# From Current Package
from ...core.schema_base import SchemaBase


class ContactSchema(SchemaBase):
    """ Schema for a contact.

    Attributes:
        type (str): The type of the contact.
        id (str): The unique identifier for this contact.
        external_id (str): The external ID of the contact.
    """
    type = fields.Str()
    id = fields.Str()
    external_id = fields.Str()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data


class TagSchema(SchemaBase):
    """ Schema for a tag.

    Attributes:
        type (str): The type of the tag.
        id (str): The unique identifier for this tag.
        name (str): The name of the tag.
        applied_at (int): The unix timestamp of when the tag was applied.
        applied_by (dict): Information about the entity that applied the tag.
    """
    type = fields.Str()
    id = fields.Str()
    name = fields.Str()
    applied_at = fields.Int()
    applied_by = fields.Dict()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data

# Define other nested schemas for ConversationRating, Source, Teammate, and so on.

class ConversationRatingSchema(SchemaBase):
    """ Schema for a conversation rating.

    Attributes:
        rating (int): The rating.
        remark (str): The remark.
        created_at (int): The unix timestamp of when the rating was created.
        contact (dict): Information about the contact who rated the conversation.
        teammate (dict): Information about the teammate who was rated.
    """
    rating = fields.Int()
    remark = fields.Str()
    created_at = fields.Int()
    contact = fields.Dict()
    teammate = fields.Dict()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ConversationSourceSchema(SchemaBase):
    """ Schema for a conversation source.

    Attributes:
        type (str): The type of the source.
        id (str): The unique identifier for this source.
        delivered_as (str): The delivery method for the source.
        subject (str): The subject of the source.
        body (str): The body of the source.
        author (dict): Information about the author of the source.
        attachments (list): A list of attachments associated with the source.
        url (str): The url of the source.
        redacted (bool): Whether the source has been redacted.
    """
    type = fields.Str()
    id = fields.Str()
    delivered_as = fields.Str()
    subject = fields.Str()
    body = fields.Str()
    author = fields.Dict()
    attachments = fields.List(fields.Dict())
    url = fields.Str()
    redacted = fields.Bool()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ContactsSchema(SchemaBase):
    """ Schema for a list of contacts.

    Attributes:
        type (str): The type of the contacts.
        contacts (list): A list of contacts.
    """
    type = fields.Str()
    contacts = fields.List(fields.Nested(ContactSchema))

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class TeammatesSchema(SchemaBase):
    """ Schema for a list of teammates.

    Attributes:
        type (str): The type of the teammates.
        teammates (list): A list of teammates.
    """
    type = fields.Str()
    teammates = fields.List(fields.Dict())

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ConversationPartSchema(SchemaBase):
    """ Schema for a conversation part.

    Attributes:
        type (str): The type of the conversation part.
        id (str): The unique identifier for this conversation part.
        part_type (str): The type of the conversation part.
        body (str): The body of the conversation part.
        created_at (int): The unix timestamp of when the conversation part was created.
        updated_at (int): The unix timestamp of when the conversation part was updated.
        notified_at (int): The unix timestamp of when the conversation part was notified.
        assigned_to (dict): Information about the entity that the conversation part was assigned to.
        author (dict): Information about the author of the conversation part.
        attachments (list): A list of attachments associated with the conversation part.
        external_id (str): The external ID of the conversation part.
        redacted (bool): Whether the conversation part has been redacted.
    """
    type = fields.Str()
    id = fields.Str()
    part_type = fields.Str()
    body = fields.Str()
    created_at = fields.Int()
    updated_at = fields.Int()
    notified_at = fields.Int()
    assigned_to = fields.Dict()
    author = fields.Dict()
    attachments = fields.List(fields.Dict())
    external_id = fields.Str()
    redacted = fields.Bool()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ConversationPartListSchema(SchemaBase):
    """ Schema for a list of conversation parts.

    Attributes:
        type (str): The type of the conversation parts.
        conversation_parts (list): A list of conversation parts.
        total_count (int): The total number of conversation parts.
    """
    type = fields.Str()
    conversation_parts = fields.List(fields.Nested(ConversationPartSchema))
    total_count = fields.Int()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class LinkedObjectsSchema(SchemaBase):
    """ Schema for a list of linked objects.

    Attributes:
        type (str): The type of the linked objects.
        total_count (int): The total number of linked objects.
        has_more (bool): Whether there are more linked objects.
        data (list): A list of linked objects.
    """
    type = fields.Str()
    total_count = fields.Int()
    has_more = fields.Bool()
    data = fields.List(fields.Dict())

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ConversationStatisticsSchema(SchemaBase):
    """ Schema for conversation statistics.

    Attributes:
        type (str): The type of the conversation statistics.
        time_to_assignment (int): The time to assignment.
        time_to_admin_reply (int): The time to admin reply.
        time_to_first_close (int): The time to first close.
        time_to_last_close (int): The time to last close.
        median_time_to_reply (int): The median time to reply.
        first_contact_reply_at (int): The unix timestamp of when the first contact reply occurred.
        first_assignment_at (int): The unix timestamp of when the first assignment occurred.
        first_admin_reply_at (int): The unix timestamp of when the first admin reply occurred.
        first_close_at (int): The unix timestamp of when the first close occurred.
        last_assignment_at (int): The unix timestamp of when the last assignment occurred.
        last_assignment_admin_reply_at (int): The unix timestamp of when the last assignment admin reply occurred.
        last_contact_reply_at (int): The unix timestamp of when the last contact reply occurred.
        last_admin_reply_at (int): The unix timestamp of when the last admin reply occurred.
        last_close_at (int): The unix timestamp of when the last close occurred.
        last_closed_by_id (str): The unique identifier for the entity that closed the conversation.
        count_reopens (int): The number of times the conversation was reopened.
        count_assignments (int): The number of times the conversation was assigned.
        count_conversation_parts (int): The number of conversation parts.
    """
    type = fields.Str()
    time_to_assignment = fields.Int()
    time_to_admin_reply = fields.Int()
    time_to_first_close = fields.Int()
    time_to_last_close = fields.Int()
    median_time_to_reply = fields.Int()
    first_contact_reply_at = fields.Int()
    first_assignment_at = fields.Int()
    first_admin_reply_at = fields.Int()
    first_close_at = fields.Int()
    last_assignment_at = fields.Int()
    last_assignment_admin_reply_at = fields.Int()
    last_contact_reply_at = fields.Int()
    last_admin_reply_at = fields.Int()
    last_close_at = fields.Int()
    last_closed_by_id = fields.Str()
    count_reopens = fields.Int()
    count_assignments = fields.Int()
    count_conversation_parts = fields.Int()

    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    

class ConversationSchema(SchemaBase):
    #use the nested classes from the top 
    """ Schema for a conversation.
    """
    type = fields.Str(allow_none=True, required=False)
    id = fields.Str(allow_none=True, required=False)
    title = fields.Str(allow_none=True, required=False)
    created_at = fields.Int(allow_none=True, required=False)
    updated_at = fields.Int(allow_none=True, required=False)
    waiting_since = fields.Int(allow_none=True, required=False)
    snoozed_until = fields.Int(allow_none=True, required=False)
    open = fields.Bool(allow_none=True, required=False)
    state = fields.Str(allow_none=True, required=False)
    read = fields.Bool(allow_none=True, required=False)
    priority = fields.Str(allow_none=True, required=False)
    admin_assignee_id = fields.Int(allow_none=True, required=False)
    team_assignee_id = fields.Str(allow_none=True, required=False)
    tags = fields.Nested(TagSchema, allow_none=True, required=False)
    conversation_rating = fields.Nested(ConversationRatingSchema, allow_none=True, required=False)
    source = fields.Nested(ConversationSourceSchema, allow_none=True, required=False)
    contacts = fields.Nested(ContactsSchema, allow_none=True, required=False)
    teammates = fields.Nested(TeammatesSchema, allow_none=True, required=False)
    custom_attributes = fields.Dict(allow_none=True, required=False)
    first_contact_reply = fields.Dict(allow_none=True, required=False)
    sla_applied = fields.Dict(allow_none=True, required=False)
    statistics = fields.Nested(ConversationStatisticsSchema, allow_none=True, required=False)
    conversation_parts = fields.Nested(ConversationPartListSchema, allow_none=True, required=False)
    linked_objects = fields.Nested(LinkedObjectsSchema, allow_none=True, required=False)
    
    @marshmallow.post_load
    def make(self, data, **kwargs):
        return data
    




