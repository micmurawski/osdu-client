from abc import ABCMeta, abstractclassmethod

from osdu_client.auth import AuthInterface


class BaseOSDUAPIClient(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, osdu_auth_backend: AuthInterface):
        pass
