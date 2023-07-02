"""
====================
TagsToAPI
====================
`apis/tags_to_api.py`

This module contains the TagsToAPI class which is a dictionary that maps
tags (API names) to their respective API classes.
"""
# External
from uplink.builder import Consumer, ConsumerMeta

# From Current API
from .admins.api import AdminsAPI
from .data_attributes.api import DataAttributesAPI


# From Current Package
from ..core.api_base import APIBase

class TagsToAPI(dict):
    """ A dictionary that maps tags (API names) to their respective API classes. """
    allowed_types = (APIBase, Consumer, ConsumerMeta) 

    # Validation of assigned values to ensure only API classes are mapped.
    def __setitem__(self, key, value):
        if not isinstance(value, self.allowed_types):
            raise TypeError(f"Invalid type. Value must be one of types {TagsToAPI.allowed_types}. Got {type(value)}.")
        super().__setitem__(key, value)


tags_to_api_dict = TagsToAPI()
tags_to_api_dict["admins"] = AdminsAPI
tags_to_api_dict["data_attributes"] = DataAttributesAPI