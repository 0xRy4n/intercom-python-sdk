""" 
# Data Attributes API

`apis/data_attributes/api.py`

This module contains the Data Attributes API class, which defines a client for the Data Attributes API.
It is used to interact with the Intercom Data Attributes API [1] as defined in the Intercom API Reference [2].

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
- [2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
from typing import Union

# External
import marshmallow
from uplink import (
    get, put, post,
    returns, json,
    response_handler,
    Body, Query
)

# From Current API
from .schemas import (
    DataAttributeSchema,
    DataAttributeListSchema
)

from .models import (
    DataAttribute,
)

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class DataAttributesAPI(APIBase):
    URI = "/data_attributes/"

    @returns(DataAttributeListSchema()) # type: ignore
    @get("")
    def list_all(self, include_archived: Query("include_archived", bool) = False, model: Query("model", str) = None): # type: ignore
        """ List all data attributes. 
        
        Args:
            include_archived (bool): Whether or not to include archived data attributes. Defaults to False. (Optional)
            model (str): The model to filter by. Valid values are 'contact', 'company', and 'conversation'. (Optional)

        Returns:
            DataAttributeList: A list of data attributes.
        """

    @returns(DataAttributeSchema()) # type: ignore
    @post("")
    def create(self, attribute: Body(type=DataAttributeSchema)): # type: ignore
        """ Create a new data attribute. 
        
        Args:
            attribute (DataAttribute): The data attribute to create.
        
        Returns:
            DataAttribute: The newly created data attribute.
        """
    
    @returns(DataAttributeSchema()) # type: ignore
    @json
    @put("{attribute_id}")
    def update_by_id(self, attribute_id: Union[str, int], attribute: Body(type=DataAttributeSchema)): # type: ignore
        """ Update a data attribute by ID.
         
        Args:
            attribute_id (Union[str, int]): The ID of the data attribute.
            attribute (DataAttribute): The updated data attribute.

        Returns:
            DataAttribute: The updated data attribute.
        """

    # Helper Methods

    def get_by_id(self, attribute_id: Union[str, int]) -> Union[DataAttribute, None]:
        """ Get a data attribute by ID. 
        
        Args:
            attribute_id (Union[str, int]): The ID of the data attribute.

        Returns:
            DataAttribute: The data attribute with the given ID.
        """
        data_attribute_list = self.list_all()
        for data_attribute in data_attribute_list: # type: ignore
            if data_attribute.id == attribute_id:
                return data_attribute
    
    @returns(DataAttributeSchema(many=False)) # type: ignore
    def archive_by_id(self, attribute_id: Union[str, int]):
        """ Archive a data attribute by ID.

        Args:
            attribute_id (Union[str, int]): The ID of the data attribute.

        Returns:
            DataAttribute: The archived data attribute.
        """
        data_attribute = self.get_by_id(attribute_id)
        if data_attribute is None:
            raise ValueError(f"Data attribute with ID {attribute_id} not found.")
        data_attribute.archived = True
        
        return self.update_by_id(attribute_id, data_attribute)