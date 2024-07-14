from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    GuessRequest,
    CatalogRecord,
)


class WellboreAPIError(OSDUAPIError):
    pass


class WellboreCommonClient(OSDUAPIClient):
    service_path = ""

    def get_about(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "about")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def recognize_family(
        self,
        *,
        label: str,
        description: str | None = None,
        log_unit: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "label": label,
        }
        if description is not None:
            data["description"] = description
        if log_unit is not None:
            data["log_unit"] = log_unit

        validate_data(data, GuessRequest, WellboreAPIError)

        url = urljoin(self.base_url, self.service_path, "log-recognition/family")
        response = requests.post(url, headers=headers, json=data)
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
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "acl": acl,
            "data": data,
            "legal": legal,
        }

        validate_data(data, CatalogRecord, WellboreAPIError)

        url = urljoin(
            self.base_url, self.service_path, "log-recognition/upload-catalog"
        )
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_version(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "version")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
