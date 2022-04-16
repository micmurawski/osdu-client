import os
from typing import Dict

import requests

from .base_api import BaseOSDUAPIClient


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
            raise Exception(response.text)

        return response.json()
