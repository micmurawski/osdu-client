from osdu_client.utils import urljoin
from osdu_client.services.base import BaseOSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
import requests
from .models import (
    RecordReindexRequest,
    ReindexRecordsRequest,
)


class IndexerAPIError(OSDUAPIError):
    pass


class IndexerClient(BaseOSDUAPIClient):
    def provision_partition(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "partitions/provision")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def create_reindex(
        self,
        *,
        kind: str,
        cursor: str | None = None,
        force_clean: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if force_clean is not None:
            params["force_clean"] = force_clean

        data = {
            "kind": kind,
        }
        if cursor is not None:
            data["cursor"] = cursor

        RecordReindexRequest(**data)

        url = urljoin(self.base_url, "reindex")
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def patch_reindex(
        self,
        *,
        force_clean: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if force_clean is not None:
            params["force_clean"] = force_clean

        url = urljoin(self.base_url, "reindex")
        response = requests.patch(url, headers=headers, params=params)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_given_records(
        self,
        *,
        record_ids: list[str],
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "recordIds": record_ids,
        }

        ReindexRecordsRequest(**data)

        url = urljoin(self.base_url, "reindex/records")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
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
            raise IndexerAPIError(response.text, response.status_code)
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
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def delete_index(
        self,
        *,
        kind: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "kind": kind,
        }

        url = urljoin(self.base_url, "index")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()
