"""
# Help Center API Models

`apis/help_center/models.py`

This module contains models used to interact with the Intercom Help Center API [1].
These models provide object oriented interfaces for the schemas defined in `apis/help_center/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listallcollections
"""

# External
from typing import Union, TYPE_CHECKING, Optional as Opt

# From Current API
from . import schemas as hc_schemas

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import HelpCenterAPI


class Collection(ModelBase):
    """
    This model represents a Collection on Intercom.
    Attributes
        id (str): The ID of the Collection.
        type (str): The type of the Collection.
        workspace_id (str): The ID of the workspace the Collection belongs to.
        name (str): The name of the Collection.
        description (str): The description of the Collection.
        created_at (str): The timestamp of when the Collection was created.
        updated_at (str): The timestamp of when the Collection was updated.
        url (str): The URL of the Collection.
        icon (str): The icon of the Collection.
        order (str): The order of the Collection.
        default_locale (str): The default locale of the Collection.
        translated_content (dict): The translated content of the Collection.
    """
    def __init__(self, *args, **kwargs):
        self.__id: int = kwargs.get('id', int())
        self.__type: str = kwargs.get('type', '')
        self.__workspace_id: str = kwargs.get('workspace_id', None)
        self.__name: str = kwargs.get('name', '')
        self.__description = kwargs.get('description', '')
        self.__created_at: int = kwargs.get('created_at', None)
        self.__updated_at: int = kwargs.get('updated_at', None)
        self.__url: str = kwargs.get('url', '')
        self.__icon: str = kwargs.get('icon', '')
        self.__order: int = kwargs.get('order', 0)
        self.__default_locale: str = kwargs.get('default_locale', 0)
        self.__translated_content: dict = kwargs.get('translated_content', {})
        self.__parent_id: int = kwargs.get('parent_id', None)
        
    # Properties
    @property
    def api_client(self) -> 'HelpCenterAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client
    
    @property
    def type(self) -> str:
        return self.__type

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def workspace_id(self) -> Opt[str]:
        return self.__workspace_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def created_at(self) -> Opt[int]:
        return self.__created_at
    
    @property
    def updated_at(self) -> Opt[int]:
        return self.__updated_at
    
    @property
    def url(self) -> str:
        return self.__url
    
    @property
    def icon(self) -> str:
        return self.__icon
    
    @property
    def order(self) -> Opt[int]:
        return self.__order
    
    @property
    def default_locale(self) -> str:
        return self.__default_locale
    
    @property
    def translated_content(self) -> dict:
        return self.__translated_content
    
    @property
    def parent_id(self) -> int:
        return self.__parent_id
    
    # Property Setters
    @api_client.setter
    def api_client(self, api_client: 'HelpCenterAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (HelpCenterAPI): The API client used by the model instance.
        """
        self._api_client = api_client


    @id.setter
    def id(self, id: Union[int, str]):
        self.__id = int(id)

    @type.setter
    def type(self, type: str):
        self.__type = type

    @workspace_id.setter
    def workspace_id(self, workspace_id: str):
        self.__workspace_id = workspace_id

    @name.setter
    def name(self, name: str):
        self.__name = name

    @description.setter
    def description(self, description: str):
        self.__description = description

    @created_at.setter
    def created_at(self, created_at: int):
        self.__created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at: int):
        self.__updated_at = updated_at

    @url.setter
    def url(self, url: str):
        self.__url = url

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @order.setter
    def order(self, order: int):
        self.__order = order
    
    @default_locale.setter
    def default_locale(self, default_locale: str):
        self.__default_locale = default_locale

    @translated_content.setter
    def translated_content(self, translated_content: dict):
        self.__translated_content = translated_content

    @parent_id.setter
    def parent_id(self, parent_id: int):
        self.__parent_id = parent_id

    def update(self):
        """ Update the Collection. """
        data = hc_schemas.CollectionSchema().dump(self)
        schema = hc_schemas.CollectionSchema().load(data)
        self.api_client.update_collection_by_id(self.id, schema)


class CollectionList(ModelBase):
    def __init__(self, *args, **kwargs):
        self.__type: str = kwargs.get('type', '')
        self.__data: list = kwargs.get('data', [])
        self.__total_count: int = kwargs.get('total_count', 0)
        self.__pages: dict = kwargs.get('pages', {})

    # Properties
    @property
    def api_client(self) -> 'HelpCenterAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def data(self) -> list:
        return self.__data
    
    @property
    def collections(self) -> list:
        """ Alias for data """
        return self.__data
    
    @property
    def total_count(self) -> int:
        return self.__total_count
    
    @property
    def pages(self) -> dict:
        return self.__pages

    # Property Setters
    @api_client.setter
    def api_client(self, api_client: 'HelpCenterAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (HelpCenterAPI): The API client used by the model instance.
        """
        self._api_client = api_client

    @type.setter
    def type(self, type: str):
        self.__type = type

    @data.setter
    def data(self, data: list):
        self.__data = data

    @collections.setter
    def collections(self, collections: list):
        """ Alias for data """
        self.__data = collections

    @total_count.setter
    def total_count(self, total_count: int):
        self.__total_count = total_count

    @pages.setter
    def pages(self, pages: dict):
        self.__pages = pages

    def get_by_id(self, id: Union[str, int]):
        """ Get a Collection by ID.

        Args:
            id (Union[str, int]): The ID of the Collection.

        Returns:
            Collection: The Collection with the given ID.
        """
        return next(
            (collection for collection in self.data if collection.id == id), None
        )

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value: 'Collection'):
        self.data[index] = value

    def __len__(self):
        return len(self.data)


