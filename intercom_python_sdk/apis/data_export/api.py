""" 
# Data Export API

`apis/data_export/api.py`

This module contains the Data Export API class, which defines a client for the Data Export API.
It is used to interact with the Intercom Data Events API [1] as defined in the Intercom API Reference.

----
- [1] https://developers.intercom.com/intercom-api-reference/reference/create-data-export
"""

# Built-ins
from typing import Union
from datetime import datetime
from validator_collection import validators

# External
import marshmallow
from uplink import (
    get, put, post, 
    returns, args, headers,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query
)

# From Current API
from . import schemas as dexport_schemas
from . import models as dexport_models


# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error


@response_handler(catch_api_error)
class DataExportAPI(APIBase):
    URI = "/export/"
    
    @json
    @returns(dexport_schemas.DataExportJobSchema()) # type: ignore
    @post("content/data")
    def __create_data_export(self, payload: Body(type=dict)): # type: ignore
        """ Create a new data export. """

    def export(self, created_before: Union[int, datetime], created_after: Union[int, datetime]):
        """ Create a new data export. 
        
        Params:
            created_before (Union[int, datetime]): Datetime or unix epoch to define the upper bound of the export.
            created_after (Union[int, datetime]): Datetime or unix epoch to define the lower bound of the export.

        Returns:
            DataExportJob: The data export job.
        """

        if isinstance(created_before, datetime):
            created_before = int(created_before.timestamp())
        else:
            created_before = validators.integer(created_before, minimum=0)
        
        if isinstance(created_after, datetime):
            created_after = int(created_after.timestamp())
        else:
            created_after = validators.integer(created_after, minimum=0)


        payload = {
            "created_before": created_before,
            "created_after": created_after
        }

        return self.__create_data_export(payload=payload)
    

    @headers({"Accept": "application/octet-stream"})
    @get("/download/content/data/{job_identifier}") # Leading slash as we aren't using the base URI
    def download(self, job_identifier: Path("job_identifier", str)): # type: ignore
        """ Download a data export. """


    

    



    

