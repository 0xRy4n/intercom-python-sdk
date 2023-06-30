from typing import Optional as Opt
from uplink.auth import BearerToken
from warnings import warn

from .apis import tags_to_api_dict
from .core.configuration import Configuration

class Intercom:
    def __init__(self, api_key: Opt[str] = None, config: Opt[Configuration] = None):
        """
        Initializes a new instance of the Intercom class. Requires either an API key or a Configuration object.

        Args:
            api_key: The API key to use for authentication. If not provided, will use the API key from the Configuration object.
            config: The configuration settings for the API. If not provided, will build one using the provided API key.
        """
        if not api_key and not config:
            raise ValueError("Must provide either an API key or a Configuration object.")
        
        if api_key and config: # type: ignore
            warn("Both an API key and a Configuration object were provided. Using the Configuration object.")
        
        if not config:
            auth = BearerToken(api_key)
            config = Configuration(auth=auth)

        
        for tag, api_class in tags_to_api_dict.items():
            setattr(self, tag, api_class(config))
