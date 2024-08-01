from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    Ddms,
    CreateAction,
    TestAction,
    Record,
    Subscription,
    Secret,
)


class RegisterAPIError(OSDUAPIError):
    pass


class RegisterClient(OSDUAPIClient):
    service_path = "/api/register/v1"

    def get_ddms(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        Get a DDMS registration with the given id. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
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

        url = urljoin(self.base_url, self.service_path, "ddms/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_ddms(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        Delete a DDMS registration with the given id. Required roles: 'users.datalake.admins'
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
        """
        Create a DDMS registration using an OpenApi spec V3 document. Required roles: 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            name (str):
            description (str):
            contact_email (str):
            interfaces (list[dict]):
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
        if name is not None:
            request_data["name"] = name
        if description is not None:
            request_data["description"] = description
        if contact_email is not None:
            request_data["contactEmail"] = contact_email
        if interfaces is not None:
            request_data["interfaces"] = interfaces

        if self.validation:
            validate_data(request_data, Ddms)

        url = urljoin(self.base_url, self.service_path, "ddms")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def query_ddms(self, *, type: str, data_partition_id: str | None = None) -> dict:
        """
        Query for DDMS registrations allowing retrievals by type. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str):
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
        """
        Get a Single DDMS record id. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            type (str): Specifies the type in ddms I.E wellbores
            localid (str): Specifies the record id with Optional version partition-id:group-type--IndividualType:UniqueRecordID:<OptionalVersionNumber>
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
            self.base_url, self.service_path, "ddms/%s/%s/%s" % (id, type, localid)
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_action(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        Get an action registration with the given id. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
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

        url = urljoin(self.base_url, self.service_path, "action/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_action(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        Delete an action registration with the given id. Required role: 'users.datalake.admins'
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
        """
        Create an action registration. Required role: 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            name (str):
            description (str):
            contact_email (str):
            img (str): Reference link to an image file that can be usd in an UI to represent the action.
            url (str):
            filter (dict):
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
            validate_data(request_data, CreateAction)

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
        """
        Test an action registration. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            action (dict):
            test_payload (dict):
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
        if action is not None:
            request_data["action"] = action
        if test_payload is not None:
            request_data["testPayload"] = test_payload

        if self.validation:
            validate_data(request_data, TestAction)

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
        """
        Retrieve an action registration. Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            kind (str):
            acl (dict):
            legal (dict):
            data (dict):
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
        if kind is not None:
            request_data["kind"] = kind
        if acl is not None:
            request_data["acl"] = acl
        if legal is not None:
            request_data["legal"] = legal
        if data is not None:
            request_data["data"] = data

        if self.validation:
            validate_data(request_data, Record)

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
        """
        Create a subscription. Required roles: 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str):
            description (str):
            topic (str):
            push_endpoint (str):
            secret (dict):
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
            validate_data(request_data, Subscription)

        url = urljoin(self.base_url, self.service_path, "subscription")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_subscription(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a subscription with its Id. Required role: 'users.datalake.editors' or 'users.datalake.admins'
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

        url = urljoin(self.base_url, self.service_path, "subscription/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def delete_subscription(
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete a subscription with its Id. Required role: 'users.datalake.admins'
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

        url = urljoin(self.base_url, self.service_path, "subscription/%s" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def update_subscription_secret(
        self,
        *,
        id: str,
        secret_type: str | None = None,
        value: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Update secret for a subscription. Required role: 'users.datalake.editors' or 'users.datalake.admins'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str):
            secret_type (str):
            value (dict):
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
        if secret_type is not None:
            request_data["secretType"] = secret_type
        if value is not None:
            request_data["value"] = value

        if self.validation:
            validate_data(request_data, Secret)

        url = urljoin(self.base_url, self.service_path, "subscription/%s/secret" % id)
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_topics(self, data_partition_id: str | None = None) -> dict:
        """
        List all topics that you can create a subscription for, along with the corresponding sample messages. Required role: 'users.datalake.editors' or 'users.datalake.admins'
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

        url = urljoin(self.base_url, self.service_path, "topics")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/info` endpoint,  which provides build and git related information.
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
            raise RegisterAPIError(response.text, response.status_code)
        return response.json()
