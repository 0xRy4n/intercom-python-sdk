""" 
# Configuration Module

`core/configuration.py`

This module contains the Configuration class for the Intercom Python SDK.
It is used to configure settings for individual API instances, which themselves
are instances of the `Consumer` class from the Uplink library.
"""
# Built-ins
from typing import (
    Optional as Opt,
    Union,
    Tuple,
    Dict
)

from warnings import warn

# External
import requests
from uplink.converters import ConverterFactory
from uplink.hooks import TransactionHook
from validator_collection import checkers


class Configuration:
    """
    A configuration class used instantiating individual API clients.
    
    Attributes:
        MIN_API_VERSION (float): The minimum API version this SDK has been tested for. 
    """

    MIN_API_VERSION = 2.9  # Minimum API Version Tested For

    def __init__(
        self,
        auth,
        base_url: str = "https://api.intercom.io",
        api_version: Opt[Union[str, int]] = None,
        converters: Union[Tuple[ConverterFactory], Tuple[()]] = (), # Uplink converters
        hooks: Union[Tuple[TransactionHook], Tuple[()]] = (), # Uplink hooks
        proxy: Opt[Dict] = None
    ):
        """
        Initializes a new instance of the Configuration class.

        Args:
            auth: The authentication instance- see the Authentication classes in the Uplink library.
            base_url: The base URL of the API. Default is "https://api.intercom.io".
            api_version: The version of the API. Default is None (will use the version specified in your Intercom instance.)
            proxy: Optional proxy configuration for debugging. Treat like a requests.Session() proxy argument.
            
        Raises:
            ValueError: If the provided api_version is not valid.
        """
        self._auth = auth
        self._base_url = base_url
        self._api_version = self.__validate_version(api_version)
        self._headers = {}
        self._session = requests.Session()

        # For flexibility with uplink
        self._converters = converters
        self._hooks = hooks

        if self._api_version:
            self._headers["Intercom-Version"] = self._api_version

        self._headers["Accept"] = "application/json"
        self._headers["Content-Type"] = "application/json"
        self._session.headers.update(self._headers)

        if proxy:
            self._session.proxies = proxy
            self._session.verify = False


    def __validate_version(self, api_version: Union[str, int, None]) -> Union[str, None]:
        """
        Validates the API version.

        Args:
            api_version: The version of the API.

        Returns:
            The validated API version.

        Raises:
            ValueError: If the provided api_version is not valid.
        """
        if not api_version:
            return None

        is_float = checkers.is_float(api_version)

        if not is_float and str(api_version).upper() != "UNSTABLE":
            raise ValueError("Could not validate API version. Please specify a floatable string such as '2.9' or 'unstable'.")

        if is_float and int(api_version) < self.MIN_API_VERSION:
            warn(f"API version {api_version} is below the minimum API version of this client ({self.MIN_API_VERSION}). Some features may not work.")

        return str(api_version)

    # Properties

    @property
    def auth(self):
        """The authentication instance. See the Authentication classes in the Uplink library. """
        return self._auth
    
    @property
    def base_url(self) -> str:
        """The base URL of the API. Example: 'https://api.intercom.io'"""
        return self._base_url
    
    @property
    def api_version(self) -> Union[str, None]:
        """The version of the API."""
        return self._api_version
    
    @property
    def headers(self) -> dict:
        """The headers to be used in the API."""
        return self._headers
    
    @property
    def session(self) -> requests.Session:
        """The session to be used in the API."""
        return self._session
    
    @property
    def converters(self) -> Union[Tuple[ConverterFactory], Tuple[()]]:
        """The converters to be used in the API."""
        return self._converters
    
    @property
    def hooks(self) -> Union[Tuple[TransactionHook], Tuple[()]]:
        """The hooks to be used in the API."""
        return self._hooks
    
    @base_url.setter
    def base_url(self, value):
        self._base_url = value
    