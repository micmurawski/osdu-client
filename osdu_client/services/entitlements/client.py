from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin


class EntitlementsAPIError(OSDUAPIError):
    pass


class EntitlementsClient(OSDUAPIClient):
    service_path = "/api/entitlements/v2"

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "_ah/liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "_ah/readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_groups(
        self,
        *,
        on_behalf_of: str | None = None,
        role_required: str | None = False,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if on_behalf_of is not None:
            headers["on-behalf-of"] = on_behalf_of

        params = {}
        if role_required is not None:
            params["roleRequired"] = role_required

        url = urljoin(self.base_url, self.service_path, "groups")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def create_group(
        self, *, group_info_dto: dict, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "groupInfoDto": group_info_dto,
        }

        url = urljoin(self.base_url, self.service_path, "groups")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def delete_group(
        self, *, group_email: str | None = None, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if group_email is not None:
            params["groupEmail"] = group_email

        url = urljoin(self.base_url, self.service_path, "groups/%s")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def update_groups(
        self,
        *,
        update_group_request: list[dict],
        group_email: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "updateGroupRequest": update_group_request,
        }

        url = urljoin(self.base_url, self.service_path, "groups/%s" % group_email)
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_groups_members(
        self,
        *,
        group_email: str,
        role: str | None = None,
        include_type: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if role is not None:
            params["role"] = role
        if include_type is not None:
            params["includeType"] = include_type

        url = urljoin(
            self.base_url, self.service_path, "groups/%s/members" % group_email
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def add_member(
        self,
        *,
        add_member_dto: dict,
        group_email: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "addMemberDto": add_member_dto,
        }

        url = urljoin(
            self.base_url, self.service_path, "groups/%s/members" % group_email
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def delete_member_from_group(
        self,
        *,
        group_email: str,
        member_email: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "groups/%s/members/%s" % (group_email, member_email),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def delete_member(
        self, *, member_email: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "members/%s" % member_email)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_members_groups(
        self,
        *,
        member_email: str,
        type: str,
        appid: str | None = None,
        role_required: str | None = False,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {
            "type": type,
        }
        if appid is not None:
            params["appid"] = appid
        if role_required is not None:
            params["roleRequired"] = role_required

        url = urljoin(
            self.base_url, self.service_path, "members/%s/groups" % member_email
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def initiate_tenant(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "tenant-provisioning")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def get_count_group_members(
        self,
        *,
        group_email: str,
        role: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if role is not None:
            params["role"] = role

        url = urljoin(
            self.base_url, self.service_path, "groups/%s/membersCount" % group_email
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()

    def list_partition_groups(
        self,
        *,
        type: str,
        cursor: str | None = None,
        limit: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {
            "type": type,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit

        url = urljoin(
            self.base_url, self.service_path, "api/entitlements/v2/groups/all"
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise EntitlementsAPIError(response.text, response.status_code)
        return response.json()
