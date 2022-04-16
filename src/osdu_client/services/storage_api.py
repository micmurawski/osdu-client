import os
from typing import AnyStr, Dict, List

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class StorageAPIError(OSDUAPIError):
    pass


class StorageAPIClient(BaseOSDUAPIClient):

    def create_or_update_records(
        self, records: List[Dict]
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/storage/v2/records/",
        )
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, json=records
        )

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def get_record(
        self,
        *,
        id: AnyStr,


    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"api/storage/v2/records/{id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def delete_record(
        self,
        *,
        id: AnyStr
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"api/storage/v2/records/{id}",
        )
        response = requests.delete(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

    def get_record_versions(
        self,
        *,
        id: AnyStr,
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"api/storage/v2/records/versions/{id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def get_specific_record(
        self,
        *,
        versioned_id: AnyStr
    ) -> Dict:
        id, version = versioned_id.rsplit(":", 1)
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"api/storage/v2/records/{id}/{version}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def query_records(
        self,
        *,
        records: List[AnyStr]
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/storage/v2/query/records",
        )
        response = requests.post(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json={"records": records},
        )

        if response.status_code // 100 != 2:
            raise StorageAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
