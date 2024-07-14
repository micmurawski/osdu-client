from __future__ import annotations

from abc import ABCMeta, abstractmethod


class AuthBackendInterface(metaclass=ABCMeta):

    def get_headers(self) -> dict:
        headers = {}
        headers.update(self.authorization_header)
        headers.update(
            {
                "tenant": self.default_tenant,
                "data-partition-id": self.default_data_partition_id
            }
        )
        return headers

    @property
    @abstractmethod
    def default_tenant(self) -> str:
        pass

    @property
    @abstractmethod
    def default_data_partition_id(self) -> str:
        pass

    @property
    @abstractmethod
    def authorization_header(self) -> dict:
        pass

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @abstractmethod
    def get_sd_connection_params(self, log_level: int = None) -> dict:
        pass
