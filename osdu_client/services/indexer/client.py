from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import RecordReindexRequest, ReindexRecordsRequest


class IndexerAPIError(OSDUAPIError):
    pass


class IndexerClient(OSDUAPIClient):
    service_path = "/api/indexer/v2"

    def provision_partition(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "partitions/provision")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_kind(
        self,
        *,
        kind: str,
        cursor: str | None = None,
        force_clean: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if force_clean is not None:
            params["force_clean"] = force_clean

        request_data = {
            "kind": kind,
        }
        if cursor is not None:
            request_data["cursor"] = cursor

        if self.validation:
            validate_data(request_data, RecordReindexRequest, IndexerAPIError)

        url = urljoin(self.base_url, self.service_path, "reindex")
        response = requests.post(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_partition(
        self, *, force_clean: str | None = None, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if force_clean is not None:
            params["force_clean"] = force_clean

        url = urljoin(self.base_url, self.service_path, "reindex")
        response = requests.patch(url, headers=headers, params=params)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_records(
        self, *, record_ids: list[str], data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "recordIds": record_ids,
        }

        if self.validation:
            validate_data(request_data, ReindexRecordsRequest, IndexerAPIError)

        url = urljoin(self.base_url, self.service_path, "reindex/records")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def delete_index(self, *, kind: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {
            "kind": kind,
        }

        url = urljoin(self.base_url, self.service_path, "index")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()
