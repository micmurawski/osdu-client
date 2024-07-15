from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import (DatasetBulkDeleteBody, DatasetCheckList, DatasetListBody, DatasetLsBody, DatasetPatch,
                     DatasetRegisterBody, ImpersonationTokenRequest, ImpTokenPatchRequest, ImpTokenRequest,
                     RefreshTokenRequest, SubProjectCreateBody, SubProjectPatchBody, TenantCreateBody, UserAddRequest)


class SDMSAPIError(OSDUAPIError):
    pass


class SDMSClient(OSDUAPIClient):
    service_path = "api/seismic-store/v3"

    def get_svcstatus(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "svcstatus")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_svcstatus_access(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "svcstatus/access")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
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
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_new_dataset(
        self,
        *,
        type: str | None = None,
        gtags: list[str] | None = None,
        seismicmeta: dict | None = None,
        openzgy_v1: dict | None = None,
        segy_v1: dict | None = None,
        acls: dict | None = None,
        impersonation_token_context: str | None = None,
        ltag: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context
        if ltag is not None:
            headers["ltag"] = ltag

        params = {}
        if path is not None:
            params["path"] = path

        data = {}
        if type is not None:
            data["type"] = type
        if gtags is not None:
            data["gtags"] = gtags
        if seismicmeta is not None:
            data["seismicmeta"] = seismicmeta
        if openzgy_v1 is not None:
            data["openzgy_v1"] = openzgy_v1
        if segy_v1 is not None:
            data["segy_v1"] = segy_v1
        if acls is not None:
            data["acls"] = acls

        if self.validation:
            validate_data(data, DatasetRegisterBody, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        seismicmeta: str | None = None,
        translate_user_info: str | None = None,
        record_version: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path
        if seismicmeta is not None:
            params["seismicmeta"] = seismicmeta
        if translate_user_info is not None:
            params["translate-user-info"] = translate_user_info
        if record_version is not None:
            params["record-version"] = record_version

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def delete_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def patch_dataset_metadata(
        self,
        *,
        dataset_new_name: str | None = None,
        metadata: dict | None = None,
        filemetadata: dict | None = None,
        last_modified_date: str | None = None,
        gtags: list[str] | None = [],
        ltag: str | None = None,
        readonly: bool | None = None,
        status: str | None = None,
        seismicmeta: dict | None = None,
        openzgy_v1: dict | None = None,
        segy_v1: dict | None = None,
        acls: dict | None = None,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        close: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path
        if close is not None:
            params["close"] = close

        data = {}
        if dataset_new_name is not None:
            data["dataset_new_name"] = dataset_new_name
        if metadata is not None:
            data["metadata"] = metadata
        if filemetadata is not None:
            data["filemetadata"] = filemetadata
        if last_modified_date is not None:
            data["last_modified_date"] = last_modified_date
        if gtags is not None:
            data["gtags"] = gtags
        if ltag is not None:
            data["ltag"] = ltag
        if readonly is not None:
            data["readonly"] = readonly
        if status is not None:
            data["status"] = status
        if seismicmeta is not None:
            data["seismicmeta"] = seismicmeta
        if openzgy_v1 is not None:
            data["openzgy_v1"] = openzgy_v1
        if segy_v1 is not None:
            data["segy_v1"] = segy_v1
        if acls is not None:
            data["acls"] = acls

        if self.validation:
            validate_data(data, DatasetPatch, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.patch(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def acquire_lock_for_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        openmode: str | None = None,
        wid: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path
        if openmode is not None:
            params["openmode"] = openmode
        if wid is not None:
            params["wid"] = wid

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/lock"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def remove_lock_associated_with_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/unlock"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_access_permissions(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/permission"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def validate_ctag(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        ctag: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "ctag": ctag,
        }
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/ctagcheck"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def upsert_tags_to_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        gtag: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "gtag": gtag,
        }
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/gtags"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def compute_and_get_size_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "path": path,
        }

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s/size"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_datasets_sizes(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        datasetid: str | None = None,
        path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if datasetid is not None:
            params["datasetid"] = datasetid
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/size" % (tenantid, subprojectid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_content_list(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/readdsdirfulllist"
            % (tenantid, subprojectid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_datasets_in_subproject(
        self,
        *,
        type: str | None = None,
        gtags: list[str] | None = None,
        search: str | None = None,
        filter: dict | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        translate_user_info: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if translate_user_info is not None:
            params["translate-user-info"] = translate_user_info

        data = {}
        if type is not None:
            data["type"] = type
        if gtags is not None:
            data["gtags"] = gtags
        if search is not None:
            data["search"] = search
        if filter is not None:
            data["filter"] = filter
        if limit is not None:
            data["limit"] = limit
        if cursor is not None:
            data["cursor"] = cursor

        if self.validation:
            validate_data(data, DatasetListBody, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def check_datasets_list(
        self,
        *,
        datasets: list[str],
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        data = {
            "datasets": datasets,
        }

        if self.validation:
            validate_data(data, DatasetCheckList, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/exist" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_datasets_sizes(
        self,
        *,
        datasets: list[str],
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        data = {
            "datasets": datasets,
        }

        if self.validation:
            validate_data(data, DatasetCheckList, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/sizes" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def ls(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath: str,
        wmode: str | None = None,
        limit: str | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }
        if wmode is not None:
            params["wmode"] = wmode
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        url = urljoin(self.base_url, self.service_path, "utility/ls")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def ls_post(
        self,
        *,
        sdpath: str,
        wmode: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        impersonation_token_context: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        data = {
            "sdpath": sdpath,
        }
        if wmode is not None:
            data["wmode"] = wmode
        if limit is not None:
            data["limit"] = limit
        if cursor is not None:
            data["cursor"] = cursor

        if self.validation:
            validate_data(data, DatasetLsBody, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "utility/ls")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_storage_tiers(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "utility/storage-tiers")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def copy_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath_from: str,
        sdpath_to: str,
        lock: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath_from": sdpath_from,
            "sdpath_to": sdpath_to,
        }
        if lock is not None:
            params["lock"] = lock

        url = urljoin(self.base_url, self.service_path, "utility/cp")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_gcs_access_token(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath: str,
        readonly: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }
        if readonly is not None:
            params["readonly"] = readonly

        url = urljoin(self.base_url, self.service_path, "utility/gcs-access-token")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_upload_connection_credential_string(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(
            self.base_url, self.service_path, "utility/upload-connection-string"
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_download_connection_credentials_string(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(
            self.base_url, self.service_path, "utility/download-connection-string"
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def create_imptoken(
        self,
        *,
        token: str,
        resources: list[dict],
        refresh_url: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
            "resources": resources,
            "refresh-url": refresh_url,
        }

        if self.validation:
            validate_data(data, ImpTokenRequest, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def refresh_imptoken(
        self,
        *,
        token: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
        }

        if self.validation:
            validate_data(data, RefreshTokenRequest, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def patch_imptoken(
        self,
        *,
        token: str,
        refresh_url: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
            "refresh-url": refresh_url,
        }

        if self.validation:
            validate_data(data, ImpTokenPatchRequest, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.patch(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def create_impersonation_token(
        self,
        *,
        resources: list[dict],
        metadata: dict | None = None,
        user_token: str,
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
                "user-token": user_token,
            }
        )

        data = {
            "resources": resources,
        }
        if metadata is not None:
            data["metadata"] = metadata

        if self.validation:
            validate_data(data, ImpersonationTokenRequest, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "impersonation-token")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def refresh_impersonation_token(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
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
                "impersonation-token": impersonation_token,
                "impersonation-token-context": impersonation_token_context,
            }
        )

        url = urljoin(self.base_url, self.service_path, "impersonation-token")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def create_new_subproject(
        self,
        *,
        admin: str | None = None,
        storage_class: str | None = None,
        storage_location: str | None = None,
        access_policy: str | None = "uniform",
        acls: dict | None = None,
        ltag: str | None = None,
        subprojectid: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if ltag is not None:
            headers["ltag"] = ltag

        data = {}
        if admin is not None:
            data["admin"] = admin
        if storage_class is not None:
            data["storage_class"] = storage_class
        if storage_location is not None:
            data["storage_location"] = storage_location
        if access_policy is not None:
            data["access_policy"] = access_policy
        if acls is not None:
            data["acls"] = acls

        if self.validation:
            validate_data(data, SubProjectCreateBody, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_subproject_metadata(
        self,
        *,
        subprojectid: str,
        tenantid: str,
        translate_user_info: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if translate_user_info is not None:
            params["translate-user-info"] = translate_user_info

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def delete_subproject(
        self,
        *,
        subprojectid: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def patch_subprojects_metadata(
        self,
        *,
        access_policy: str | None = "dataset",
        acls: dict | None = None,
        ltag: str,
        tenantid: str,
        subprojectid: str,
        recursive: str | None = None,
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
                "ltag": ltag,
            }
        )

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        data = {}
        if access_policy is not None:
            data["access_policy"] = access_policy
        if acls is not None:
            data["acls"] = acls

        if self.validation:
            validate_data(data, SubProjectPatchBody, SDMSAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (tenantid, subprojectid),
        )
        response = requests.patch(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_subprojects_in_tenant(
        self,
        *,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "subproject/tenant/%s" % tenantid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_tenant(
        self,
        *,
        gcpid: str,
        esd: str,
        default_acls: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "gcpid": gcpid,
            "esd": esd,
            "default_acls": default_acls,
        }

        if self.validation:
            validate_data(data, TenantCreateBody, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "tenant/%s" % tenantid)
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant(
        self,
        *,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "tenant/%s" % tenantid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant_sdpath(
        self,
        *,
        datapartition: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "datapartition": datapartition,
        }

        url = urljoin(self.base_url, self.service_path, "tenant/sdpath")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def update_user(
        self,
        *,
        email: str,
        path: str,
        group: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "email": email,
            "path": path,
            "group": group,
        }

        if self.validation:
            validate_data(data, UserAddRequest, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_user(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def delete_user(
        self,
        *,
        email: str,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "path": path,
        }

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_user_roles(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "user/roles")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_app(
        self,
        *,
        email: str,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_app(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def set_app_trusted(
        self,
        *,
        email: str,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app/trusted")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_app_trusted(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app/trusted")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def delete_all_datasets_in_subproject(
        self,
        *,
        filter: dict | None = None,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "path": path,
        }

        data = {}
        if filter is not None:
            data["filter"] = filter

        if self.validation:
            validate_data(data, DatasetBulkDeleteBody, SDMSAPIError)

        url = urljoin(self.base_url, self.service_path, "operation/bulk-delete")
        response = requests.put(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_operation_bulk_delete_status(
        self,
        *,
        operation_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "operation/bulk-delete/%s" % operation_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()
