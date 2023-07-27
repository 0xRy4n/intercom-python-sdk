"""
# Tags To API

`apis/tags_to_api.py`

This module contains the TagsToAPI class which is a dictionary that maps
tags (API names) to their respective API classes. It's used to control the name used to 
access the API classes from the Intercom object, as well as which API classes
are enabled via the Intercom object.

## Example Usage

To enable a new API, first import it like so:

```python
from .my_new_api.api import MyNewAPI
```

Then add it to the `tags_to_api_dict` like so:
```python
tags_to_api_dict["my_new_api"] = MyNewAPI
```

You can then access the API via the Intercom object like so:
```python
intercom = Intercom('my_api_key')
intercom.my_new_api
```
"""
# External
from uplink.builder import Consumer, ConsumerMeta

# From Current API
from .admins.api import AdminsAPI
from .data_attributes.api import DataAttributesAPI
from .articles.api import ArticlesAPI
from .data_events.api import DataEventsAPI
from .data_export.api import DataExportAPI

# From Current Package
from ..core.api_base import APIBase

class TagsToAPI(dict):
    """ 
    A dictionary that maps tags (API names) to their respective API classes. 
    
    Only API-client type classes can be mapped to tags, as per the `allowed_types` attribute.
    """
    allowed_types = (APIBase, Consumer, ConsumerMeta)

    # Validation of assigned values to ensure only API classes are mapped.
    def __setitem__(self, key, value):
        if not isinstance(value, self.allowed_types):
            raise TypeError(f"Invalid type. Value must be one of types {TagsToAPI.allowed_types}. Got {type(value)}.")
        super().__setitem__(key, value)


tags_to_api_dict = TagsToAPI()
tags_to_api_dict["admins"] = AdminsAPI
tags_to_api_dict["articles"] = ArticlesAPI
tags_to_api_dict["data_attributes"] = DataAttributesAPI
tags_to_api_dict["data_events"] = DataEventsAPI
tags_to_api_dict["data_export"] = DataExportAPI