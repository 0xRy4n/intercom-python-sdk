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
        self.config = config

        # --- Ripped from uplink.Consumer and modified for Configuration object. ---
        # https://uplink.readthedocs.io/en/stable/_modules/uplink/builder.html#Consumer
        if isinstance(self.config.hooks, hooks_.TransactionHook):
            hooks = (self.config.hooks,)

        builder = Builder()
        builder.base_url = self.config.base_url
        builder.converters = self.config.converters
        builder.add_hook(*self.config.hooks)
        builder.auth = self.config.auth
        builder.client = self.config.session

        self.__session = session.Session(builder)
        self.__client = builder.client
        # --- End rip ---

