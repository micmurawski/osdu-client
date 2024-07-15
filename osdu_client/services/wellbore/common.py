from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CatalogRecord, GuessRequest


class WellboreAPIError(OSDUAPIError):
    pass


class WellboreCommonClient(OSDUAPIClient):
    service_path = ""

    def get_about(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "about")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def recognize_family(
        self,
        *,
        description: str | None = None,
        log_unit: str | None = None,
        label: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Find the most probable family and unit using family assignment rule based catalogs. User defined catalog will have the priority.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            label (str):
            description (str):
            log_unit (str):
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
            "label": label,
        }
        if description is not None:
            request_data["description"] = description
        if log_unit is not None:
            request_data["log_unit"] = log_unit

        if self.validation:
            validate_data(request_data, GuessRequest)

        url = urljoin(self.base_url, self.service_path, "log-recognition/family")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def update_log_recognition_upload_catalog(
        self,
        *,
        acl: dict,
        data: dict,
        legal: dict,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Upload user-defined catalog with family assignment rules for specific partition ID.
                    If there is an existing catalog, it will be replaced. It takes maximum of 5 mins to replace the existing catalog.
                    Hence, any call to retrieve the family should be made after 5 mins of uploading the catalog.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                acl (dict):
                data (dict):
                legal (dict):
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
            "acl": acl,
            "data": data,
            "legal": legal,
        }

        if self.validation:
            validate_data(request_data, CatalogRecord)

        url = urljoin(
            self.base_url, self.service_path, "log-recognition/upload-catalog"
        )
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_version(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "version")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
