from .dataset_api import DatasetAPIClient
from .entitlements_api import EntitlementsAPIClient
from .schema_api import SchemaAPIClient
from .sddms_api import SDDMSAPIClient
from .search_api import SearchAPIClient
from .storage_api import StorageAPIClient

CLIENTS = {
    "dataset": DatasetAPIClient,
    "entitlements": EntitlementsAPIClient,
    "schema": SchemaAPIClient,
    "sddms": SDDMSAPIClient,
    "search": SearchAPIClient,
    "storage": StorageAPIClient,
}


def get_service_client(name):
    if name not in CLIENTS:
        raise Exception(f"Service {name} not recognized. Choose one from available {', '.join(CLIENTS.keys())}")
    return CLIENTS[name]
