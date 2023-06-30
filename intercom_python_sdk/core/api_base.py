""" API Base Module
`api_base.py`

Contains the core base classes and methodsfor all API classes in the Intercom Python SDK.
"""
import functools
from typing import Optional as Opt, Union
from uplink.builder import Builder
from uplink import Consumer, hooks as hooks_, session, returns
from validator_collection import checkers
from warnings import warn

from .configuration import Configuration
from .model_base import ModelBase

    
class APIBase(Consumer):
    def __init__(self, config: Configuration, **kwargs):
        """
        Initializes a new instance of the APIBase class.
        Overrides the Consumer class from the Uplink library to 
        configure the Consumer instance using a Configuration object.

        Args:
            config: The configuration settings for the API.
        """
        print(config)

        super().__init__(
            base_url=config.base_url,
            converters=config.converters,
            hooks=config.hooks,
            auth=config.auth,
            client=config.session
        )

class APIProxyClass:
    """
    A proxy class that functions as an interface to API client / consumer objects.
    This allows for interception of API calls and modification of the results.
    In practice, this is how the model instance objects are captured and injected
    with the API client object.

    Given the nature of the Uplink library, it is not possible to inject a reference
    to the API client object into the model instance objects from within the API client
    itself.

    Args:
        api_class: The API class to proxy.
        config: The configuration settings for the API.
    
    Attributes:
        All attributes and methods are passed through to the API object. It will be as if
        you are accessing the API object directly.

    Returns:
        A proxy class that functions as an interface to API client / consumer objects.
    """
    def __init__(self, api_class, config):
        self.api_object = api_class(config)
    
    def __dir__(self):
        return dir(self.api_object)
    
    def __getattribute__(self, item):
        api_object = object.__getattribute__(self, 'api_object')
        if item == 'api_object':
            return api_object
        attr = getattr(api_object, item)
        if callable(attr):
            # This is where we wrap the callable to intercept the result
            return object.__getattribute__(self, '_wrap_callable')(attr)
        else:
            return attr
        
    def __setattr__(self, item, value):
        if item == 'api_object':
            return object.__setattr__(self, item, value)
        api_object = object.__getattribute__(self, 'api_object')
        setattr(api_object, item, value)
    
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Direct method calls on ProxyClass are not supported. Access methods through api_object.")

    def __repr__(self):
        return repr(f"<{object.__getattribute__(self, '__class__').__name}> - {self.api_object}")
    
    def _wrap_callable(self, method):
        def wrapped(*args, **kwargs):
            result = method(*args, **kwargs)
            if isinstance(result, ModelBase):
                # Inject the API client into the model object
                result.api_client = self.api_object
            return result
        return wrapped
    

def create_api_client(api_class: APIBase, config: Configuration):
    """
    Creates a proxy interface for an API client for the provided API class.

    Args:
        api_class: The API class to create a client for.
        config: The configuration settings for the API.

    Returns:
        An proxy interface to the instance of the API class with an API client attached to each model object.
    """
    return APIProxyClass(api_class, config)