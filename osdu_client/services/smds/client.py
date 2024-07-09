from osdu_client.utils import urljoin
from osdu_client.services.base import BaseOSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
import requests
from .models import (
    DatasetRegisterBody,
    DatasetPatch,
    DatasetListBody,
    DatasetCheckList,
    DatasetCheckList,
    DatasetLsBody,
    ImpTokenRequest,
    RefreshTokenRequest,
    ImpTokenPatchRequest,
    ImpersonationTokenRequest,
    SubProjectCreateBody,
    SubProjectPatchBody,
    TenantCreateBody,
    UserAddRequest,
    DatasetBulkDeleteBody,
)


class SMDSAPIError(OSDUAPIError):
    pass


class SMDSClient(BaseOSDUAPIClient):
    def get_svcstatus(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "svcstatus")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_svcstatus_access(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "svcstatus/access")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        impersonation_token_context: dict | None = None,
        ltag: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        DatasetRegisterBody(**data)

        url = urljoin(
            self.base_url,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset(
        self,
        *,
        impersonation_token_context: dict | None = None,
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
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def delete_dataset(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        close: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        DatasetPatch(**data)

        url = urljoin(
            self.base_url,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.patch(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def acquire_lock_for_dataset_id(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        openmode: str | None = None,
        wid: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/lock"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def remove_lock_associated_with_dataset_id(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/unlock"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_access_permissions_user_on_dataset_id(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/permission"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_dataset_tenant_subproject_dataset_ctagcheck(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        ctag: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/ctagcheck"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def upsert_tags_to_dataset(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        gtag: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/gtags"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def compute_and_get_size_dataset(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/dataset/%s/size"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_datasets_size(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        datasetid: str | None = None,
        path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/size" % (tenantid, subprojectid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_content_list(
        self,
        *,
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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
            "dataset/tenant/%s/subproject/%s/readdsdirfulllist"
            % (tenantid, subprojectid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        translate_user_info: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        DatasetListBody(**data)

        url = urljoin(
            self.base_url, "dataset/tenant/%s/subproject/%s" % (tenantid, subprojectid)
        )
        response = requests.post(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_dataset_tenant_subproject_exist(
        self,
        *,
        datasets: list[str],
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        data = {
            "datasets": datasets,
        }

        DatasetCheckList(**data)

        url = urljoin(
            self.base_url,
            "dataset/tenant/%s/subproject/%s/exist" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_datasets_sizes(
        self,
        *,
        datasets: list[str],
        impersonation_token_context: dict | None = None,
        tenantid: str,
        subprojectid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        data = {
            "datasets": datasets,
        }

        DatasetCheckList(**data)

        url = urljoin(
            self.base_url,
            "dataset/tenant/%s/subproject/%s/sizes" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def list_datasets(
        self,
        *,
        impersonation_token_context: dict | None = None,
        sdpath: str,
        wmode: str | None = None,
        limit: str | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        url = urljoin(self.base_url, "utility/ls")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def list_post_datasets(
        self,
        *,
        sdpath: str,
        wmode: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        impersonation_token_context: dict | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        DatasetLsBody(**data)

        url = urljoin(self.base_url, "utility/ls")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_utility_storage_tiers(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "utility/storage-tiers")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def copy_dataset(
        self,
        *,
        impersonation_token_context: dict | None = None,
        sdpath_from: str,
        sdpath_to: str,
        lock: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        url = urljoin(self.base_url, "utility/cp")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_utility_gcs_access_token(
        self,
        *,
        impersonation_token_context: dict | None = None,
        sdpath: str,
        readonly: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        url = urljoin(self.base_url, "utility/gcs-access-token")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_utility_upload_connection_string(
        self,
        *,
        impersonation_token_context: dict | None = None,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "utility/upload-connection-string")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_utility_download_connection_string(
        self,
        *,
        impersonation_token_context: dict | None = None,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "utility/download-connection-string")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
            "resources": resources,
            "refresh-url": refresh_url,
        }

        ImpTokenRequest(**data)

        url = urljoin(self.base_url, "imptoken")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def update_imptoken(
        self,
        *,
        token: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
        }

        RefreshTokenRequest(**data)

        url = urljoin(self.base_url, "imptoken")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def patch_imptoken(
        self,
        *,
        token: str,
        refresh_url: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "token": token,
            "refresh-url": refresh_url,
        }

        ImpTokenPatchRequest(**data)

        url = urljoin(self.base_url, "imptoken")
        response = requests.patch(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_impersonation_token(
        self,
        *,
        resources: list[dict],
        metadata: dict | None = None,
        user_token: dict,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        ImpersonationTokenRequest(**data)

        url = urljoin(self.base_url, "impersonation-token")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def update_impersonation_token(
        self,
        *,
        impersonation_token: dict,
        impersonation_token_context: dict,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        url = urljoin(self.base_url, "impersonation-token")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_new_subproject(
        self,
        *,
        admin: str | None = None,
        storage_class: str | None = None,
        storage_location: str | None = None,
        access_policy: str | None = "uniform",
        acls: dict | None = None,
        ltag: dict | None = None,
        subprojectid: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        SubProjectCreateBody(**data)

        url = urljoin(
            self.base_url,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if translate_user_info is not None:
            params["translate-user-info"] = translate_user_info

        url = urljoin(
            self.base_url,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def delete_subproject(
        self,
        *,
        subprojectid: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def patch_subprojects_metadata(
        self,
        *,
        access_policy: str | None = "dataset",
        acls: dict | None = None,
        ltag: dict,
        tenantid: str,
        subprojectid: str,
        recursive: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        SubProjectPatchBody(**data)

        url = urljoin(
            self.base_url,
            "subproject/tenant/%s/subproject/%s" % (tenantid, subprojectid),
        )
        response = requests.patch(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_subproject_tenant(
        self,
        *,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "subproject/tenant/%s" % tenantid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_tenant(
        self,
        *,
        gcpid: str,
        esd: str,
        default_acls: str,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "gcpid": gcpid,
            "esd": esd,
            "default_acls": default_acls,
        }

        TenantCreateBody(**data)

        url = urljoin(self.base_url, "tenant/%s" % tenantid)
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant(
        self,
        *,
        tenantid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "tenant/%s" % tenantid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant_sdpath(
        self,
        *,
        datapartition: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "datapartition": datapartition,
        }

        url = urljoin(self.base_url, "tenant/sdpath")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
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
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "email": email,
            "path": path,
            "group": group,
        }

        UserAddRequest(**data)

        url = urljoin(self.base_url, "user")
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_user(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "user")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def delete_user(
        self,
        *,
        email: str,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "path": path,
        }

        url = urljoin(self.base_url, "user")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_user_roles(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "user/roles")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_app(
        self,
        *,
        email: str,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "app")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_app(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "app")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def create_app_trusted(
        self,
        *,
        email: str,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "app/trusted")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_app_trusted(
        self,
        *,
        sdpath: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, "app/trusted")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def update_operation_bulk_delete(
        self,
        *,
        filter: dict | None = None,
        path: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
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

        DatasetBulkDeleteBody(**data)

        url = urljoin(self.base_url, "operation/bulk-delete")
        response = requests.put(url, headers=headers, params=params, json=data)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()

    def get_operation_bulk_delete(
        self,
        *,
        operation_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "operation/bulk-delete/%s" % operation_id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SMDSAPIError(response.text, response.status_code)
        return response.json()
