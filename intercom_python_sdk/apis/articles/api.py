""" 
====================
Articles API
====================
`apis/articles/api.py`

This module contains the ArticlesAPI class, which defines a client for the Articles API.
It is used to interact with the Intercom Articles API [1] as defined in the Intercom API Reference [2].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/articles
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
import functools
from typing import Union, cast

# External
from uplink import (
    get, put, post,
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query,delete
)

# From Current API
from .schemas import (
    ArticleSchema,
    ArticleStatisticsSchema,
    CreateArticleSchema,
    DeletedArticleSchema,
    ArticleListSchema
)
from .models import Article, ArticleStatistics, CreateArticle, DeletedArticle, ArticleList

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error

@response_handler(catch_api_error)
class ArticlesAPI(APIBase):
    URI = "/articles/"

    @returns(ArticleSchema(many=False)) # type: ignore
    @get("{article_id}")
    def get_by_id(self, article_id: Union[str, int]):
        """ Get an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            Article: The Article with the given ID.
        """
    
    @returns(ArticleSchema(many=False)) # type: ignore
    @post("")
    def create(self, data: Body(type=CreateArticleSchema)): # type: ignore

        """ Create an Article.

        Args:
            data (Body(type=CreateArticleSchema)): The data to create the Article with.

        Returns:
            Article: The created Article.
        """


    @returns(DeletedArticleSchema(many=False)) # type: ignore
    @delete("{article_id}")
    def delete_by_id(self, article_id: Union[str, int]):
        """ Delete an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            DeletedArticle: The deleted Article.
        """


    @returns(ArticleListSchema(many=False)) # type: ignore
    @get("")
    def list_all(self, page: Query("page", int) = 1, per_page: Query("per_page", int) = 50, order: Query("order", str) = None, sort: Query("sort", str) = None, type: Query("type", str) = None, workspace_id: Query("workspace_id", str) = None, parent_id: Query("parent_id", str) = None, parent_type: Query("parent_type", str) = None, tag_id: Query("tag_id", str) = None, query: Query("query", str) = None, label_id: Query("label_id", str) = None, include: Query("include", str) = None, label_type: Query("label_type", str) = None, label_name: Query("label_name", str) = None, label_color: Query("label_color", str) = None, label_parent_id: Query("label_parent_id", str) = None, label_parent_type: Query("label_parent_type", str) = None, label_parent_name: Query("label_parent_name", str) = None, label_parent_color: Query("label_parent_color", str) = None, label_parent_parent_id: Query("label_parent_parent_id", str) = None, label_parent_parent_type: Query("label_parent_parent_type", str) = None, label_parent_parent_name: Query("label_parent_parent_name", str) = None, label_parent_parent_color: Query("label_parent_parent_color", str) = None): # type: ignore
        """ List all Articles.

        Args:
            page (int): The page number.
            per_page (int): The number of Articles per page.
            order (str): The order to sort the Articles by. Valid values are 'asc' and 'desc'. (Optional)
            sort (str): The field to sort the Articles by. Valid values are 'created_at' and 'updated_at'. (Optional)
            type (str): The type of Articles to list. Valid values are 'article' and 'folder'. (Optional)
            workspace_id (str): The ID of the workspace to filter by. (Optional)
            parent_id (str): The ID of the parent to filter by. (Optional)
            parent_type (str): The type of the parent to filter by. (Optional)


            """

    @returns(ArticleSchema(many=False)) # type: ignore
    @json
    @put("{article_id}")
    def update_by_id(self, article_id: Union[str, int], data: Body(type=ArticleSchema)): # type: ignore
        """ Update an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.
            data (Body(type=ArticleSchema)): The data to update the Article with.

        """