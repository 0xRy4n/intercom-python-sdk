"""
# Intercom Client

`intercom.py`

This module contains the Intercom class, which is used to interact with the Intercom API.
"""
# Built-ins
from typing import Optional as Opt
from warnings import warn

# External
from uplink.auth import BearerToken

# Current package 
from .apis import tags_to_api_dict
from .core.configuration import Configuration
from .core.api_base import create_api_client


class Intercom:
    def __init__(self, api_key: Opt[str] = None, config: Opt[Configuration] = None, debug=False):
        """
        Initializes a new instance of the Intercom class. Requires either an API key or a Configuration object.

        Args:
            api_key (str): The API key to use for authentication. If not provided, will use the API key from the Configuration object.
            config (Configuration): The configuration settings for the API. If not provided, will build one using the provided API key.
            debug (dict): Enables debugging features. 
                - Default HTTP proxy configuration enabled. Use custom config for more control.
        """
        if not api_key and not config:
            raise ValueError("Must provide either an API key or a Configuration object.")
        
        if api_key and config:  # type: ignore
            warn("Both an API key and a Configuration object were provided. Using the Configuration object.")
        
        if not config:
            auth = BearerToken(api_key)
            if debug:
                proxy = {
                    "http": "http://localhost:8080",
                    "https": "http://localhost:8080",
                }
            else:
                proxy = None

            config = Configuration(auth=auth, proxy=proxy)
        
        for tag, api_class in tags_to_api_dict.items():
            setattr(self, tag, create_api_client(api_class, config))
