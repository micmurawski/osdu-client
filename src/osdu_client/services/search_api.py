import os
from typing import AnyStr

import requests

from osdu_client.auth import AuthInterface

from .base_api import BaseOSDUAPIClient


class SearchAPIClient(BaseOSDUAPIClient):
    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend

    def search_query(
        self,
        *,
        kind: AnyStr,
        query: AnyStr,
        limit: int = 20,
        offset: int = 0
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/search/v2/query",
        )
        data = {"kind": kind, "query": query, "limit": limit, "offset": offset}
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=data
        )

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()
