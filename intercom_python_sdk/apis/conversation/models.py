"""
# Conversation API Models

`apis/Conversation/models.py`

This module contains models used to interact with the Intercom Conversation API [1].
These models provide object oriented interfaces for the schemas defined in `apis/Conversation/schemas.py`.

---
- [1] https://developers.intercom.com/docs/references/rest-api/api.intercom.io/Conversations/conversation/
"""

"""
{
  "type": "conversation",
  "id": "1295",
  "title": "Conversation Title",
  "created_at": 1663597223,
  "updated_at": 1663597260,
  "waiting_since": 1663597260,
  "snoozed_until": 1663597260,
  "open": true,
  "state": "open",
  "read": true,
  "priority": "priority",
  "admin_assignee_id": 0,
  "team_assignee_id": "5017691",
  "tags": {
    "type": "tag.list",
    "tags": [
      {
        "type": "tag",
        "id": "123456",
        "name": "Test tag",
        "applied_at": 1663597223,
        "applied_by": {
          "type": "contact",
          "id": "1a2b3c"
        }
      }
    ]
  },
  "conversation_rating": {
    "rating": 5,
    "remark": "",
    "created_at": 1671028894,
    "contact": {
      "type": "contact",
      "id": "5ba682d23d7cf92bef87bfd4",
      "external_id": "f3b87a2e09d514c6c2e79b9a"
    },
    "teammate": {
      "type": "contact",
      "id": "1a2b3c"
    }
  },
  "source": {
    "type": "conversation",
    "id": "3",
    "delivered_as": "operator_initiated",
    "subject": "",
    "body": "<p>Hey there!</p>",
    "author": {
      "type": "admin",
      "id": "274",
      "name": "Operator",
      "email": "operator+abcd1234@intercom.io"
    },
    "attachments": [
      {
        "type": "upload",
        "name": "example.png",
        "url": "https://picsum.photos/200/300",
        "content_type": "image/png",
        "filesize": 100,
        "width": 100,
        "height": 100
      }
    ],
    "url": null,
    "redacted": false
  },
  "contacts": {
    "type": "contact.list",
    "contacts": [
      {
        "type": "contact",
        "id": "5ba682d23d7cf92bef87bfd4",
        "external_id": "f3b87a2e09d514c6c2e79b9a"
      }
    ]
  },
  "teammates": {
    "type": "admin.list",
    "teammates": [
      {
        "type": "contact",
        "id": "1a2b3c"
      }
    ]
  },
  "custom_attributes": {
    "property1": "string",
    "property2": "string"
  },
  "first_contact_reply": {
    "created_at": 1663597223,
    "type": "conversation",
    "url": "https://developers.intercom.com/"
  },
  "sla_applied": {
    "type": "conversation_sla_summary",
    "sla_name": "",
    "sla_status": "hit"
  },
  "statistics": {
    "type": "conversation_statistics",
    "time_to_assignment": 2310,
    "time_to_admin_reply": 2310,
    "time_to_first_close": 2310,
    "time_to_last_close": 2310,
    "median_time_to_reply": 2310,
    "first_contact_reply_at": 1663597233,
    "first_assignment_at": 1663597233,
    "first_admin_reply_at": 1663597233,
    "first_close_at": 1663597233,
    "last_assignment_at": 1663597233,
    "last_assignment_admin_reply_at": 1663597233,
    "last_contact_reply_at": 1663597233,
    "last_admin_reply_at": 1663597233,
    "last_close_at": 1663597233,
    "last_closed_by_id": "c3po",
    "count_reopens": 1,
    "count_assignments": 1,
    "count_conversation_parts": 1
  },
  "conversation_parts": {
    "type": "conversation_part.list",
    "conversation_parts": [
      {
        "type": "conversation_part",
        "id": "3",
        "part_type": "comment",
        "body": "<p>Okay!</p>",
        "created_at": 1663597223,
        "updated_at": 1663597260,
        "notified_at": 1663597260,
        "assigned_to": {
          "type": "contact",
          "id": "1a2b3c"
        },
        "author": {
          "type": "admin",
          "id": "274",
          "name": "Operator",
          "email": "operator+abcd1234@intercom.io"
        },
        "attachments": [
          {
            "type": "upload",
            "name": "example.png",
            "url": "https://picsum.photos/200/300",
            "content_type": "image/png",
            "filesize": 100,
            "width": 100,
            "height": 100
          }
        ],
        "external_id": "abcd1234",
        "redacted": false
      }
    ],
    "total_count": 2
  },
  "linked_objects": {
    "type": "list",
    "total_count": 100,
    "has_more": false,
    "data": [
      {
        "type": "ticket",
        "id": "7583",
        "category": "Customer"
      }
    ]
  }
}
"""

# External
from bs4 import BeautifulSoup

from typing import (
    List,
    Optional,
    Union,
    TYPE_CHECKING
)

# From Current API
from . import schemas as c_schemas

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import ConversationAPI


class Conversation(ModelBase):
    """
    Represents a Conversation.

    Attributes:
        See the `ConversationSchema` definition in `apis/Conversation/schemas.py` for details.

    Model-Specific Attributes:
        api_client (ConversationAPI): The API Client Instance. Injected via APIProxyInterface
    """

    def __init__(self, *args, **kwargs):
        self.__type: str = kwargs.get('type', '')
        self.__id: str = kwargs.get('id', '')
        self.__title: str = kwargs.get('title', '')
        self.__created_at: int = kwargs.get('created_at', 0)
        self.__updated_at: int = kwargs.get('updated_at', 0)
        self.__waiting_since: int = kwargs.get('waiting_since', 0)
        self.__snoozed_until: int = kwargs.get('snoozed_until', 0)
        self.__open: bool = kwargs.get('open', False)
        self.__state: str = kwargs.get('state', '')
        self.__read: bool = kwargs.get('read', False)
        self.__priority: str = kwargs.get('priority', '')
        self.__admin_assignee_id: int = kwargs.get('admin_assignee_id', 0)
        self.__team_assignee_id: str = kwargs.get('team_assignee_id', '')
        self.__tags: c_schemas.Tags = kwargs.get('tags', None)
        self.__conversation_rating: c_schemas.ConversationRating = kwargs.get('conversation_rating', None)
        self.__source: c_schemas.Source = kwargs.get('source', None)
        self.__contacts: c_schemas.Contacts = kwargs.get('contacts', None)
        self.__teammates: c_schemas.Teammates = kwargs.get('teammates', None)
        self.__custom_attributes: dict = kwargs.get('custom_attributes', {})
        self.__first_contact_reply: c_schemas.FirstContactReply = kwargs.get('first_contact_reply', None)
        self.__sla_applied: c_schemas.SLAApplied = kwargs.get('sla_applied', None)
        self.__statistics: c_schemas.Statistics = kwargs.get('statistics', None)
        self.__conversation_parts: c_schemas.ConversationParts = kwargs.get('conversation_parts', None)
        self.__linked_objects: c_schemas.LinkedObjects = kwargs.get('linked_objects', None)



   