class Section(ModelBase):
    def __init__(self, *args, **kwargs):
        self.__id: int = kwargs.get('id', int())
        self.__type: str = kwargs.get('type', '')
        self.__workspace_id: str = kwargs.get('workspace_id', '')
        self.__name: str = kwargs.get('name', '')
        self.__created_at: int = kwargs.get('created_at', int())
        self.__updated_at: int = kwargs.get('updated_at', int())
        self.__url: str = kwargs.get('url', '')
        self.__icon: str = kwargs.get('icon', '')
        self.__order: int = kwargs.get('order', '')
        self.__collection_id: int = kwargs.get('collection_id', int())
        self.__default_locale: str = kwargs.get('default_locale', '')
        self.__translated_content: dict = kwargs.get('translated_content', dict())

    # Properties
    @property
    def api_client(self) -> 'HelpCenterAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client

    @property
    def id(self) -> int:
        return self.__id

    @property
    def type(self) -> str:
        return self.__type

    @property
    def workspace_id(self) -> str:
        return self.__workspace_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def created_at(self) -> int:
        return self.__created_at

    @property
    def updated_at(self) -> int:
        return self.__updated_at

    @property
    def url(self) -> str:
        return self.__url

    @property
    def icon(self) -> str:
        return self.__icon

    @property
    def order(self) -> int:
        return self.__order

    @property
    def collection_id(self) -> int:
        return self.__collection_id

    @property
    def default_locale(self) -> str:
        return self.__default_locale

    @property
    def translated_content(self) -> dict:
        return self.__translated_content

    # Property Setters
    @api_client.setter
    def api_client(self, api_client: 'HelpCenterAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (HelpCenterAPI): The API client used by the model instance.
        """
        self._api_client = api_client

    @id.setter
    def id(self, id: Union[str, int]):
        self.__id = int(id)

    @type.setter
    def type(self, type: str):
        self.__type = type

    @workspace_id.setter
    def workspace_id(self, workspace_id: str):
        self.__workspace_id = workspace_id

    @name.setter
    def name(self, name: str):
        self.__name = name

    @created_at.setter
    def created_at(self, created_at: int):
        self.__created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at: int):

        self.__updated_at = updated_at

    @url.setter
    def url(self, url: str):
        self.__url = url

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @order.setter
    def order(self, order: int):
        self.__order = order

    @collection_id.setter
    def collection_id(self, collection_id: int):
        self.__collection_id = collection_id

    @default_locale.setter
    def default_locale(self, default_locale: str):
        self.__default_locale = default_locale

    @translated_content.setter
    def translated_content(self, translated_content: dict):
        self.__translated_content = translated_content


class SectionList(ModelBase):
    def __init__(self, *args, **kwargs):
        self.__type: str = kwargs.get('type', '')
        self.__data: list = kwargs.get('data', [])
        self.__total_count = kwargs.get('total_count', int())
        self.__pages = kwargs.get('pages', int())

    # Properties
    @property
    def api_client(self) -> 'HelpCenterAPI':
        """
        The API client used by the model instance.

        Returns:
            ArticlesAPI: The API client used by the model instance.
        """
        return self._api_client
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def data(self) -> list:
        return self.__data
    
    @property
    def total_count(self) -> int:
        return self.__total_count
    
    @property
    def pages(self) -> dict:
        return self.__pages

    # Property Setters
    @api_client.setter
    def api_client(self, api_client: 'HelpCenterAPI'):
        """
        The API client used by the model instance.

        Args:
            api_client (HelpCenterAPI): The API client used by the model instance.
        """
        self._api_client = api_client

    @type.setter
    def type(self, type: str):
        self.__type = type

    @data.setter
    def data(self, data: list):
        self.__data = data

    @total_count.setter
    def total_count(self, total_count: int):
        self.__total_count = total_count

    @pages.setter
    def pages(self, pages: dict):
        self.__pages = pages
