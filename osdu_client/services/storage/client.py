from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
from osdu_client.validation import validate_data

from .models import (
    RecordBulkUpdateParam,
    CopyRecordReferencesModel,
    MultiRecordIds,
    MultiRecordRequest,
    ReplayRequest,
)


class StorageAPIError(OSDUAPIError):
    pass


class StorageClient(OSDUAPIClient):
    service_path = "/api/storage/v2/"

    def update_records(
        self,
        *,
        x_collaboration: str | None = None,
        skipdupes: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        params = {}
        if skipdupes is not None:
            params["skipdupes"] = skipdupes

        url = urljoin(self.base_url, self.service_path, "records")
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def patch_records(
        self,
        *,
        query: dict,
        ops: list[dict],
        x_collaboration: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        data = {
            "query": query,
            "ops": ops,
        }

        validate_data(data, RecordBulkUpdateParam, StorageAPIError)

        url = urljoin(self.base_url, self.service_path, "records")
        response = requests.patch(url, headers=headers, json=data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def update_records_copy(
        self,
        *,
        target: str | None = None,
        records: list[dict] | None = None,
        x_collaboration: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        data = {}
        if target is not None:
            data["target"] = target
        if records is not None:
            data["records"] = records

        validate_data(data, CopyRecordReferencesModel, StorageAPIError)

        url = urljoin(self.base_url, self.service_path, "records/copy")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def delete_record(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        url = urljoin(self.base_url, self.service_path, "records/%s:delete" % id)
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def create_records_delete(
        self,
        *,
        x_collaboration: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        url = urljoin(self.base_url, self.service_path, "records/delete")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def query_records_from_kind(
        self,
        *,
        x_collaboration: str | None = None,
        cursor: str | None = None,
        limit: str | None = None,
        kind: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        params = {
            "kind": kind,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit

        url = urljoin(self.base_url, self.service_path, "query/records")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def query_records(
        self,
        *,
        records: list[str],
        attributes: list[str] | None = None,
        x_collaboration: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        data = {
            "records": records,
        }
        if attributes is not None:
            data["attributes"] = attributes

        validate_data(data, MultiRecordIds, StorageAPIError)

        url = urljoin(self.base_url, self.service_path, "query/records")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def query_records_batch(
        self,
        *,
        records: list[str],
        x_collaboration: str | None = None,
        frame_of_reference: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        headers.update(
            {
                "frame-of-reference": frame_of_reference,
            }
        )
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        data = {
            "records": records,
        }

        validate_data(data, MultiRecordRequest, StorageAPIError)

        url = urljoin(self.base_url, self.service_path, "query/records:batch")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_record(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        attribute: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        params = {}
        if attribute is not None:
            params["attribute"] = attribute

        url = urljoin(self.base_url, self.service_path, "records/%s" % id)
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def purge_record(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        url = urljoin(self.base_url, self.service_path, "records/%s" % id)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_record_version(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        version: str,
        attribute: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        params = {}
        if attribute is not None:
            params["attribute"] = attribute

        url = urljoin(self.base_url, self.service_path, "records/%s/%s" % (id, version))
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_record_versions(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        url = urljoin(self.base_url, self.service_path, "records/versions/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
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
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def purge_record_versions(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        version_ids: str | None = None,
        limit: str | None = None,
        _form: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        params = {}
        if version_ids is not None:
            params["versionIds"] = version_ids
        if limit is not None:
            params["limit"] = limit
        if _form is not None:
            params["from"] = _form

        url = urljoin(self.base_url, self.service_path, "records/%s/versions" % id)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_replay_status(
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

        url = urljoin(self.base_url, self.service_path, "replay/status/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def create_replay(
        self,
        *,
        operation: str,
        filter: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "operation": operation,
        }
        if filter is not None:
            data["filter"] = filter

        validate_data(data, ReplayRequest, StorageAPIError)

        url = urljoin(self.base_url, self.service_path, "replay")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def update_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def create_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def delete_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def options_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.options(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def head_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.head(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def patch_whoami(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.patch(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()
