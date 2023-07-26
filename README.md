# Intercom Python SDK

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37d20c511a7d4c8590099f9ddcaf4485)](https://app.codacy.com/gh/0xRy4n/intercom-python-sdk?utm_source=github.com&utm_medium=referral&utm_content=0xRy4n/intercom-python-sdk&utm_campaign=Badge_Grade)

### Disclaimer

This is an unofficial Python SDK for interacting with the Intercom API as defined in the [Intercom API Reference](https://developers.intercom.com/intercom-api-reference/reference). This project is in no way associated with Intercom and is provided as-is without warranty. See the `LICENSE` file for more information.

### Docs
You can read the docs at https://0xry4n.github.io/intercom-python-sdk/

## Usage

#### Basic

All functionality to the SDK is provided through a single `Intercom` class which can be imported as follows:

```python
from intercom_python_sdk import Intercom
```

The most basic way to authenticate with the SDK is to provide an API Key (Private App Key) as follows:

```python
import intercom_python_sdk

intercom = intercom_python_sdk.Intercom(api_key='my_api_key')
```

You can then access all sub-APIs through this object, like so:

```python

cur_admin = intercom.admins.me()
all_admins = intercom.admins.list_all()

all_data_events = intercom.data_events.list_all()
```


#### Advanced

The `Intercom` class can support being passed a `Configuration` object. This class itself will expect you to manually build your Authentication object from the `Uplink` library, and gives you access to some additional settings.

```python
from uplink.auth import BearerToken
from intercom_python_sdk import Intercom, Configuration

auth = BearerToken('my_api_key')
config = Configuration(
    auth=auth, 
    base_url='https://api.intercom.io',
    api_version="2.9",
    proxy={'https': 'https://127.0.0.1:8080'} # Optional Proxy for Debug-- see requests.Session proxy documentation
)

intercom = Intercom(config=config)
```

For developers, additional parameters from the underlying library (`Uplink`) are exposed here as well. See the docstrings for more information.

##### Using Individual Sub-APIs

You also have the ability to create individual clients for a specific API instead of using the Intercom class. This may be useful if you have different credentials for different APIs, or if you want to use the same credentials but different configurations.

```python

from intercom_python_sdk import Admins, Configuration, create_api_client, API_TAGS

auth = BearerToken('my_api_key')
config = Configuration(auth=auth)
admins = create_api_client(API_TAGS["admin"], config)
```

