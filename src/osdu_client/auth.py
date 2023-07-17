from abc import ABCMeta, abstractmethod
from typing import Dict


class AuthBackendInterface(metaclass=ABCMeta):

    @property
    def headers(self) -> Dict:
        return self.get_headers()

    @property
    def base_url(self) -> str:
        return self.get_base_url()

    @abstractmethod
    def get_headers(self) -> Dict:
        pass

    @abstractmethod
    def get_base_url(self) -> str:
        pass

    @abstractmethod
    def get_sd_connection_params(self, log_level: int = None) -> Dict:
        pass
