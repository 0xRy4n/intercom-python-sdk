""" API Base Module
`api_base.py`

Contains the base class for all API classes in the Intercom Python SDK.
Extends with 

"""
from typing import Optional as Opt, Union
from uplink import Consumer
from uplink.session import Session
from validator_collection import checkers
from warnings import warn

from .configuration import Configuration

class APIBase(Consumer):
    def __init__(self, config: Configuration):
        """
        Initializes a new instance of the APIBase class.

        Args:
            config: The configuration settings for the API.
        """

        super().__init__(
            
        )

