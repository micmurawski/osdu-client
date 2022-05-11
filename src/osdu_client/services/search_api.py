import os
from typing import AnyStr, Dict, List

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
        spatial_filter: Dict = None,
        returned_fields: List[AnyStr] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/search/v2/query",
        )
        data = {
            "kind": kind,
            "query": query,
            "limit": limit,
            "offset": offset,
        }

        if spatial_filter:
            data["spatialFilter"] = spatial_filter

        if returned_fields:
            data["returnedFields"] = returned_fields

        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=data
        )

        if not response.ok:
            raise SearchAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def search_query_with_cursor(
        self,
        *,
        kind: AnyStr,
        query: AnyStr,
        spatial_filter: Dict = None,
        returned_fields: List[AnyStr] = None,
        cursor: AnyStr = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/search/v2/query_with_cursor",
        )
        data = {
            "kind": kind,
            "query": query,
            "limit": limit,
            "offset": offset,
        }

        if spatial_filter:
            data["spatialFilter"] = spatial_filter

        if returned_fields:
            data["returnedFields"] = returned_fields

        if cursor:
            data["cursor"] = cursor

        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=data
        )

        if not response.ok:
            raise SearchAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
