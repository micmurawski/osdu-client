from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    StatusDto,
)


class PWSAPIError(OSDUAPIError):
    pass


class PWSClient(OSDUAPIClient):
    service_path = "/api/pws/v1/"

    def get_projects(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "projects")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def create_project(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "projects")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def change_projects_status(
        self,
        *,
        status: str | None = None,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if status is not None:
            data["status"] = status

        if self.validation:
            validate_data(data, StatusDto, PWSAPIError)

        url = urljoin(self.base_url, self.service_path, "projects/%s/status" % id)
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_project_resources(
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

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def assign_projects_resources(
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

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def delete_projects_resources(
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

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_projects_lifecycleevent(
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

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def assign_projects_lifecycleevent(
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

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def delete_projects_lifecycleevent(
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

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_project(
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

        url = urljoin(self.base_url, self.service_path, "projects/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_projects_wip_resources(
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

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/wip-resources" % id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
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
            raise PWSAPIError(response.text, response.status_code)
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
            raise PWSAPIError(response.text, response.status_code)
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
            raise PWSAPIError(response.text, response.status_code)
        return response.json()
