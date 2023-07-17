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
from typing import Dict

from osdu_client import OSDUAPI
from osdu_client.auth import AuthBackendInterface


class AuthBackend(AuthBackendInterface):
    def __init__(self, headers, base_url) -> None:
        self._headers = headers
        self._base_url = base_url

    def get_headers(self) -> Dict:
        return self._headers

    def get_base_url(self) -> str:
        return self._osdu_base_url

    def get_sd_connection_params(self, log_level: int = None) -> Dict:
        return {}


auth_backend = AuthBackend(
    headers={"Authorization": "Bearer XYZ"},
    base_url="https://exmaple.com"
)

storage_client = OSDUAPI.client('storage', auth_backend=auth_backend)
response = storage_client.get_record_versions(id="123")

```