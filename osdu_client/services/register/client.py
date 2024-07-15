from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CreateAction, Ddms, Record, Secret, Subscription, TestAction


class RegisterAPIError(OSDUAPIError):
    pass


class RegisterClient(OSDUAPIClient):
    service_path = "/api/register/v1"

    def get_ddms(self, *, id: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_ddms(self, *, id: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if id is not None:
            request_data["id"] = id
        if name is not None:
            request_data["name"] = name
        if description is not None:
            request_data["description"] = description
        if contact_email is not None:
            request_data["contactEmail"] = contact_email
        if interfaces is not None:
            request_data["interfaces"] = interfaces

        if self.validation:
            validate_data(request_data, Ddms, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "ddms")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def query_ddms(self, *, type: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {
            "type": type,
        }

        url = urljoin(self.base_url, self.service_path, "ddms")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_d(
        self, *, id: str, type: str, localid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/%s/%s/%s" % (id, type, localid)
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_action(self, *, id: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "action/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_action(self, *, id: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if id is not None:
            request_data["id"] = id
        if name is not None:
            request_data["name"] = name
        if description is not None:
            request_data["description"] = description
        if contact_email is not None:
            request_data["contactEmail"] = contact_email
        if img is not None:
            request_data["img"] = img
        if url is not None:
            request_data["url"] = url
        if filter is not None:
            request_data["filter"] = filter

        if self.validation:
            validate_data(request_data, CreateAction, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def create_action_test(
        self,
        *,
        action: dict | None = None,
        test_payload: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if action is not None:
            request_data["action"] = action
        if test_payload is not None:
            request_data["testPayload"] = test_payload

        if self.validation:
            validate_data(request_data, TestAction, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action:test")
        response = requests.post(url, headers=headers, json=request_data)
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if id is not None:
            request_data["id"] = id
        if kind is not None:
            request_data["kind"] = kind
        if acl is not None:
            request_data["acl"] = acl
        if legal is not None:
            request_data["legal"] = legal
        if data is not None:
            request_data["data"] = data

        if self.validation:
            validate_data(request_data, Record, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "action:retrieve")
        response = requests.post(url, headers=headers, json=request_data)
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if name is not None:
            request_data["name"] = name
        if description is not None:
            request_data["description"] = description
        if topic is not None:
            request_data["topic"] = topic
        if push_endpoint is not None:
            request_data["pushEndpoint"] = push_endpoint
        if secret is not None:
            request_data["secret"] = secret

        if self.validation:
            validate_data(request_data, Subscription, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "subscription")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_subscription(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "subscription/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_subscription(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if secret_type is not None:
            request_data["secretType"] = secret_type
        if value is not None:
            request_data["value"] = value

        if self.validation:
            validate_data(request_data, Secret, RegisterAPIError)

        url = urljoin(self.base_url, self.service_path, "subscription/%s/secret" % id)
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_topics(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "topics")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()
