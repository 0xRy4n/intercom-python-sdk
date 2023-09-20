"""
# Articles API Models

`apis/articles/models.py`

This module contains models used to interact with the Intercom Articles API [1].
These models provide object oriented interfaces for the schemas defined in `apis/articles/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listarticles
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
from . import schemas as a_schemas

# From Current Package
from ...core.model_base import ModelBase

from .languages import ArticleLanguages

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import ArticlesAPI


class ArticleStatistics(ModelBase):
    """
    This model represents the statistics of an Article on Intercom.

    Attributes:
        See the `ArticleStatisticsSchema` class.
    """
    views: Optional[int]
    conversations: Optional[int]
    reactions: Optional[int]
    happy_reaction_percentage: Optional[int]
    neutral_reaction_percentage: Optional[int]
    sad_reaction_percentage: Optional[int]


class Article(ModelBase):
    """
    This model represents an Article on Intercom.

    Attributes:
        See the `ArticleSchema` class.
    """
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type', 'article')
        self.__workspace_id = kwargs.get('workspace_id', '')
        self.__title = kwargs.get('title', '')
        self.__description = kwargs.get('description', '')
        self.__body = kwargs.get('body', '')
        self.__author_id = kwargs.get('author_id', None)
        self.__state = kwargs.get('state', '')
        self.__created_at = kwargs.get('created_at', None)
        self.__updated_at = kwargs.get('updated_at', None)
        self.__url = kwargs.get('url', '')
        self.__parent_id = kwargs.get('parent_id', None)
        self.__parent_type = kwargs.get('parent_type', '')
        self.__default_locale = kwargs.get('default_locale', '')
        self.__statistics = kwargs.get('statistics', None)
        self.__id = kwargs.get('id', None)
        self.__translated_content = kwargs.get('translated_content', {})

    # Properties
    @property
    def api_client(self) -> 'ArticlesAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client

    @property
    def type(self) -> str:
        """
        The type of the Article.

        Returns:
            str: The type of the Article.
        """
        return self.__type

    @property
    def workspace_id(self) -> str:
        """
        The ID of the workspace the Article belongs to.

        Returns:
            str: The ID of the workspace the Article belongs to.
        """
        return self.__workspace_id

    @property
    def title(self) -> str:
        """
        The title of the Article.

        Returns:
            str: The title of the Article.
        """
        return self.__title

    @property
    def description(self) -> str:
        """
        The description of the Article.

        Returns:
            str: The description of the Article.
        """
        return self.__description

    @property
    def body(self) -> str:
        """
        The body of the Article.

        Returns:
            str: The body of the Article.
        """
        return self.__body

    @property
    def author_id(self) -> Optional[int]:

        """
        The ID of the author of the Article.

        Returns:
            int: The ID of the author of the Article.
        """
        return self.__author_id

    @property
    def state(self) -> str:
        """
        The state of the Article.

        Returns:
            str: The state of the Article.
        """
        return self.__state

    @property
    def created_at(self) -> Optional[int]:
        """
        The timestamp of when the Article was created.

        Returns:
            int: The timestamp of when the Article was created.
        """
        return self.__created_at

    @property
    def updated_at(self) -> Optional[int]:
        """
        The timestamp of when the Article was updated.

        Returns:
            int: The timestamp of when the Article was updated.
        """
        return self.__updated_at

    @property
    def url(self) -> str:
        """
        The URL of the Article.

        Returns:
            str: The URL of the Article.
        """
        return self.__url

    @property
    def parent_id(self) -> Optional[int]:
        """
        The ID of the parent of the Article.

        Returns:
            int: The ID of the parent of the Article.
        """
        return self.__parent_id

    @property
    def parent_type(self) -> str:
        """
        The type of the parent of the Article.

        Returns:
            str: The type of the parent of the Article.
        """
        return self.__parent_type

    @property
    def default_locale(self) -> str:
        """
        The default locale of the Article.

        Returns:
            str: The default locale of the Article.
        """
        return self.__default_locale

    @property
    def statistics(self) -> Optional[ArticleStatistics]:
        """
        The statistics of the Article.

        Returns:
            ArticleStatistics: The statistics of the Article.
        """
        return self.__statistics

    @property
    def id(self) -> Optional[int]:
        """
        The ID of the Article.

        Returns:
            int: The ID of the Article.
        """
        return self.__id

    @property
    def translated_content(self) -> dict:
        """
        The translated content of the Article.

        Returns:
            dict: The translated content of the Article.
        """
        return self.__translated_content
    
    @property
    def content(self) -> BeautifulSoup:
        """
        The content of the Article as a BeautifulSoup object.

        Returns:
            BeautifulSoup: The content of the Article.
        """
        return BeautifulSoup(self.body, 'html.parser')

    # Property Setters

    @api_client.setter
    def api_client(self, api_client: 'ArticlesAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (ArticlesAPI): The API client used by the model instance.
        """
        self._api_client = api_client

    @type.setter
    def type(self, type: str):
        """
        The type of the Article.

        Args:
            type (str): The type of the Article.
        """
        self.__type = type

    @workspace_id.setter
    def workspace_id(self, workspace_id: str):
        """
        The ID of the workspace the Article belongs to.

        Args:
            workspace_id (str): The ID of the workspace the Article belongs to.
        """
        self.__workspace_id = workspace_id

    @title.setter
    def title(self, title: str):
        """
        The title of the Article.

        Args:
            title (str): The title of the Article.
        """
        self.__title = title

    @description.setter
    def description(self, description: str):
        """
        The description of the Article.

        Args:
            description (str): The description of the Article.
        """
        self.__description = description

    @body.setter
    def body(self, body: str):
        """
        The body of the Article.

        Args:
            body (str): The body of the Article.
        """
        self.__body = body

    @author_id.setter
    def author_id(self, author_id: int):
        """
        The ID of the author of the Article.

        Args:
            author_id (int): The ID of the author of the Article.
        """
        self.__author_id = author_id

    @state.setter
    def state(self, state: str):
        """
        The state of the Article.

        Args:
            state (str): The state of the Article.
        """
        self.__state = state

    @created_at.setter
    def created_at(self, created_at: int):
        """
        The timestamp of when the Article was created.

        Args:
            created_at (int): The timestamp of when the Article was created.
        """
        self.__created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at: int):
        """
        The timestamp of when the Article was updated.

        Args:
            updated_at (int): The timestamp of when the Article was updated.
        """
        self.__updated_at = updated_at

    @url.setter
    def url(self, url: str):
        """
        The URL of the Article.

        Args:
            url (str): The URL of the Article.
        """
        self.__url = url

    @parent_id.setter
    def parent_id(self, parent_id: int):
        """
        The ID of the parent of the Article.

        Args:
            parent_id (int): The ID of the parent of the Article.
        """
        self.__parent_id = parent_id

    @parent_type.setter
    def parent_type(self, parent_type: str):
        """
        The type of the parent of the Article.

        Args:
            parent_type (str): The type of the parent of the Article.
        """
        self.__parent_type = parent_type

    @default_locale.setter
    def default_locale(self, default_locale: str):
        """
        The default locale of the Article.

        Args:
            default_locale (str): The default locale of the Article.
        """
        self.__default_locale = default_locale

    @statistics.setter
    def statistics(self, statistics: ArticleStatistics):
        """
        The statistics of the Article.

        Args:
            statistics (ArticleStatistics): The statistics of the Article.
        """
        self.__statistics = statistics

    @id.setter
    def id(self, id: int):
        """
        The ID of the Article.

        Args:
            id (int): The ID of the Article.
        """
        self.__id = id

    @translated_content.setter
    def translated_content(self, translated_content: dict):
        """
        The translated content of the Article.

        Args:
            translated_content (dict): The translated content of the Article.
        """
        self.__translated_content = translated_content

    # Methods

    def update(self) -> 'Article':
        """
        Update the Article.
        """
        data = a_schemas.ArticleSchema().dump(self)
        schema = a_schemas.ArticleSchema().load(data)
        self.api_client.update_by_id(self.id, schema)


