from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    LocationRequest,
    Record,
    FileLocationRequest,
    DeliveryGetFileSignedURLRequest,
    FileListRequest,
)


class FileAPIError(OSDUAPIError):
    pass


class FileClient(OSDUAPIClient):
    service_path = "VALID_FILE_SERVICE_BASE_URL"

    def get_location(
        self,
        *,
        file_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if file_id is not None:
            data["FileID"] = file_id

        if self.validation:
            validate_data(data, LocationRequest, FileAPIError)

        url = urljoin(self.base_url, self.service_path, "v2/getLocation")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_files_upload_url(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "v2/files/uploadURL")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def create_files_metadata(
        self,
        *,
        kind: str,
        acl: dict,
        legal: dict,
        data: dict,
        id: str | None = None,
        ancestry: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "kind": kind,
            "acl": acl,
            "legal": legal,
            "data": data,
        }
        if id is not None:
            data["id"] = id
        if ancestry is not None:
            data["ancestry"] = ancestry

        if self.validation:
            validate_data(data, Record, FileAPIError)

        url = urljoin(self.base_url, self.service_path, "v2/files/metadata")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_files_metadata(
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

        url = urljoin(self.base_url, self.service_path, "v2/files/%s/metadata" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def delete_files_metadata(
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

        url = urljoin(self.base_url, self.service_path, "v2/files/%s/metadata" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def gets_url_to_download_file(
        self,
        *,
        id: str,
        expiry_time: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if expiry_time is not None:
            params["expiryTime"] = expiry_time

        url = urljoin(self.base_url, self.service_path, "v2/files/%s/downloadURL" % id)
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_file_location(
        self,
        *,
        file_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if file_id is not None:
            data["FileID"] = file_id

        if self.validation:
            validate_data(data, FileLocationRequest, FileAPIError)

        url = urljoin(self.base_url, self.service_path, "v2/getFileLocation")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_file_signed_url(
        self,
        *,
        srn: list[dict] | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if srn is not None:
            data["srn"] = srn

        if self.validation:
            validate_data(data, DeliveryGetFileSignedURLRequest, FileAPIError)

        url = urljoin(self.base_url, self.service_path, "v2/delivery/getFileSignedUrl")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_file_list(
        self,
        *,
        time_from: str | None = None,
        time_to: str | None = None,
        page_num: int | None = None,
        items: int | None = None,
        user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {}
        if time_from is not None:
            data["TimeFrom"] = time_from
        if time_to is not None:
            data["TimeTo"] = time_to
        if page_num is not None:
            data["PageNum"] = page_num
        if items is not None:
            data["Items"] = items
        if user_id is not None:
            data["UserID"] = user_id

        if self.validation:
            validate_data(data, FileListRequest, FileAPIError)

        url = urljoin(self.base_url, self.service_path, "v2/getFileList")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "v2/info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_file_collections_storage_instructions(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "v2/file-collections/storageInstructions"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def get_file_collections_retrieval_instructions(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "v2/file-collections/retrievalInstructions",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()

    def copy_file_collections(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "v2/file-collections/copy")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise FileAPIError(response.text, response.status_code)
        return response.json()
