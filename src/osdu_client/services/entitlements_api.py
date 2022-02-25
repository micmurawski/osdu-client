import os

import requests

from osdu_client.auth import AuthInterface

from .base_api import BaseOSDUAPIClient


class EntitlementsAPIClient(BaseOSDUAPIClient):
    service_path = "api/entitlements/v2"

    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend

    def get_groups(self):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "groups",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()
