import os
from typing import Any, AnyStr

from .auth import AuthBackendInterface
from .exceptions import OSDUClientError
from .services.dataset_api import DatasetAPIClient
from .services.entitlements_api import EntitlementsAPIClient
from .services.legal_api import LegalAPIClient
from .services.schema_api import SchemaAPIClient
from .services.sdms_api import SDMSAPIClient
from .services.search_api import SearchAPIClient
from .services.storage_api import StorageAPIClient

CLIENTS = {
    "dataset": DatasetAPIClient,
    "entitlements": EntitlementsAPIClient,
    "schema": SchemaAPIClient,
    "sdms": SDMSAPIClient,
    "search": SearchAPIClient,
    "storage": StorageAPIClient,
    "legal": LegalAPIClient,
}


def get_service_client(name):
    if name not in CLIENTS:
        raise OSDUClientError(
            f"Service {name} not recognized. Choose one from available {', '.join(CLIENTS.keys())}"
        )
    return CLIENTS[name]


class OSDUAPI:
    @staticmethod
    def client(service_name, url: AnyStr = None, auth_backend: AuthBackendInterface = None, http_backend: Any = None):
        url = url or os.environ.get("OSDU_URL")
        if url is None:
            raise ValueError("OSDU url is not provided. Set url attribute or set environment variable OSDU_URL.")
        return get_service_client(service_name)(url, auth_backend, http_backend)
