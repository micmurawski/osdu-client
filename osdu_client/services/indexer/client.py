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
        """
        Provision partition. Required roles: `users.datalake.ops`
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

        url = urljoin(self.base_url, self.service_path, "partitions/provision")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_kind(
        self,
        *,
        force_clean: str | None = None,
        cursor: str | None = None,
        kind: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        This API allows users to re-index a 'kind' without re-ingesting the records via storage API. Required roles: `service.search.admin`
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            force_clean (str): Force Clean
            kind (str):
            cursor (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
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
            validate_data(request_data, RecordReindexRequest)

        url = urljoin(self.base_url, self.service_path, "reindex")
        response = requests.post(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def reindex_partition(
        self, *, force_clean: str | None = None, data_partition_id: str | None = None
    ) -> dict:
        """
        This API allows users to re-index an entire partition without re-ingesting the records via storage API.Required roles: `users.datalake.ops`
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            force_clean (str): Force Clean
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
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
        """
        This API allows users to re-index the given records by providing record ids without re-ingesting the records via storage API. Required roles: `service.search.admin`
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_ids (list[str]):
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
            "recordIds": record_ids,
        }

        if self.validation:
            validate_data(request_data, ReindexRecordsRequest)

        url = urljoin(self.base_url, self.service_path, "reindex/records")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/readiness_check` endpoint.
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

        url = urljoin(self.base_url, self.service_path, "readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise IndexerAPIError(response.text, response.status_code)
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
            raise IndexerAPIError(response.text, response.status_code)
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
            raise IndexerAPIError(response.text, response.status_code)
        return response.json()

    def delete_index(self, *, kind: str, data_partition_id: str | None = None) -> dict:
        """
        Delete Index for the given kind. Required roles: `users.datalake.ops`
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            kind (str): Kind
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
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
