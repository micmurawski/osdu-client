from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    PartitionInfo,
    PartitionInfo,
)


class PartitionAPIError(OSDUAPIError):
    pass


class PartitionClient(OSDUAPIClient):
    service_path = "/api/partition/v1"

    def get_partition(
        self,
        *,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def create_partitions(
        self,
        *,
        properties: dict,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "properties": properties,
        }

        if self.validation:
            validate_data(data, PartitionInfo, PartitionAPIError)

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def delete_partition(
        self,
        *,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def update_partitions(
        self,
        *,
        properties: dict,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "properties": properties,
        }

        if self.validation:
            validate_data(data, PartitionInfo, PartitionAPIError)

        url = urljoin(self.base_url, self.service_path, "partitions/%s" % partition_id)
        response = requests.patch(url, headers=headers, json=data)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def list_partitions(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "partitions")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()