class ArticleList(ModelBase):
    """
    This model represents a list of Articles on Intercom.

    Attributes:
        See the `ArticleListSchema` class.
    """
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type', '')
        self.__pages = kwargs.get('pages', {})
        self.__total_count = kwargs.get('total_count', 0)
        self.__data = kwargs.get('data', [])

    # Properties
    @property
    def api_client(self) -> 'ArticlesAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client

    @property
    def type(self) -> str:
        """
        The type of the Article.

        Returns:
            str: The type of the Article.
        """
        return self.__type

    @property
    def pages(self) -> dict:
        """
        The pages of the Article.

        Returns:
            dict: The pages of the Article.
        """
        return self.__pages

    @property
    def total_count(self) -> int:
        """
        The total count of the Article.

        Returns:
            int: The total count of the Article.
        """
        return self.__total_count

    @property
    def data(self) -> List[Article]:
        """
        The data of the Article.

        Returns:
            List[Article]: The data of the Article.
        """
        return self.__data

    # Property Setters
    @api_client.setter
    def api_client(self, api_client: 'ArticlesAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (ArticlesAPI): The API client used by the model instance.
        """
        self._api_client = api_client

    @type.setter
    def type(self, type: str):
        """
        The type of the Article.

        Args:
            type (str): The type of the Article.
        """
        self.__type = type

    @pages.setter
    def pages(self, pages: dict):
        """
        The pages of the Article.

        Args:
            pages (dict): The pages of the Article.
        """
        self.__pages = pages

    @total_count.setter
    def total_count(self, total_count: int):
        """
        The total count of the Article.

        Args:
            total_count (int): The total count of the Article.
        """
        self.__total_count = total_count

    @data.setter
    def data(self, data: List[Article]):
        """
        The data of the Article.

        Args:
            data (List[Article]): The data of the Article.
        """
        self.__data = data

    def get_by_id(self, article_id: Union[str, int]) -> Optional[Article]:
        """
        Gets an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            Optional[Article]: The Article with the given ID.
        """
        return next(
            (article for article in self.data if article.id == article_id), None
        )

    def extend(self, articles: 'ArticleList'):
        """
        Extend the ArticleList with another ArticleList.

        Args:
            ArticleList (ArticleList): The ArticleList to extend.
        """
        article_ids = [a.id for a in self]
        for article in articles:
            if article.id not in article_ids:
                self.data.append(article)

    def __len__(self):
        """ The length of the ArticleList"""
        return len(self.data)

    def __iter__(self):
        """ Iterates over articles in the ArticleList

        Example:
            >>> article_list = intercom.articles.list_all()
            >>> [article for article in article_list]
        """
        return iter(self.data)

    def __getitem__(self, index):
        """ Gets an article from ArticleList.data at a given index.

        Example:
            >>> article_list = intercom.articles.list_all()
            >>> article_list[0]
        """
        return self.data[index]
