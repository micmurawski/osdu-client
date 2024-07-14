import pytest
import os
from tests.utils import create_swagger_server
from osdu_client.auth import AuthBackendInterface
from osdu_client.client import OSDUAPI, OSDUAPIClient
import requests_mock


BASE_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="session")
def auth_backend() -> AuthBackendInterface:
    class AuthSession(AuthBackendInterface):
        base_url = "https://base.url"
        default_data_partition_id = "osdu"
        default_tenant = "osdu"
        authorization_header = {"Authorization": "Bearer access_token"}


        def get_sd_connection_params(self):
            return {}


    return AuthSession()



@pytest.fixture(scope="session")
def rafs_api_server():
    with requests_mock.Mocker() as mocker:
        create_swagger_server(mocker, os.path.join(BASE_DIR, "swagger.yaml"))
        yield mocker



@pytest.fixture(scope="session")
def rafs_client(auth_backend: AuthBackendInterface) -> OSDUAPIClient:
    return OSDUAPI.client("rafs", auth_backend=auth_backend)
