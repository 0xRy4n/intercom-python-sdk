
"""
# Data Attributes API Models

`apis/data_attributes/models.py`

This module contains models used to interact with the Intercom Admins API [1].
These models provide object oriented interfaces for the schemas defined in `apis/data_attributes/schemas.py`.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
"""
# Built-ins
from typing import (
    Union,
    List,
    TYPE_CHECKING
)

# From Current API
from . import schemas as da_schemas

# From Current Package
from ...core.model_base import ModelBase

# Type Check Imports - TYPE_CHECKING is assumed True by type-checkers but is False at runtime.
# See: https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING
if TYPE_CHECKING:
    from .api import DataAttributesAPI


class DataAttribute(ModelBase):
    """ Represents a Data Attribute as an object. """
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
    def api_client(self) -> 'DataAttributesAPI':
        """
        Get the API client used to interact with the data attribute.

        Returns:
            DataAttributesAPI: The API client used to interact with the data attribute.
        """
        return self._api_client
    
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
    
    # Property Setters
    
    @api_client.setter
    def api_client(self, value: 'DataAttributesAPI'):
        """ Setter for the api_client property """
        self._api_client = value
    
    @type.setter
    def type(self, value: str):
        """ Setter for the type property """
        self.__type = value

    @id.setter
    def id(self, value: Union[str, None]):
        """ Setter for the id property """
        self.__id = value
    
    @model.setter
    def model(self, value: str):
        """ Setter for the model property """
        self.__model = value
    
    @name.setter
    def name(self, value: str):
        """ Setter for the name property """
        self.__name = value
    
    @full_name.setter
    def full_name(self, value: str):
        """ Setter for the full_name property """
        self.__full_name = value
    
    @label.setter
    def label(self, value: str):
        """ Setter for the label property """
        self.__label = value
    
    @description.setter
    def description(self, value: str):
        """ Setter for the description property """
        self.__description = value
    
    @data_type.setter
    def data_type(self, value: str):
        """ Setter for the data_type property """
        self.__data_type = value
    
    @options.setter
    def options(self, value: List[str]):
        """ Setter for the options property """
        self.__options = value
    
    @api_writable.setter
    def api_writable(self, value: Union[int, None]):
        """ Setter for the api_writable property """
        self.__api_writable = value

    @ui_writable.setter
    def ui_writable(self, value: Union[int, None]):
        """ Setter for the ui_writable property """
        self.__ui_writable = value

    @custom.setter
    def custom(self, value: Union[int, None]):
        """ Setter for the custom property """
        self.__custom = value

    @archived.setter
    def archived(self, value: Union[int, None]):
        """ Setter for the archived property """
        self.__archived = value
    
    @created_at.setter
    def created_at(self, value: Union[int, None]):
        """ Setter for the created_at property """
        self.__created_at = value
    
    @updated_at.setter
    def updated_at(self, value: Union[int, None]):
        """ Setter for the updated_at property """
        self.__updated_at = value
    
    @admin_id.setter
    def admin_id(self, value: Union[int, None]):
        """ Setter for the admin_id property """
        self.__admin_id = value

    # Methods
    def update(self):
        """
        Update the data attribute to match the current object.
        """
        if not (self.id and self.api_writable):
            raise ValueError('This data attribute is not writable.')
        
        data = da_schemas.DataAttributeSchema().dump(self)
        schema = da_schemas.DataAttributeSchema().load(data, partial=True)
        self.api_client.update_by_id(self.id, schema)


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
    
    # Methods

    def get_attribute_by_id(self, id: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified ID.

        Args:
            id (str): The ID of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified ID. None if not found.
        """
        return next(
            (attribute for attribute in self.__data if attribute.id == id), None
        )
    
    def get_attribute_by_name(self, name: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified name.

        Args:
            name (str): The name of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified name. None if not found.
        """
        return next(
            (attribute for attribute in self.__data if attribute.name == name),
            None,
        )
    
    def get_attribute_by_full_name(self, full_name: str) -> Union[DataAttribute, None]:
        """
        Get the data attribute with the specified full name.

        Args:
            full_name (str): The full name of the data attribute to get.

        Returns:
            DataAttribute: The data attribute with the specified full name. None if not found.
        """
        return next(
            (
                attribute
                for attribute in self.__data
                if attribute.full_name == full_name
            ),
            None,
        )
    
    # Dunder Overrides

    def __getitem__(self, key: int) -> Union[DataAttribute, None]:
        return self.__data[key]

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
    
    def __contains__(self, item: Union[DataAttribute, str]) -> bool:
        """
        Returns True if the data attribute list contains the specified item.

        Args:
            item (Union[DataAttribute, str]): The item to check for.
        Returns:
            bool: True if the data attribute list contains the specified item.
        """
        if isinstance(item, DataAttribute):
            return item in self.__data
        elif isinstance(item, str):
            return any(
                attribute.name == item or attribute.full_name == item
                for attribute in self.__data
            )
        else:
            return False