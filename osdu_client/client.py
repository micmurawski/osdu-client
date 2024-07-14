from __future__ import annotations
from osdu_client.auth import AuthBackendInterface
from osdu_client.exceptions import OSDUClientError
from osdu_client.services.base import OSDUAPIClient
from importlib import import_module

DMS_NAMES = {
    "sdms": "SDMS",
    "pws": "PWS",
    "rafs": "RAFS",
    "welldelivery": "WellDelivery"
}


def get_service_client(name: str, version: str | None = None) -> type[OSDUAPIClient]:
    service_name = DMS_NAMES.get(name, name.capitalize())

    try:
        module = import_module(
            f"osdu_client.services.{name}"
        )
        available_versions = getattr(module, "VERSIONS", {})

        if available_versions and version is None:
            version = getattr(module, "DEFAULT_VERSION")
            client_class = available_versions[version]
        else:
            client_class = getattr(module, f"{service_name}Client")
    except KeyError as e:
        raise OSDUClientError(
            f"Version {version} of a client {name} does not exist. Available: {available_versions}") from e
    except ImportError as e:
        raise OSDUClientError(f"Client for service {name} does not exist.") from e
    return client_class


class OSDUAPI:
    @staticmethod
    def client(service_name, auth_backend: AuthBackendInterface, version: str | None = None, validation: bool = True) -> OSDUAPIClient:
        client_class = get_service_client(service_name, version)
        return client_class(
            auth_backend=auth_backend,
            validation=validation,
        )
