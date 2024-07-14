from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    ddms,
    createAction,
    testAction,
    record,
    subscription,
    secret,
)


class RegisterAPIError(OSDUAPIError):
    pass


class RegisterClient(OSDUAPIClient):
    service_path = "/api/register/v1"

    def get_ddms(
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

        url = urljoin(self.base_url, self.service_path, "ddms/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_ddms(
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

        url = urljoin(self.base_url, self.service_path, "ddms/%s" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_ddms(
        self,
        *,
        id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        contact_email: str | None = None,
        interfaces: list[dict] | None = None,
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
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if contact_email is not None:
            data["contactEmail"] = contact_email
        if interfaces is not None:
            data["interfaces"] = interfaces

        validate_data(data, ddms, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "ddms")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def query_ddms(
        self,
        *,
        type: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "type": type,
        }

        url = urljoin(self.base_url, self.service_path, "ddms")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_d(
        self,
        *,
        id: str,
        type: str,
        localid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/%s/%s/%s" % (id, type, localid)
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_action(
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

        url = urljoin(self.base_url, self.service_path, "action/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_action(
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

        url = urljoin(self.base_url, self.service_path, "action/%s" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_action(
        self,
        *,
        id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        contact_email: str | None = None,
        img: str | None = None,
        url: str | None = None,
        filter: dict | None = None,
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
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if contact_email is not None:
            data["contactEmail"] = contact_email
        if img is not None:
            data["img"] = img
        if url is not None:
            data["url"] = url
        if filter is not None:
            data["filter"] = filter

        validate_data(data, createAction, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_action_test(
        self,
        *,
        action: dict | None = None,
        test_payload: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if action is not None:
            data["action"] = action
        if test_payload is not None:
            data["testPayload"] = test_payload

        validate_data(data, testAction, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action:test")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_action_get(
        self,
        *,
        id: str | None = None,
        kind: str | None = None,
        acl: dict | None = None,
        legal: dict | None = None,
        data: dict | None = None,
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
        if kind is not None:
            data["kind"] = kind
        if acl is not None:
            data["acl"] = acl
        if legal is not None:
            data["legal"] = legal
        if data is not None:
            data["data"] = data

        validate_data(data, record, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action:retrieve")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_subscription(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        topic: str | None = None,
        push_endpoint: str | None = None,
        secret: dict | None = None,
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
        if topic is not None:
            data["topic"] = topic
        if push_endpoint is not None:
            data["pushEndpoint"] = push_endpoint
        if secret is not None:
            data["secret"] = secret

        validate_data(data, subscription, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "subscription")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_subscription(
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

        url = urljoin(self.base_url, self.service_path, "subscription/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_subscription(
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

        url = urljoin(self.base_url, self.service_path, "subscription/%s" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def update_subscription_secret(
        self,
        *,
        secret_type: str | None = None,
        value: dict | None = None,
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
        if secret_type is not None:
            data["secretType"] = secret_type
        if value is not None:
            data["value"] = value

        validate_data(data, secret, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "subscription/%s/secret" % id)
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_topics(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "topics")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
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
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()
