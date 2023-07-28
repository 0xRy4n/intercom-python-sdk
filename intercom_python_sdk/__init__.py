# flake8: noqa
"""
# Intercom Python SDK
The unofficial Python SDK for the Intercom API, _because we can't all be Ruby or Go evagelists._

## Quick Start

```python

from intercom_python_sdk import Intercom

intercom = Intercom('my_api_key')

intercom.admins.me() # Returns the current Admin
intercom.data_attributes.list_all() # Returns a DataAttributesList object
intercom.articles.list_all() # Returns an ArticlesList object
```

## Using Schemas
You can import any available schema from the `schemas` module like so:

```python
from intercom_python_sdk.schemas import AdminSchema
```

Generally speaking, you don't need to use schemas directly unless you are POSTing a new object to the API, such as to create a new Data Attribute. For example:

```python
from intercom_python_sdk.schemas import DataAttributeSchema

data = {
    'name': 'Example',
    'model': 'company', # Can be 'contact', 'company', or 'conversation`
    'data_type': 'string', # Can be `string`, `integer`, `float`, `boolean`, `date`, `datetime`
    'description': 'Example Description',
    'options': ['Option 1', 'Option 2'], # If your attribute has options, define theme (string only).
}

attribute_data = DataAttributeSchema().dump(data) # You could also do .validate(data) here
new_attribute = intercom.data_attributes.create(new_attribute) # Returns the new DataAttribute object.
```

Here, you can dump a standard dictionary of data into a Schema object, which can then be sent off to the API.

## Using Models
You can import any available model from the `models` module like so:

```python
from intercom_python_sdk.models import Admin
```

There are very few circumstances where you would need to access a Model class directly in this way. Instead, model _instances_ are always returned from API calls. For example, `intercom.admins.me()` returns an `Admin` object.

These objects contain all the properties defined for their model in the Intercom API Reference. They may also contain methods which allow you take actions on the object, or access related objects. For example, `Admin` objects have a `set_away()` method which allows you to set the Admin's status to away.
"""

from .intercom import Intercom
from .core.configuration import Configuration
from .core.api_base import create_api_client
from .apis.tags_to_api import tags_to_api_dict as API_TAGS
