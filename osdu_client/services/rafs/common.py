from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin


class RAFSAPIError(OSDUAPIError):
    pass


class RAFSCommonClient(OSDUAPIClient):
    service_path = ""

    def get_metrics(self, data_partition_id: str | None = None) -> dict:
        """
        Endpoint that serves Prometheus metrics.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "metrics")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        """
            Get application info.

        :return: application info
        :rtype: InfoResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()
