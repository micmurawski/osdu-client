import os
from abc import ABCMeta
from typing import Any, AnyStr

import requests

from ..auth import AuthBackendInterface


class BaseOSDUAPIClient(metaclass=ABCMeta):

    __slots__ = ("service_path")

    def __init__(self, url: AnyStr, osdu_auth_backend: AuthBackendInterface, http_backend: Any = None):
        self.url = url
        self.osdu_auth_backend = osdu_auth_backend
        if http_backend is None:
            self.http_backend = requests

    def __enter__(self):
        yield self

    def __aenter__(self):
        yield self

    @property
    def base_path(self):
        return os.path.join(
            self.url,
            self.service_path,
        )
