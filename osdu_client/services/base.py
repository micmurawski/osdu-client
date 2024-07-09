from abc import ABCMeta

from osdu_client.auth import AuthBackendInterface


class BaseOSDUAPIClient(metaclass=ABCMeta):
    def __init__(self, osdu_auth_backend: AuthBackendInterface, base_url: str):
        self.osdu_auth_backend = osdu_auth_backend
        self.base_url = base_url
