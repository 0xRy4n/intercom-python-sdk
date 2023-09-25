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
from typing import Union

# External
from uplink import (
    get,
    returns,
    response_handler,
)

# From Current API
from .schemas import (
    CollectionSchema,
    CollectionListSchema,
    SectionSchema,
    SectionListSchema,
)


# From Current Package
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
    def list_all_collections(self):
        """ List all Collections.

        Returns:
            CollectionList: A list of all Collections.
        """

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
