import os
from typing import Dict

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class EntitlementsAPIException(OSDUAPIError):
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

        if response.ok:
            raise EntitlementsAPIException(
                status_code=response.status_code,
                message=response.text
            )

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

        if response.ok:
            raise EntitlementsAPIException(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
