"""
# Help Center API

`apis/help_center/api.py`

This module contains the HelpCenterAPI class, which defines a client for the Help Cneter API.
It is used to interact with the Intercom Help Center API [1] as defined in the Intercom API Reference [2].

---
[1] https://developers.intercom.com/intercom-api-reference/reference/help_center
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
from typing import Union, TYPE_CHECKING

# External
from uplink import (
    json,
    get, put,
    post, delete,
    Query, Body,
    returns, response_handler,
)

# From Current API
from .schemas import (
    CollectionSchema,
    CollectionListSchema,
    SectionSchema,
    SectionListSchema,
)

if TYPE_CHECKING:
    from .models import CollectionList

# Intercom Python SDK
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class HelpCenterAPI(APIBase):  # type: ignore
    URI = "/help_center/"

    @returns(CollectionSchema(many=False))  # type: ignore
    @get("collections/{collection_id}")
    def get_collection_by_id(self, collection_id: Union[str, int]):
        """ Get a Collection by ID.

        Args:
            collection_id (Union[str, int]): The ID of the Collection.

        Returns:
            Collection: The Collection with the given ID.
        """

    @returns(CollectionListSchema(many=False))  # type: ignore
    @get("collections")
    def __list_all_collections(self, page: Query('page') = 1, per_page: Query('per_page') = 50):  # type: ignore
        """ List all Collections.

        Returns:
            CollectionList: A list of all Collections.
        """

    def list_all_collections(self):
        """ List all Collections.

        Returns:
            CollectionList: A list of  all Collections.
        """
        resp: 'CollectionList' = self.__list_all_collections()  # type: ignore
        page = resp.pages['page']
        total = resp.pages['total_pages']

        if page == total:
            return resp
        
        for page in range(page + 1, total + 1):
            resp.collections.extend(self.__list_all_collections(page=page).collections)
            resp.pages['page'] = page

        return resp

    @returns(CollectionSchema(many=False))  # type: ignore
    @json()
    @put("collections/{collection_id}")
    def update_collection_by_id(self, collection_id: Union[str, int], data: Body(type=CollectionSchema)):  # type: ignore
        """ Update a Collection.

        Args:
            collection_id (Union[str, int]): The ID of the Collection.
            data (CollectionSchema): The data to update the Collection with.

        Returns:
            Collection: The updated Collection.
        """
    
    @returns(CollectionSchema(many=False))  # type: ignore
    @json()
    @post("collections")
    def create_collection(self, data: Body(type=CollectionSchema)):  # type: ignore
        """ Create a Collection.

        Args:
            data (CollectionSchema): The data to create the Collection with.

        Returns:
            Collection: The created Collection.
        """

    @delete("collections/{collection_id}")
    def delete_collection_by_id(self, collection_id: Union[str, int]):
        """ Delete a Collection by ID.

        Args:
            collection_id (Union[str, int]): The ID of the Collection.
        """

    # Sections

    @returns(SectionSchema(many=False))  # type: ignore
    @get("sections/{section_id}")
    def get_section_by_id(self, section_id: Union[str, int]):
        """ Get a Section by ID.

        Args:
            section_id (Union[str, int]): The ID of the Section.

        Returns:
            Section: The Section with the given ID.
        """

    @returns(SectionListSchema(many=False))  # type: ignore
    @get("sections")
    def list_all_sections(self):
        """ List all Sections.

        Returns:
            SectionList: A list of all Sections.
        """
