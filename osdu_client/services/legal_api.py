import os
from typing import AnyStr, Dict

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class LegalAPIException(OSDUAPIError):
    pass


class LegalAPIClient(BaseOSDUAPIClient):
    service_path = "api/legal/v1"

    def get_legal_tags(
        self,
        *,
        valid: bool = True,
        osdu_account_id: AnyStr = None,
        osdu_on_behalf_of: AnyStr = None,
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags",
        )
        params = {"valid": valid}
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of
        response = requests.get(url=url, headers=headers, params=params)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()
