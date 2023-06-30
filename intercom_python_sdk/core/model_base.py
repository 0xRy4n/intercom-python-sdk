"""
Extensible models applicable to all APIS.
"""

from pprint import pformat

class ModelBase:
    """
    Base model for all API models.

    Raises:
        NotImplementedError: When setting a property with no setter.
    """
    def __setattr__(self, name, value):
        prop = getattr(self, name, None)
        if isinstance(prop, property) and not prop.fset:
            raise NotImplementedError(f"Setting {name} property is either not supported by the API or not implemented in the SDK.")
        super().__setattr__(name, value)

    def __repr__(self):
        properties = {attr: getattr(self, attr) for attr in dir(self) if isinstance(getattr(type(self), attr, None), property)}
        return f"{self.__class__.__name__}(\n{pformat(properties)}\n)"
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    @property
    def api_client(self):
        return getattr(self, "_api_client", None)
    
    @api_client.setter
    def api_client(self, api_client):
        self._api_client = api_client
    
    
