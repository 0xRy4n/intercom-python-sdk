
"""
====================
Data Attributes API Models
====================
`apis/data_attributes/models.py`

This module contains models used to interact with the Intercom Admins API [1].
These models provide object oriented interfaces for the schemas defined in `apis/data_attributes/schemas.py`.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
"""
# Built-ins
from typing import Union, TYPE_CHECKING, List

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# We can use this to allow for type hinting without causing circular imports.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import DataAttributesAPI


class DataAttribute(ModelBase):
    """
    Represents a data attribute.

    Attributes:
        See the `DataAttributeSchema` definition in `apis/data_attributes/schemas.py` for details.
    """
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type', '')
        self.__id = kwargs.get('id', None)
        self.__model = kwargs.get('model', '')
        self.__name = kwargs.get('name', '')
        self.__full_name = kwargs.get('full_name', '')
        self.__label = kwargs.get('label', '')
        self.__description = kwargs.get('description', '')
        self.__data_type = kwargs.get('data_type', '')
        self.__options = kwargs.get('options', [])
        self.__api_writable = kwargs.get('api_writable', None)
        self.__ui_writable = kwargs.get('ui_writable', None)
        self.__custom = kwargs.get('custom', None)
        self.__archived = kwargs.get('archived', None)
        self.__created_at = kwargs.get('created_at', None)
        self.__updated_at = kwargs.get('updated_at', None)
        self.__admin_id = kwargs.get('admin_id', None)

    # Properties

    @property
    def type(self) -> str:
        """
        Get the type of the data attribute.

        Returns:
            str: The type of the data attribute.
        """
        return self.__type
    
    @property
    def id(self) -> Union[str, None]:
        """
        Get the ID of the data attribute.

        Returns:
            str: The ID of the data attribute.
        """
        return self.__id
    
    @property
    def model(self) -> str:
        """
        Get the model of the data attribute.

        Returns:
            str: The model of the data attribute.
        """
        return self.__model
    
    @property
    def name(self) -> str:
        """
        Get the name of the data attribute.

        Returns:
            str: The name of the data attribute.
        """
        return self.__name
    
    @property
    def full_name(self) -> str:
        """
        Get the full name of the data attribute.

        Returns:
            str: The full name of the data attribute.
        """
        return self.__full_name
    
    @property
    def label(self) -> str:
        """
        Get the label of the data attribute.

        Returns:
            str: The label of the data attribute.
        """
        return self.__label
    
    @property
    def description(self) -> str:
        """
        Get the description of the data attribute.

        Returns:
            str: The description of the data attribute.
        """
        return self.__description
    
    @property
    def data_type(self) -> str:
        """
        Get the data type of the data attribute.

        Returns:
            str: The data type of the data attribute.
        """
        return self.__data_type
    
    @property
    def options(self) -> List[str]:
        """
        Get the options of the data attribute.

        Returns:
            str: The options of the data attribute.
        """
        return self.__options
    
    @property
    def api_writable(self) -> Union[int, None]:
        """
        Get the API writable of the data attribute.

        Returns:
            str: The API writable of the data attribute.
        """
        return self.__api_writable
    
    @property
    def ui_writable(self) -> Union[int, None]:
        """
        Get the UI writable of the data attribute.

        Returns:
            str: The UI writable of the data attribute.
        """
        return self.__ui_writable
    
    @property
    def custom(self) -> Union[int, None]:
        """
        Get the custom of the data attribute.

        Returns:
            str: The custom of the data attribute.
        """
        return self.__custom
    
    @property
    def archived(self) -> Union[int, None]:
        """
        Get the archived of the data attribute.

        Returns:
            str: The archived of the data attribute.
        """
        return self.__archived

    @property
    def created_at(self) -> Union[int, None]:
        """
        Get the created at of the data attribute.

        Returns:
            str: The created at of the data attribute.
        """
        return self.__created_at
    
    @property
    def updated_at(self) -> Union[int, None]:
        """
        Get the updated at of the data attribute.

        Returns:
            str: The updated at of the data attribute.
        """
        return self.__updated_at

    @property
    def admin_id(self) -> Union[int, None]:
        """
        Get the admin id of the data attribute.

        Returns:
            str: The admin id of the data attribute.
        """
        return self.__admin_id


class DataAttributeList(ModelBase):
    """
    Represents a list of data attributes.

    Attributes:
        See the `DataAttributeListSchema` definition in `apis/data_attributes/schemas.py` for details.
    """
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.get('type', '')
        self.__data = kwargs.get('data', [])
    
    # Properties

    @property
    def type(self) -> str:
        """
        Get the type of the data attribute list.

        Returns:
            str: The type of the data attribute list.
        """
        return self.__type
    
    @property
    def data(self) -> List[DataAttribute]:
        """
        Get the data of the data attribute list.

        Returns:
            str: The data of the data attribute list.
        """
        return self.__data
    
    def __iter__(self):
        """
        Returns an iterator for the data attribute list.

        Returns:
            Iterator[DataAttribute]: An iterator for the data attribute list.
        """
        return iter(self.__data)
    
    def __len__(self):
        """
        Returns the length of the data attribute list.

        Returns:
            int: The length of the data attribute list.
        """
        return len(self.__data)
    
    # Methods

    def get_attribute_by_id(self, id: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified ID.

        Args:
            id (str): The ID of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified ID. None if not found.
        """
        for attribute in self.__data:
            if attribute.id == id:
                return attribute
        return None
    
    def get_attribute_by_name(self, name: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified name.

        Args:
            name (str): The name of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified name. None if not found.
        """
        for attribute in self.__data:
            if attribute.name == name:
                return attribute
        return None
    
    def get_attribute_by_full_name(self, full_name: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified full name.

        Args:
            full_name (str): The full name of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified full name. None if not found.
        """
        for attribute in self.__data:
            if attribute.full_name == full_name:
                return attribute
        return None
    
