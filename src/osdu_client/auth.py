from abc import ABCMeta, abstractmethod, abstractproperty
from typing import AnyStr, Dict


class AuthInterface(metaclass=ABCMeta):

    @abstractproperty
    def headers(self) -> Dict:
        pass

    @abstractproperty
    def osdu_base_url(self) -> AnyStr:
        pass

    @abstractmethod
    def get_sd_connection_string(self, log_level: int = None) -> AnyStr:
        pass
