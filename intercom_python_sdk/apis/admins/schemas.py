"""
# Admins API Schemas

`apis/admins/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined
in the `apis/admins/models.py` module.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/the-admin-model
"""

# External
import marshmallow
from marshmallow import fields

# From Current API
from .models import (
    Admin,
    AdminList,
    TeamPriorityLevel
)

# From Current Package
from ...core.schema_base import SchemaBase


class AdminAppSchema(SchemaBase):
    """
    This schema represents the app the admin belongs to.

    Attributes:
        type (str): The type of the app.
        id (str): The ID of the app.
        name (str): The name of the app.
        region (str): The region of the app.
        timezone (str): The timezone of the app.
        created_at (int): The creation time of the app.
        identity_verification (bool): True if the app has identity verification enabled, False otherwise.
    """
    type = fields.Str()
    id = fields.Str()
    name = fields.Str()
    region = fields.Str()
    timezone = fields.Str()
    created_at = fields.Int()
    identity_verification = fields.Boolean()


class AdminAvatarSchema(SchemaBase):
    """
    This schema represents an avatar of an admin user.

    Attributes:
        type (str): The type of the avatar.
        image_url (str): The URL of the avatar image.
    """
    type = fields.Str(default='avatar')
    image_url = fields.Str()


class TeamPriorityLevelSchema(SchemaBase):
    """
    This schema represents a priority level of a team.

    Attributes:
        primary_team_ids (List[int]): The IDs of the primary teams.
        secondary_team_ids (List[int]): The IDs of the secondary teams.
    """
    primary_team_ids = fields.List(fields.Int())
    secondary_team_ids = fields.List(fields.Int())

    @marshmallow.post_load
    def make_team_priority_level(self, data, **kwargs):
        return TeamPriorityLevel(**data)


class AdminSchema(SchemaBase):
    """
    This schema represents an admin user on Intercom.

    Attributes:
        type (str): The type of the admin user.
        id (str): The ID of the admin user.
        name (str): The name of the admin user.
        email (str): The email of the admin user.
        job_title (str): The job title of the admin user.
        away_mode_enabled (bool): True if the away mode is enabled for the admin user, False otherwise.
        away_mode_reassign (bool): True if the away mode reassign is enabled for the admin user, False otherwise.
        has_inbox_seat (bool): True if the admin user has an inbox seat, False otherwise.
        team_ids (List[int]): The IDs of the teams the admin user belongs to.
        avatar (Dict): The URL of the admin user's avatar.
        team_priority_level (TeamPriorityLevelSchema): The priority level of the admin user's team.
    """
    type = fields.Str()
    id = fields.Str()
    name = fields.Str()
    email = fields.Str()
    email_verified = fields.Boolean()
    job_title = fields.Str()
    away_mode_enabled = fields.Boolean(allow_none=True)
    away_mode_reassign = fields.Boolean(allow_none=True)
    has_inbox_seat = fields.Boolean()
    team_ids = fields.List(fields.Int())
    avatar = fields.Nested(AdminAvatarSchema)
    app = fields.Nested(AdminAppSchema)
    team_priority_level = fields.Nested(TeamPriorityLevelSchema)

    @marshmallow.post_load
    def make_admin(self, data, **kwargs):
        return Admin(**data)


class AdminListSchema(SchemaBase):
    type = fields.Str()
    admins = fields.List(fields.Nested(AdminSchema))

    @marshmallow.post_load
    def make_admin_list(self, data, **kwargs):
        return AdminList(**data)
