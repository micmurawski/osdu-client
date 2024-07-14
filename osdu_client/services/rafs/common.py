from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin


class RAFSAPIError(OSDUAPIError):
    pass


class RAFSCommonClient(OSDUAPIClient):
    service_path = ""

    def get_metrics(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "metrics")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()
