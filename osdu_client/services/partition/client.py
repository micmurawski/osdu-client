from osdu_client.utils import urljoin
from osdu_client.services.base import BaseOSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
import requests
from .models import (
    PartitionInfo,
    PartitionInfo,
)


class PartitionAPIError(OSDUAPIError):
    pass


class PartitionClient(BaseOSDUAPIClient):
    def get_partition(
        self,
        *,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "partitions/%s" % partition_id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def create_partition(
        self,
        *,
        properties: dict,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "properties": properties,
        }

        PartitionInfo(**data)

        url = urljoin(self.base_url, "partitions/%s" % partition_id)
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
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "partitions/%s" % partition_id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def patch_partition(
        self,
        *,
        properties: dict,
        partition_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "properties": properties,
        }

        PartitionInfo(**data)

        url = urljoin(self.base_url, "partitions/%s" % partition_id)
        response = requests.patch(url, headers=headers, json=data)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def list_partitions(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "partitions")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PartitionAPIError(response.text, response.status_code)
        return response.json()
