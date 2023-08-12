"""
# Articles API Models

`apis/help_center/models.py`

This module contains models used to interact with the Intercom Help Center API [1].
These models provide object oriented interfaces for the schemas defined in `apis/help_center/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/listallcollections
"""

# External
import marshmallow
from marshmallow import fields
from typing import List, Optional, Union , TYPE_CHECKING

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
        self.__id = kwargs.get('id')
        self.__type = kwargs.get('type')
        self.__workspace_id = kwargs.get('workspace_id')
        self.__name = kwargs.get('name')
        self.__description = kwargs.get('description')
        self.__created_at = kwargs.get('created_at')
        self.__updated_at = kwargs.get('updated_at')
        self.__url = kwargs.get('url')
        self.__icon = kwargs.get('icon')
        self.__order = kwargs.get('order')
        self.__default_locale = kwargs.get('default_locale',None)
        self.__translated_content = kwargs.get('translated_content',None)
        


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
    def id(self) -> str:
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
    def description(self) -> str:
        return self.__description
    
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
    def id(self, id: str):
        self.__id = id

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
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at: str):
        self.__updated_at = updated_at

    @url.setter
    def url(self, url: str):
        self.__url = url

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @order.setter
    def order(self, order: str):
        self.__order = order
    
    @default_locale.setter
    def default_locale(self, default_locale: str):
        self.__default_locale = default_locale

    @translated_content.setter
    def translated_content(self, translated_content: dict):
        self.__translated_content = translated_content

    
    

class CollectionList(ModelBase):
    

    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type')
        self.__data = kwargs.get('data')
        self.__total_count = kwargs.get('total_count')
        self.__pages = kwargs.get('pages')
        


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



"""
    id = fields.Str()
    type = fields.Str()
    parent_id = fields.Int()
    workspace_id = fields.Str()
    name = fields.Str()
    created_at = fields.Int()
    updated_at = fields.Int()
    url = fields.Str()
    icon = fields.Str()
    order = fields.Int()
    collection_id = fields.Str()
    default_locale = fields.Str(allow_none=True)
    translated_content = fields.Dict(allow_none=True)
"""

class Section(ModelBase):

    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get('id')
        self.__type = kwargs.get('type')
        self.__workspace_id = kwargs.get('workspace_id')
        self.__name = kwargs.get('name')
        self.__created_at = kwargs.get('created_at')
        self.__updated_at = kwargs.get('updated_at')
        self.__url = kwargs.get('url')
        self.__icon = kwargs.get('icon')
        self.__order = kwargs.get('order')
        self.__collection_id = kwargs.get('collection_id')
        self.__default_locale = kwargs.get('default_locale',None)
        self.__translated_content = kwargs.get('translated_content',None)


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
    def id(self) -> str:
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
    def collection_id(self) -> str:
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
    def id(self, id: str):
        self.__id = id

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
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at: str):

        self.__updated_at = updated_at

    @url.setter
    def url(self, url: str):
        self.__url = url

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @order.setter
    def order(self, order: str):
        self.__order = order

    @collection_id.setter
    def collection_id(self, collection_id: str):
        self.__collection_id = collection_id
    
    @default_locale.setter
    def default_locale(self, default_locale: str):
        self.__default_locale = default_locale

    @translated_content.setter
    def translated_content(self, translated_content: dict):
        self.__translated_content = translated_content


class SectionList(ModelBase):
    
        def __init__(self, *args, **kwargs):
            self.__type = kwargs.get('type')
            self.__data = kwargs.get('data')
            self.__total_count = kwargs.get('total_count')
            self.__pages = kwargs.get('pages')
            
    
    
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







    


    