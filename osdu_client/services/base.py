from abc import ABCMeta

from osdu_client.auth import AuthBackendInterface


class OSDUAPIClient(metaclass=ABCMeta):
    def __init__(self, auth_backend: AuthBackendInterface, base_url: str | None = None, validation: bool = True):
        self.auth = auth_backend
        self.base_url = base_url or auth_backend.base_url
        self.validation = validation
