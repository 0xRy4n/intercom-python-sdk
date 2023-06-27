from marshmallow import Schema, fields

class AdminSchema(Schema):
    type = fields.Str()
    id = fields.Str()
    name = fields.Str()
    email = fields.Str()
    job_title = fields.Str()
    away_mode_enabled = fields.Boolean()
    away_mode_reassign = fields.Boolean()
    has_inbox_seat = fields.Boolean()
    team_ids = fields.List(fields.Int())
    avatar = fields.Str()
    team_priority_level = fields.Object()

class