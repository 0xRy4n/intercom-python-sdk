""" 
# Articles API

`apis/articles/api.py`

This module contains the ArticlesAPI class, which defines a client for the Articles API.
It is used to interact with the Intercom Articles API [1] as defined in the Intercom API Reference [2].

---
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
    ArticleListSchema
)
from .models import Article, ArticleStatistics, ArticleList

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error

@response_handler(catch_api_error)
class ArticlesAPI(APIBase):
    URI = "/articles/"

    @returns(ArticleSchema) # type: ignore
    @get("{article_id}")
    def get_by_id(self, article_id: Union[str, int]):
        """ Get an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            Article: The Article with the given ID.
        """
    
    @returns(ArticleSchema) # type: ignore
    @json
    @post("")
    def create(self, data: Body(type=ArticleSchema)): # type: ignore

        """ Create an Article.

        Args:
            data (ArticleSchema): The ArticleSchema to create the article with.

        Returns:
            Article: The created Article.
        """

    @returns(ArticleSchema) # type: ignore
    @delete("{article_id}")
    def delete_by_id(self, article_id: Union[str, int]):
        """ Delete an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            DeletedArticle: The deleted Article.
        """

    @returns(ArticleListSchema) # type: ignore
    @get("")
    def __list_all(self, page: Query('page'), per_page: Query('per_page') = 50):
        """ List all Articles. """

    def list_all(self, page: int = 1, per_page: int = 50) -> ArticleList:
        """ List all Articles. Automatically paginates through all Articles.

        Args:
            start (int): The page number to start at.
            per_page (int): The number of Articles to return per page.

        Returns:
            ArticleList: A list of Articles.
        """

        article_list = self.__list_all(page=page, per_page=per_page)
        while page < article_list.pages['total_pages']:
            page += 1
            new_page = self.__list_all(page=page, per_page=per_page)
            article_list.extend(new_page)
            article_list.pages = new_page.pages
        
        return article_list

    @returns(ArticleSchema) # type: ignore
    @json
    @put("{article_id}")
    def update_by_id(self, article_id: Union[str, int], data: Body(type=ArticleSchema)): # type: ignore
        """ Update an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.
            data (ArticleSchema): An article schema object to update via. 
        """