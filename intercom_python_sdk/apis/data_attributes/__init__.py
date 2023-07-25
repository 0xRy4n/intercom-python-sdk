""" 
# Intercom Data Attributes API

Implements the Intercom Data Attributes API [1].

## Example Usage

```python
from intercom_python_sdk import Intercom

intercom = Intercom('my_api_key')

attributes = intercom.data_attributes.list_all() # Returns a DataAttributesList object

for attribute in attributes: # We can iterate over the DataAttributesList object like a list
    print(attribute.name) # We can access the attributes of each DataAttribute object, as is defined in `apis/data_attributes/models.py` and the Intercom Data Attribute Model [2].

first_attribute = attributes[0] # We can also index into the DataAttributesList object like a list.
```

### Creating a Data Attribute

```python
data = {
    'name': 'Example',
    'model': 'company', # Can be 'contact', 'company', or 'conversation`
    'data_type': 'string', # Can be `string`, `integer`, `float`, `boolean`, `date`, `datetime`
    'description': 'Example Description',
    'options': ['Option 1', 'Option 2'], # If your attribute has options, define theme (string only).
}

from intercom_python_sdk.schemas import DataAttributeSchema

new_attribute = DataAttributeSchema().dump(data)

new_attribute = intercom.data_attributes.create(new_attribute) # Returns the new DataAttribute object.
```

### Updating a Data Attribute
If an attribute is updatable, you can modify a DataAttribute object and call `update()` on it to update the attribute.

```python
new_attribute.description = "My New Description"
new_attribute.update()
```
"""

from . import api
from . import models
from . import schemas