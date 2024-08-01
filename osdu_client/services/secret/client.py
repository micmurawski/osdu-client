from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    Secret,
    Secret,
)


class SecretAPIError(OSDUAPIError):
    pass


class SecretClient(OSDUAPIClient):
    service_path = "/api/secret/v1"

    def get_secret(
        self, *, secret_name: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            secret_name (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def update_secret(
        self,
        *,
        secret_name: str,
        id: str | None = None,
        key: str | None = None,
        value: str | None = None,
        created_at: str | None = None,
        enabled: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            secret_name (str):
            id (str):
            key (str):
            value (str):
            created_at (str):
            enabled (bool):
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
        if id is not None:
            request_data["id"] = id
        if key is not None:
            request_data["key"] = key
        if value is not None:
            request_data["value"] = value
        if created_at is not None:
            request_data["createdAt"] = created_at
        if enabled is not None:
            request_data["enabled"] = enabled

        if self.validation:
            validate_data(request_data, Secret)

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def delete_secret(
        self, *, secret_name: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            secret_name (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def list_secrets(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "secrets")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def create_secrets(
        self,
        *,
        id: str | None = None,
        key: str | None = None,
        value: str | None = None,
        created_at: str | None = None,
        enabled: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            key (str):
            value (str):
            created_at (str):
            enabled (bool):
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
        if id is not None:
            request_data["id"] = id
        if key is not None:
            request_data["key"] = key
        if value is not None:
            request_data["value"] = value
        if created_at is not None:
            request_data["createdAt"] = created_at
        if enabled is not None:
            request_data["enabled"] = enabled

        if self.validation:
            validate_data(request_data, Secret)

        url = urljoin(self.base_url, self.service_path, "secrets")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def create_secrets_get(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "secrets:retrieve")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def create_secrets_recover(
        self, *, secret_name: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            secret_name (str):
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
            self.base_url, self.service_path, "secrets/recover/%s" % secret_name
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def get_secrets_deleted(
        self, *, secret_name: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            secret_name (str):
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
            self.base_url, self.service_path, "secrets/deleted/%s" % secret_name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def get_health(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "health")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()
