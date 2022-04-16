import os
from typing import Dict

import requests

from . import OSDUAPIException
from .base_api import BaseOSDUAPIClient


class EntitlementsAPIException(OSDUAPIException):
    pass


class EntitlementsAPIClient(BaseOSDUAPIClient):
    service_path = "api/entitlements/v2"

    def get_groups(self) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "groups",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise EntitlementsAPIException(response.text)

        return response.json()

    def get_members_groups(
        self,
        *,
        member_email,
        type="None"
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"members/{member_email}/groups",
        )
        params = {"type": type}
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers, params=params)

        if response.status_code // 100 != 2:
            raise EntitlementsAPIException(response.text)

        return response.json()
