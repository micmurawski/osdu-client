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
    def client(service_name, auth_backend: AuthBackendInterface = None):
        return get_service_client(service_name)(auth_backend)
