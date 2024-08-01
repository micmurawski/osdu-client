from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    PartitionInfo,
)


class PartitionAPIError(OSDUAPIError):
    pass


class PartitionClient(OSDUAPIClient):
    service_path = "/api/partition/v1"

    def get_partition(
        self, *, partition_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get all properties and their values for a given data partition id
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            partition_id (str): Partition Id
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def create_partitions(
        self,
        *,
        partition_id: str,
        properties: dict,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Creates a new data partition with all given properties and their values.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            partition_id (str): Partition Id
            properties (dict): Free form key value pair object for any data partition specific values
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "properties": properties,
        }

        if self.validation:
            validate_data(request_data, PartitionInfo)

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def delete_partition(
        self, *, partition_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete all the properties of a given data partition
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            partition_id (str): Partition Id
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def update_partitions(
        self,
        *,
        partition_id: str,
        properties: dict,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Add new properties or update existing properties of a given data partition
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            partition_id (str): Partition Id
            properties (dict): Free form key value pair object for any data partition specific values
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "properties": properties,
        }

        if self.validation:
            validate_data(request_data, PartitionInfo)

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def list_partitions(self, data_partition_id: str | None = None) -> dict:
        """
        Returns all existing data partitions
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

        url = urljoin(self.base_url, self.service_path, "partitions")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint.
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

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/info` endpoint, which provides build and git related information.
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

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()
