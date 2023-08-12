"""
# Help Center API Schemas

`apis/teams/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the 
`apis/teams/models.py` module.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listteams
"""


# External
import marshmallow
from marshmallow import fields

# From Current API
from . import models as t_models

# From Current Package
from ...core.schema_base import SchemaBase

'''
{
    "type": "team",
    "id": "814865",
    "name": "Example Team",
    "admin_ids": [
        493881
        814860
    ]
   "admin_priority_level": {
     "primary_admin_ids": [
        493881
      ],
      "secondary_admin_ids": [
        814860
      ]
    },
}
'''
class AdminPriorityLevelSchema(SchemaBase):
    """
    This schema represents a AdminPriorityLevel on Intercom.

    Attributes:
        primary_admin_ids (list): The IDs of the primary admins of the AdminPriorityLevel.
        secondary_admin_ids (list): The IDs of the secondary admins of the AdminPriorityLevel.
    """
    primary_admin_ids = fields.List(fields.Int())
    secondary_admin_ids = fields.List(fields.Int())

class TeamSchema(SchemaBase):
    """
    This schema represents a Team on Intercom.

    Attributes:
        id (int): The ID of the Team.
        type (str): The type of the Team.
        name (str): The name of the Team.
        admin_ids (list): The IDs of the admins of the Team.
        admin_priority_level (dict): The priority level of the admins of the Team.
    """
    id = fields.Int()
    type = fields.Str()
    name = fields.Str()
    admin_ids = fields.List(fields.Int())
    admin_priority_level = fields.Nested(AdminPriorityLevelSchema)
    



class TeamListSchema(SchemaBase):
    """
    This schema represents a TeamList on Intercom.

    Attributes:
        teams (list): The Teams of the TeamList.
    """
    teams = fields.List(fields.Nested(TeamSchema))
