from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import StatusDto


class PWSAPIError(OSDUAPIError):
    pass


class PWSClient(OSDUAPIClient):
    service_path = "/api/pws/v1/"

    def get_projects(self, data_partition_id: str | None = None) -> dict:
        """
        This API returns a list of projects.
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

        url = urljoin(self.base_url, self.service_path, "projects")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def create_project(self, data_partition_id: str | None = None) -> dict:
        """
        The API performs new collaboration project creation.
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

        url = urljoin(self.base_url, self.service_path, "projects")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def change_projects_status(
        self,
        *,
        id: str,
        status: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        The API to change status by project Id.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            status (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if status is not None:
            request_data["status"] = status

        if self.validation:
            validate_data(request_data, StatusDto)

        url = urljoin(self.base_url, self.service_path, "projects/%s/status" % id)
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_project_resources(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the given record by project Id.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def assign_projects_resources(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs assignment of resources to the collaboration project.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def delete_projects_resources(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API revoke resources by project Id.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "projects/%s/resources" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_projects_lifecycleevent(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs read operation of LifecycleEvents from the collaboration project.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def assign_projects_lifecycleevent(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs assignment of LifecycleEvents to the collaboration project.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def delete_projects_lifecycleevent(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs delete operation of LifecycleEvents from the collaboration project.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/lifecycleevent" % id
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_project(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        The API returns the given record by its Id.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "projects/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_projects_wip_resources(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the given record by project Id.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "projects/%s/wip-resources" % id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
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
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/readiness_check` endpoint, which provides `PWS service is ready` message.
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

        url = urljoin(self.base_url, self.service_path, "_ah/readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint, which provides `PWS service is alive` message.
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

        url = urljoin(self.base_url, self.service_path, "_ah/liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PWSAPIError(response.text, response.status_code)
        return response.json()
