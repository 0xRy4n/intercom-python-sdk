""" API Base Module
`api_base.py`

Contains the base class for all API classes in the Intercom Python SDK.
Extends with 

"""
from typing import Optional as Opt, Union
from uplink.builder import Builder
from uplink import Consumer, hooks as hooks_, session
from validator_collection import checkers
from warnings import warn

from .configuration import Configuration

class APIBase(Consumer):
    def __init__(self, config: Configuration, **kwargs):
        """
        Initializes a new instance of the APIBase class.
        Overrides the Consumer class from the Uplink library to 
        configure the Consumer instance using a Configuration object.

        Args:
            config: The configuration settings for the API.
        """
        super().__init__(
            base_url=config.base_url,
            converters=config.converters,
            hooks=config.hooks,
            auth=config.auth,
            client=config.session
        )

    def set_api_client(self):
        """
        A wrapper that sets the API client attribute for a returned model object.
        """
        def wrap(*args, **kwargs):
            model = args[0]
            model.api_client = self
            return model
        
        return wrap
    

