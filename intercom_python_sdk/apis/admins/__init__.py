""" 
# Intercom Admins API

Implements the Intercom Admins API [1].

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/admins
- [2] https://developers.intercom.com/intercom-api-reference/reference/the-admin-model

## Example Usage

```python
from intercom_python_sdk import Intercom

intercom = Intercom('my_api_key')

admins_list = intercom.admins.list_all() # Returns an AdminsList object

for admin in admins_list: # We can iterate over the AdminsList object like a list
    print(admin.name) # We can access the attributes of each Admin object, as is defined in `apis/admins/models.py` and the Intercom Admins Model [2].

cur_admin = intercom.admins.me() # Returns the current Admin
cur_admin.set_away() # We can take API actions on the Admin object, as is defined in `apis/admins/models.py`.
```

"""

from . import api
from . import models
from . import schemas