from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    CreateDatasetRegistryRequest,
    GetDatasetRegistryRequest,
    GetDatasetRegistryRequest,
)


class DatasetAPIError(OSDUAPIError):
    pass


class DatasetClient(OSDUAPIClient):
    service_path = "/api/dataset/v1/"

    def create_or_update_dataset_registry(
        self,
        *,
        dataset_registries: list[dict],
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "datasetRegistries": dataset_registries,
        }

        validate_data(data, CreateDatasetRegistryRequest, DatasetAPIError)

        url = urljoin(self.base_url, self.service_path, "registerDataset")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_storage_instructions(
        self,
        *,
        kind_sub_type: str,
        expiry_time: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "kindSubType": kind_sub_type,
        }
        if expiry_time is not None:
            params["expiryTime"] = expiry_time

        url = urljoin(self.base_url, self.service_path, "storageInstructions")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_revoke_url(
        self,
        *,
        kind_sub_type: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "kindSubType": kind_sub_type,
        }

        url = urljoin(self.base_url, self.service_path, "revokeURL")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_retrieval_instructions(
        self,
        *,
        id: str,
        expiry_time: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "id": id,
        }
        if expiry_time is not None:
            params["expiryTime"] = expiry_time

        url = urljoin(self.base_url, self.service_path, "retrievalInstructions")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_retrieval_instructions_for_multiple_datasets(
        self,
        *,
        dataset_registry_ids: list[str],
        expiry_time: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if expiry_time is not None:
            params["expiryTime"] = expiry_time

        data = {
            "datasetRegistryIds": dataset_registry_ids,
        }

        validate_data(data, GetDatasetRegistryRequest, DatasetAPIError)

        url = urljoin(self.base_url, self.service_path, "retrievalInstructions")
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_registry(
        self,
        *,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "id": id,
        }

        url = urljoin(self.base_url, self.service_path, "getDatasetRegistry")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_registries(
        self,
        *,
        dataset_registry_ids: list[str],
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "datasetRegistryIds": dataset_registry_ids,
        }

        validate_data(data, GetDatasetRegistryRequest, DatasetAPIError)

        url = urljoin(self.base_url, self.service_path, "getDatasetRegistry")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
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
            raise DatasetAPIError(response.text, response.status_code)
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
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()
