from abc import ABCMeta

from osdu_client.auth import AuthInterface


class BaseOSDUAPIClient(metaclass=ABCMeta):
    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend
