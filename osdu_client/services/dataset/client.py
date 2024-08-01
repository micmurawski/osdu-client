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
        self, *, dataset_registries: list[dict], data_partition_id: str | None = None
    ) -> dict:
        """
            Create or Update Dataset Registry.
        **Required roles: `service.storage.creator` or `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dataset_registries (list[dict]):
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
            "datasetRegistries": dataset_registries,
        }

        if self.validation:
            validate_data(request_data, CreateDatasetRegistryRequest)

        url = urljoin(self.base_url, self.service_path, "registerDataset")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_storage_instructions(
        self,
        *,
        kind_sub_type: str,
        expiry_time: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Generate storage instructions (Eg - Signed URLs) for datasets.
        Required roles: `service.dataset.editors`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                kind_sub_type (str): subType of the kind (partition:wks:kindSubType:version)
                expiry_time (str): The Time for which Signed URL to be valid. Accepted Regex patterns are "^[0-9]+M$", "^[0-9]+H$", "^[0-9]+D$" denoting Integer values in Minutes, Hours, Days respectively. In absence of this parameter the URL would be valid for 1 Hour.
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
        self, *, kind_sub_type: str, data_partition_id: str | None = None
    ) -> dict:
        """
        ${datasetDmsAdminApi.revokeURL.description}
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            kind_sub_type (str): subType of the kind (partition:wks:kindSubType:version)
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
    ) -> dict:
        """
            Generate retrieval instructions (Eg - Signed URLs) for single dataset.
        Required roles: `service.dataset.viewers`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                id (str): Dataset registry id
                expiry_time (str): The Time for which Signed URL to be valid. Accepted Regex patterns are "^[0-9]+M$", "^[0-9]+H$", "^[0-9]+D$" denoting Integer values in Minutes, Hours, Days respectively. In absence of this parameter the URL would be valid for 1 Hour.
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
        expiry_time: str | None = None,
        dataset_registry_ids: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Generate retrieval instructions (Eg - Signed URLs) for multiple datasets.
        Required roles: `service.dataset.viewers`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                expiry_time (str): The Time for which Signed URL to be valid. Accepted Regex patterns are "^[0-9]+M$", "^[0-9]+H$", "^[0-9]+D$" denoting Integer values in Minutes, Hours, Days respectively. In absence of this parameter the URL would be valid for 1 Hour.
                dataset_registry_ids (list[str]):
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
        if expiry_time is not None:
            params["expiryTime"] = expiry_time

        request_data = {
            "datasetRegistryIds": dataset_registry_ids,
        }

        if self.validation:
            validate_data(request_data, GetDatasetRegistryRequest)

        url = urljoin(self.base_url, self.service_path, "retrievalInstructions")
        response = requests.post(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_registry(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get Dataset Registry.
        **Required roles:  `service.storage.creator` or `service.storage.admin` or `service.storage.viewer`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                id (str): Dataset registry id
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
            "id": id,
        }

        url = urljoin(self.base_url, self.service_path, "getDatasetRegistry")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_registries(
        self, *, dataset_registry_ids: list[str], data_partition_id: str | None = None
    ) -> dict:
        """
            Get Dataset Registries.
        **Required roles:  `service.storage.creator` or `service.storage.admin` or `service.storage.viewer`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dataset_registry_ids (list[str]):
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
            "datasetRegistryIds": dataset_registry_ids,
        }

        if self.validation:
            validate_data(request_data, GetDatasetRegistryRequest)

        url = urljoin(self.base_url, self.service_path, "getDatasetRegistry")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint verifies the operational status of the Dataset Service.
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
            raise DatasetAPIError(response.text, response.status_code)
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
            raise DatasetAPIError(response.text, response.status_code)
        return response.json()
