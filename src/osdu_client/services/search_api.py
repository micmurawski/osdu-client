import os
from typing import AnyStr, Dict

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class SearchAPIError(OSDUAPIError):
    pass


class SearchAPIClient(BaseOSDUAPIClient):

    def search_query(
        self,
        *,
        kind: AnyStr,
        query: AnyStr,
        limit: int = 20,
        offset: int = 0
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/search/v2/query",
        )
        data = {"kind": kind, "query": query, "limit": limit, "offset": offset}
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=data
        )

        if not response.ok:
            raise SearchAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
