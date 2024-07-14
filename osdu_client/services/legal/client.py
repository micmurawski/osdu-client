from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import LegalTagDto, RequestLegalTags, SearchLegalTag, UpdateLegalTag


class LegalAPIError(OSDUAPIError):
    pass


class LegalClient(OSDUAPIClient):
    service_path = "/api/legal/v1/"

    def list_legaltags(
        self,
        *,
        valid: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if valid is not None:
            params["valid"] = valid

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def update_legaltag(
        self,
        *,
        name: str | None = None,
        contract_id: str | None = None,
        description: str | None = None,
        expiration_date: str | None = None,
        extension_properties: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if name is not None:
            data["name"] = name
        if contract_id is not None:
            data["contractId"] = contract_id
        if description is not None:
            data["description"] = description
        if expiration_date is not None:
            data["expirationDate"] = expiration_date
        if extension_properties is not None:
            data["extensionProperties"] = extension_properties

        if self.validation:
            validate_data(data, UpdateLegalTag, LegalAPIError)

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def create_legaltag(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        properties: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if properties is not None:
            data["properties"] = properties

        if self.validation:
            validate_data(data, LegalTagDto, LegalAPIError)

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def validate_legaltags(
        self,
        *,
        names: list[str],
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "names": names,
        }

        if self.validation:
            validate_data(data, RequestLegalTags, LegalAPIError)

        url = urljoin(self.base_url, self.service_path, "legaltags:validate")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def query_legaltags(
        self,
        *,
        query_list: list[str] | None = None,
        operator_list: list[str] | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        limit: int | None = None,
        valid: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if valid is not None:
            params["valid"] = valid

        data = {}
        if query_list is not None:
            data["queryList"] = query_list
        if operator_list is not None:
            data["operatorList"] = operator_list
        if sort_by is not None:
            data["sortBy"] = sort_by
        if sort_order is not None:
            data["sortOrder"] = sort_order
        if limit is not None:
            data["limit"] = limit

        if self.validation:
            validate_data(data, SearchLegalTag, LegalAPIError)

        url = urljoin(self.base_url, self.service_path, "legaltags:query")
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_batch_legaltags(
        self,
        *,
        names: list[str],
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "names": names,
        }

        if self.validation:
            validate_data(data, RequestLegalTags, LegalAPIError)

        url = urljoin(self.base_url, self.service_path, "legaltags:batchRetrieve")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltags_properties(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "legaltags:properties")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltag(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "legaltags/%s" % name)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def delete_legaltag(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "legaltags/%s" % name)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltag_compliance_job_status(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "jobs/updateLegalTagStatus")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
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
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "_ah/readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "_ah/liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()
