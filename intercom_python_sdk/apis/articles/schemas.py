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
        url (str): The URL of the Article.can be null if the Article is not published.
        parent_id (int): The ID of the parent of the Article. can be null if the Article is not a child of another Article.
        parent_type (str): The type of the parent of the Article. can be null if the Article is not a child of another Article.
        default_locale (str): The default locale of the Article.
        statistics (dict): The statistics of the Article.
    """
    id = fields.Int(required=True)
    type = fields.Str()
    workspace_id = fields.Str()
    title = fields.Str()
    description = fields.Str(allow_none=True)
    body = fields.Str()
    author_id = fields.Int()
    state = fields.Str(allow_none=True)
    created_at = fields.Int(allow_none=True)
    updated_at = fields.Int(allow_none=True)
    url = fields.Str(allow_none=True)
    default_locale = fields.Str()
    translated_content = fields.Dict()
    statistics = fields.Nested(ArticleStatisticsSchema)

    parent_id = fields.Int(allow_none=True)
    parent_type = fields.Str(allow_none=True)
    

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
    
    """
    {
  "type": "list",
  "pages": {
    "type": "pages",
    "next": "https://api.intercom.io/articles?per_page=25&page=2",
    "page": 1,
    "per_page": 25,
    "total_pages": 6
  },
  "total_count": 150,
  "data": [
    {
      "id": "8117054",
      "type": "article",
      "workspace_id": "awwxrc0h",
      "parent_id": 2919918,
      "parent_type": "section",
      "title": "Guided Mode For Machines",
      "description": "Unlocking the Full Experience: Exploring and Mastering Guided Mode",
      "body": "",
      "author_id": 6396415,
      "state": "published",
      "created_at": 1689086414,
      "updated_at": 1689161069,
      "url": "https://help.hackthebox.com/en/articles/8117054-guided-mode-for-machines"
    },
    {
      "id": "8116542",
      "type": "article",
      "workspace_id": "awwxrc0h",
      "parent_id": 2919960,
      "parent_type": "collection",
      "title": "HTB Affiliate Program: Program Policy & Guidelines",
      "description": "Resources, assets, and content to help you make Hack The Box available to your audience, so you can collect more affiliate rewards!",
      "body": "TEST",
      "author_id": 5165498,
      "state": "published",
      "created_at": 1689081668,
      "updated_at": 1689088989,
      "url": "https://help.hackthebox.com/en/articles/8116542-htb-affiliate-program-program-policy-guidelines"
    },
    {
    """

class ArticleListSchema(SchemaBase):
    pages = fields.Dict()
    total_count = fields.Int()
    data = fields.Nested(ArticleSchema, many=True)

    @marshmallow.post_load
    def make_article_list(self, data, **kwargs):
        return a_models.ArticleList(**data)