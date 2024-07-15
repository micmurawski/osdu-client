from __future__ import annotations

from importlib import import_module

from osdu_client.auth import AuthBackendInterface
from osdu_client.exceptions import OSDUClientError
from osdu_client.services.base import OSDUAPIClient

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
        if available_versions:
            client_class = available_versions.get(
                version, getattr(module, "DEFAULT_VERSION")
            )
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
        """Creates client instance for given service.
            Args:
                service_name (str): The OSDU API service name, to check available services call list_available_services method.
                auth_backend (AuthBackendInterface): class object that implements AuthBackendInterface and stores all auth headers.
                version (str): Version of the service API client. If None method will produce the latest client.
                validation (bool): Disable to turn-off request body validation done before client makes a request. By default True
            Returns:
                Instance of OSDUAPIClient for given service_name
            Raises:
                OSDUClientError: if bad arguments provided

        """
        client_class = get_service_client(service_name, version)
        return client_class(
            auth_backend=auth_backend,
            validation=validation,
        )

    @classmethod
    def print_available_services(cls):
        """
        Prints available services for client
        """
        print("|      Name      |    Versions    |")
        print("===================================")
        for k, v in cls.list_available_services():
            print("|", end="")
            space = 16 - len(k)
            print((" "*(space//2))+k+(" "*((space//2) + space % 2)), end="")
            print("|", end="")
            versions_str = str(v)[1:-1].replace("'", "")
            versions_str = versions_str if len(versions_str) else "latest"
            space = 16 - len(versions_str)
            print(" "*(space//2)+versions_str+(" "*((space//2) + space % 2)), end="")
            print("|")

    @staticmethod
    def list_available_services() -> list[tuple[str, list[str]]]:
        """
        Returns list of available services for client
        Returns:
            list of available services for API versions (list[tuple[str, list[str]]])
        """
        module = import_module("osdu_client.services")
        return [(k, v) for k, v in module.SERVICES.items()]
