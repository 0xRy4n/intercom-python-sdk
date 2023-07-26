"""
# API Base Module

`core/api_base.py`

Contains the core base classes and methodsfor all API classes in the Intercom Python SDK.
"""
# Third-Party Imports
from uplink import (
    Consumer,
    json
)

# Local Imports
from .configuration import Configuration
from .model_base import ModelBase


class APIProxyInterface:
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
        """
        Set the API object for the API we are proxying

        Args:
            api_class: The API class to proxy.
            config: The configuration settings for the API.
        """
        self.api_object = api_class(config)

    def __dir__(self):
        """ Proxy the dir() method to the API object. """
        return dir(self.api_object)

    def __getattribute__(self, item):
        """ Proxy all attribute access to the API object (except for api_object itself). """
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
        """ Proxy all attribute setting to the API object (except for api_object itself). """
        if item == 'api_object':
            return object.__setattr__(self, item, value)
        api_object = object.__getattribute__(self, 'api_object')
        setattr(api_object, item, value)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Direct method calls on APIProxyInterface are not supported. Access methods through api_object.")

    def __repr__(self):
        return repr(f"<{object.__getattribute__(self, '__class__').__name__}> - {self.api_object}")

    def _wrap_callable(self, method):
        """
        Wraps callable method to intercept the result.
        If the result is a model object, inject the API client into the model object.
        """
        def wrapped(*args, **kwargs):
            result = method(*args, **kwargs)
            inject_into_instances = object.__getattribute__(self, '_inject_into_instances')
            inject_into_instances(result, ModelBase, 'api_client', self.api_object)
            return result
        return wrapped

    def _inject_into_instances(self, obj, cls, attribute_name, attribute_value, visited=None):
        """
        Allows us to inject an attribute into all instances of a class, contained
        within an arbitrary data structure of unknown depth.

        This is useful for injecting the API client instance into Model Objects
        that may be contained within some nested data structure (like a list of objects).
        """
        if visited is None:
            visited = set()

        if id(obj) in visited:
            return

        visited.add(id(obj))

        inject_into_instances_method = object.__getattribute__(self, '_inject_into_instances')
        inject = lambda obj: inject_into_instances_method(obj, cls, attribute_name, attribute_value, visited) # noqa

        if isinstance(obj, cls):
            obj.__setattr__(attribute_name, attribute_value)

        if isinstance(obj, dict):
            for value in obj.values():
                inject(value)

        elif isinstance(obj, (list, set, tuple)):
            for item in obj:
                inject(item)

        elif hasattr(obj, '__dict__'):
            for attr in vars(obj).values():
                inject(attr)


@json
class APIBase(Consumer):
    """
    The base class for all API classes in the Intercom Python SDK.
    """
    URI = ""

    def __init__(self, config: Configuration, **kwargs):
        """
        Initializes a new instance of the APIBase class.
        Overrides the Consumer class from the Uplink library to
        configure the Consumer instance using a Configuration object.

        Args:
            config: The configuration settings for the API.
        """
        self.config = config

        self.base_url = config.base_url + self.URI

        print(f"[*] Loaded API Endpoint: {self.base_url}")

        super().__init__(
            base_url=self.base_url,
            converters=config.converters,
            hooks=config.hooks,
            auth=config.auth,
            client=config.session
        )

    def make_subapi(self, api_tag, api_cls, api_config):
        # api_tag is the name of the subapi
        # api_cls class
        # api_config is the config object

        if not hasattr(self, api_tag):
            # If the subapi has not been created yet, create it
            setattr(self, api_tag, create_api_client(api_cls, api_config))

        else:
            # If the subapi has already been created, return it
            return getattr(self, api_tag)


# Functions
def create_api_client(api_class: 'APIBase', config: Configuration) -> APIProxyInterface:
    """
    Creates a proxy interface for an API client for the provided API class.

    Args:
        api_class: The API class to create a client for.
        config: The configuration settings for the API.

    Returns:
        An proxy interface to the instance of the API class with an API client attached to each model object.
    """
    return APIProxyInterface(api_class, config)
