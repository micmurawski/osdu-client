from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import Secret


class SecretAPIError(OSDUAPIError):
    pass


class SecretClient(OSDUAPIClient):
    service_path = "http://localhost:8080/api/secret/v1"

    def get_secret(
        self,
        *,
        secret_name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def update_secret(
        self,
        *,
        id: str | None = None,
        key: str | None = None,
        value: str | None = None,
        created_at: str | None = None,
        enabled: bool | None = None,
        secret_name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if id is not None:
            data["id"] = id
        if key is not None:
            data["key"] = key
        if value is not None:
            data["value"] = value
        if created_at is not None:
            data["createdAt"] = created_at
        if enabled is not None:
            data["enabled"] = enabled

        if self.validation:
            validate_data(data, Secret, SecretAPIError)

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def delete_secret(
        self,
        *,
        secret_name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "secrets/%s" % secret_name)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def list_secrets(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

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
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if id is not None:
            data["id"] = id
        if key is not None:
            data["key"] = key
        if value is not None:
            data["value"] = value
        if created_at is not None:
            data["createdAt"] = created_at
        if enabled is not None:
            data["enabled"] = enabled

        if self.validation:
            validate_data(data, Secret, SecretAPIError)

        url = urljoin(self.base_url, self.service_path, "secrets")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def create_secrets_get(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "secrets:retrieve")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def create_secrets_recover(
        self,
        *,
        secret_name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "secrets/recover/%s" % secret_name
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def get_secrets_deleted(
        self,
        *,
        secret_name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "secrets/deleted/%s" % secret_name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
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
            raise SecretAPIError(response.text, response.status_code)
        return response.json()

    def get_health(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "health")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SecretAPIError(response.text, response.status_code)
        return response.json()
