"""
====================
Articles API Schemas
====================
`apis/articles/schemas.py`

This module contains the schema definitions provided by the Intercom API Reference [1].
These schemas provide serialization/deserialization to and from the models defined in the 
`apis/data_attributes/models.py` module.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/the-article-model
"""

# External
import marshmallow
from marshmallow import fields

# From Current API
from . import models as a_models

# From Current Package
from ...core.schema_base import SchemaBase



class ArticleStatisticsSchema(SchemaBase):
    """
    This schema represents the statistics of an Article on Intercom.

    Attributes:
        views (int): The number of views of the Article.
        conversations (int): The number of conversations of the Article.
        reactions (int): The number of reactions of the Article.
        happy_reaction_percentage (int): The percentage of happy reactions of the Article.
        neutral_reaction_percentage (int): The percentage of neutral reactions of the Article.
        sad_reaction_percentage (int): The percentage of sad reactions of the Article.
    """
    views = fields.Int()
    conversations = fields.Int()
    reactions = fields.Int()
    happy_reaction_percentage = fields.Int()
    neutral_reaction_percentage = fields.Int()
    sad_reaction_percentage = fields.Int()



class ArticleSchema(SchemaBase):
    """
    This schema represents an Article on Intercom.

    Attributes:
        id (int): The ID of the Article.
        type (str): The type of the Article.
        workspace_id (str): The ID of the workspace the Article belongs to.
        title (str): The title of the Article.
        description (str): The description of the Article.
        body (str): The body of the Article.
        author_id (int): The ID of the author of the Article.
        state (str): The state of the Article.
        created_at (int): The timestamp of when the Article was created.
        updated_at (int): The timestamp of when the Article was updated.
        url (str): The URL of the Article.
        parent_id (int): The ID of the parent of the Article.
        parent_type (str): The type of the parent of the Article.
        default_locale (str): The default locale of the Article.
        statistics (dict): The statistics of the Article.
    """
    id = fields.Int()
    type = fields.Str()
    workspace_id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    body = fields.Str()
    author_id = fields.Int()
    state = fields.Str()
    created_at = fields.Int()
    updated_at = fields.Int()
    url = fields.Str()
    parent_id = fields.Int()
    parent_type = fields.Str()
    default_locale = fields.Str()
    translated_content = fields.Dict()
    statistics = fields.Nested(ArticleStatisticsSchema)

    @marshmallow.post_load
    def make_article(self, data, **kwargs):
        return a_models.Article(**data)
    

class CreateArticleSchema(SchemaBase):
    author_id = fields.Int()
    title = fields.Str()


    @marshmallow.post_load
    def make_article(self, data, **kwargs):
        return a_models.CreateArticle(**data)


class DeletedArticleSchema(SchemaBase):
    id = fields.Int()
    object = fields.Str()
    deleted = fields.Bool()

    @marshmallow.post_load
    def make_deleted_article(self, data, **kwargs):
        return a_models.DeletedArticle(**data)
    