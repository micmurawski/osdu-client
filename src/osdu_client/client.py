from osdu_client.exceptions import OSDUClientError
from osdu_client.services.dataset_api import DatasetAPIClient
from osdu_client.services.entitlements_api import EntitlementsAPIClient
from osdu_client.services.schema_api import SchemaAPIClient
from osdu_client.services.sdms_api import SDMSAPIClient
from osdu_client.services.search_api import SearchAPIClient
from osdu_client.services.storage_api import StorageAPIClient

from .auth import AuthBackendInterface

CLIENTS = {
    "dataset": DatasetAPIClient,
    "entitlements": EntitlementsAPIClient,
    "schema": SchemaAPIClient,
    "sdms": SDMSAPIClient,
    "search": SearchAPIClient,
    "storage": StorageAPIClient,
}


def get_service_client(name):
    if name not in CLIENTS:
        raise OSDUClientError(f"Service {name} not recognized. Choose one from available {', '.join(CLIENTS.keys())}")
    return CLIENTS[name]


class OSDUAPI:
    @staticmethod
    def client(service_name, auth_backend: AuthBackendInterface = None):
        return get_service_client(service_name)(auth_backend)
