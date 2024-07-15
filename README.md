# Introduction

[![pypi](https://img.shields.io/pypi/v/osdu-client.svg)](https://pypi.org/project/osdu-client/)

`osdu-client` is a python library implementing a simple OSDU client with an abstracted-out authorization backend.

# Instalation
```
pip install osdu-client
```

# Example
OSDU API client can be adjusted to specific OSDU deployment by defining auth backend according to `AuthBackendInterface` methods.



```python
from osdu_client import OSDUAPI
from osdu_client.auth import AuthBackendInterface


class AuthSession(AuthBackendInterface):
    base_url = "https://base.url"
    default_data_partition_id = "osdu"
    default_tenant = "osdu"
    authorization_header = {"Authorization": "Bearer access_token"}

    def get_sd_connection_params(self):
        return {}


auth_backend = AuthSession(
    headers={"Authorization": "Bearer XYZ"},
    base_url="https://exmaple.com"
)

storage_client = OSDUAPI.client('storage', auth_backend=auth_backend)
response = storage_client.get_record_versions(id="123")

```