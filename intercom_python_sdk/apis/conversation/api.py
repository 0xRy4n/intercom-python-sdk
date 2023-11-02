"""
# Conversation API

`apis/data_events/api.py`

This module contains the conversationAPI class, which defines a client for the conversation API.
It is used to interact with the Intercom Conversation API [1] as defined in the Intercom API Reference [2].

---
- [1] https://developers.intercom.com/docs/references/rest-api/api.intercom.io/Conversations/conversation/
- [2] https://github.com/intercom/Intercom-OpenAPI
"""

# External
from uplink import (
    get, post,
    returns,
    response_handler,
    Body, Query,json
)

# From Current API

# Intercom Python SDK
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class ConversationAPI(APIBase):  # type: ignore
    URI = "/conversations/"

    @json  # type: ignore
    @post("{conversation_id}/reply")
    def reply_to_conversation(self, conversation_id: str, payload: Body): #type: ignore
        """ Reply to a Conversation.

        Args:
            conversation_id (str): The ID of the Conversation.
            payload (Body): The payload of the reply.

        Returns:
            Conversation: The Conversation with the given ID.
        """

