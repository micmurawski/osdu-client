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

    def get_svcstatus(self, data_partition_id: str | None = None) -> dict:
        """
        Return the seismic store service status.Required roles: none
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

        url = urljoin(self.base_url, self.service_path, "svcstatus")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_svcstatus_access(self, data_partition_id: str | None = None) -> dict:
        """
        Validates if the token audience is allowedRequired roles: none
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

        url = urljoin(self.base_url, self.service_path, "svcstatus/access")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        """
        Return the seismic store service deployment information.Required roles: none
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
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_new_dataset(
        self,
        *,
        impersonation_token_context: str | None = None,
        ltag: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        type: str | None = None,
        gtags: list[str] | None = None,
        seismicmeta: dict | None = None,
        openzgy_v1: dict | None = None,
        segy_v1: dict | None = None,
        acls: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Register a new dataset in the seismic store.Required roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            ltag (str): Legal tag of the dataset.
            tenantid (str): Name of the tenant.
            subprojectid (str): Name of the subproject.
            path (str): Hierarchical path of the dataset.
            datasetid (str): Name of the dataset.
            type (str):
            gtags (list[str]): Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.
            seismicmeta (dict): Seismic metadata to be stored as dataecosystem storage record.
            openzgy_v1 (dict):
            segy_v1 (dict):
            acls (dict): ACLs with admin groups and viewer groups for the dataset.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context
        if ltag is not None:
            headers["ltag"] = ltag

        params = {}
        if path is not None:
            params["path"] = path

        request_data = {}
        if type is not None:
            request_data["type"] = type
        if gtags is not None:
            request_data["gtags"] = gtags
        if seismicmeta is not None:
            request_data["seismicmeta"] = seismicmeta
        if openzgy_v1 is not None:
            request_data["openzgy_v1"] = openzgy_v1
        if segy_v1 is not None:
            request_data["segy_v1"] = segy_v1
        if acls is not None:
            request_data["acls"] = acls

        if self.validation:
            validate_data(request_data, DatasetRegisterBody)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.post(url, headers=headers, params=params, json=request_data)
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
        seismicmeta: bool | None = None,
        translate_user_info: bool | None = None,
        record_version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
         Return the dataset metadata from seismic store. Required roles:  subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform' dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            tenantid (str): Name of the tenant.
            subprojectid (str): Name of the subproject.
            path (str): Hierarchical path of the dataset.
            datasetid (str): Name of the dataset.
            seismicmeta (bool): Include the seismic storage metadata record if it exists.
            translate_user_info (bool): translate the user-id to a more human readable user info
            record_version (str): Retrieve a specific version of the seismic storage metadata record
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
         Delete a dataset in the seismic store. Required roles:  subproject.admin: if the applied subproject policy is 'uniform' dataset.admin: if the applied subproject policy is 'dataset'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            tenantid (str): Name of the tenant.
            subprojectid (str): Name of the subproject.
            path (str): Hierarchical path of the dataset.
            datasetid (str): Name of the dataset.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        path: str | None = None,
        datasetid: str,
        close: str | None = None,
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
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Update the dataset meta information in the seismic store or close (unlock) the dataset. If the endpoint is used without the close parameter, at least one body field is required or the endpoint will return an error.
        Required roles:

            subproject.admin: if the applied subproject policy is 'uniform'
            dataset.admin: if the applied subproject policy is 'dataset'


        Patchable fields:
        dataset_new_name: new name to use for the dataset (rename).
        filemetadata: This is a seismic store specific field and describes how the physical data is stored in the cloud storage system (GCS/AzureContainer etc.). This metadata is mainly used by client libraries to correctly reconstruct the dataset. For example you can store a dataset as truncated in multiple objects of 64MB each, name them from 0 to N and save the filemetadata = “{nObject: N, totalSize: 1024, objsize: 64, sizeUnit: MB}”.
        gtags: Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then new gtags are appended to this list.
        ltag: Update the existing legalTag value.
        readonly: Update the dataset mode to readonly (true) or to read/write (false).
        status: Update the dataset status.

        NOTE: last_modified_date is updated automatically with each metadata change through Patch endpoint calling.


            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant.
                subprojectid (str): Name of the subproject.
                path (str): Hierarchical path of the dataset.
                datasetid (str): Name of the dataset.
                close (str): Non null sbit value of the dataset. Using this value here will close the dataset.
                dataset_new_name (str): New name for the dataset.
                metadata (dict): Generic information about the dataset stored as key value pairs.
                filemetadata (dict): Number of objects and the size in bytes of the dataset.
                last_modified_date (str): Date when the dataset was last modified.
                gtags (list[str]): Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.
                ltag (str): Legal tag associated with the dataset.
                readonly (bool): True if the dataset is read only.
                status (str): The status of the dataset (if set)
                seismicmeta (dict): Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.
                openzgy_v1 (dict):
                segy_v1 (dict):
                acls (dict): ACLs with admin groups and viewer groups for the dataset.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if path is not None:
            params["path"] = path
        if close is not None:
            params["close"] = close

        request_data = {}
        if dataset_new_name is not None:
            request_data["dataset_new_name"] = dataset_new_name
        if metadata is not None:
            request_data["metadata"] = metadata
        if filemetadata is not None:
            request_data["filemetadata"] = filemetadata
        if last_modified_date is not None:
            request_data["last_modified_date"] = last_modified_date
        if gtags is not None:
            request_data["gtags"] = gtags
        if ltag is not None:
            request_data["ltag"] = ltag
        if readonly is not None:
            request_data["readonly"] = readonly
        if status is not None:
            request_data["status"] = status
        if seismicmeta is not None:
            request_data["seismicmeta"] = seismicmeta
        if openzgy_v1 is not None:
            request_data["openzgy_v1"] = openzgy_v1
        if segy_v1 is not None:
            request_data["segy_v1"] = segy_v1
        if acls is not None:
            request_data["acls"] = acls

        if self.validation:
            validate_data(request_data, DatasetPatch)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/dataset/%s"
            % (tenantid, subprojectid, datasetid),
        )
        response = requests.patch(
            url, headers=headers, params=params, json=request_data
        )
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
        wid: int | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

          Open a dataset for read or write and lock its state.
          Required roles open lock for write:

              subproject.admin: if the applied subproject policy is 'uniform'
              dataset.admin: if the applied subproject policy is 'dataset'


          Required roles open lock for read:

              subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'
              dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'



        operationId: dataset-lock

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant.
                subprojectid (str): Name of the subproject.
                path (str): Hierarchical path of the dataset.
                datasetid (str): Name of the dataset.
                openmode (str): Type of the lock which can be set to 'read' (default) or 'write'.
                wid (int): Session identifier issued for a previous write lock acquisition operation.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        Removes the lock for a dataset id.
        Required roles:

            subproject.admin: if the applied subproject policy is 'uniform'
            dataset.admin: if the applied subproject policy is 'dataset'




          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
              tenantid (str): Name of the tenant.
              subprojectid (str): Name of the subproject.
              path (str): Hierarchical path for the dataset.
              datasetid (str): Name of the dataset.
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        Retrieve the access permission of a user on a dataset.
        Required roles:

            subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'
            dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'




          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
              tenantid (str): Name of the tenant.
              subprojectid (str): Name of the subproject.
              path (str): Hierarchical path for the dataset.
              datasetid (str): Name of the dataset.
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
        Check if the provided dataset cTag match the one stored in the metadata catalog.Required roles: subproject.admin, subproject.viewer
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            tenantid (str): Name of the tenant.
            subprojectid (str): Name of the subproject.
            path (str): Hierarchical path of the dataset.
            datasetid (str): Name of the dataset.
            ctag (str): Ctag to be validated.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        gtag: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.
        Required roles:

            subproject.admin: if the applied subproject policy is 'uniform'
            dataset.admin: if the applied subproject policy is 'dataset'




          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
              tenantid (str): Name of the tenant.
              subprojectid (str): Name of the subproject.
              path (str): Hierarchical path of the dataset.
              datasetid (str): Name of the dataset.
              gtag (list[str]): Gtags array list.
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        Compute and retrieve the size of a dataset and the date of when the size was computed.
        Required roles: subproject.admin

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant.
                subprojectid (str): Name of the subproject.
                datasetid (str): Name of the dataset.
                path (str): Hierarchical path of the dataset.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        Required roles: subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant.
                subprojectid (str): Name of the subproject.
                datasetid (str): Name of the dataset.
                path (str): Hierarchical path of the dataset.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        List datasets and sub-directories for a directory path.
        Required roles: subproject.admin, subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): The tenant project name.
                subprojectid (str): The sub-project name.
                path (str): The hierarchy path.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        translate_user_info: bool | None = None,
        type: str | None = None,
        gtags: list[str] | None = None,
        search: str | None = None,
        filter: dict | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.
        Required roles: subproject.admin, subproject.viewer


          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
              tenantid (str): Name of the tenant.
              subprojectid (str): Name of the subproject.
              translate_user_info (bool): translate the user-id to a more human readable user info
              type (str):
              gtags (list[str]): Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.
              search (str):
              filter (dict):
              limit (int): the maximum number of datasets in the response
              cursor (str): the cursor value required to retrieve the next page of result
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        params = {}
        if translate_user_info is not None:
            params["translate-user-info"] = translate_user_info

        request_data = {}
        if type is not None:
            request_data["type"] = type
        if gtags is not None:
            request_data["gtags"] = gtags
        if search is not None:
            request_data["search"] = search
        if filter is not None:
            request_data["filter"] = filter
        if limit is not None:
            request_data["limit"] = limit
        if cursor is not None:
            request_data["cursor"] = cursor

        if self.validation:
            validate_data(request_data, DatasetListBody)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def check_datasets_list(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        datasets: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Check if the dataset exists.
        Required roles: subproject.admin, subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant.
                subprojectid (str): Name of the subproject.
                datasets (list[str]): Array of datasets inside the subproject.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        request_data = {
            "datasets": datasets,
        }

        if self.validation:
            validate_data(request_data, DatasetCheckList)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/exist" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_datasets_sizes(
        self,
        *,
        impersonation_token_context: str | None = None,
        tenantid: str,
        subprojectid: str,
        datasets: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Return a list with the sizes of the requested datasets.
        The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.
        This API is deprecated, please using /size endpoint to compute and retrieve the size information
        Required roles: subproject.admin, subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                tenantid (str): Name of the tenant
                subprojectid (str): Name of the subproject.
                datasets (list[str]): Array of datasets inside the subproject.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        request_data = {
            "datasets": datasets,
        }

        if self.validation:
            validate_data(request_data, DatasetCheckList)

        url = urljoin(
            self.base_url,
            self.service_path,
            "dataset/tenant/%s/subproject/%s/sizes" % (tenantid, subprojectid),
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def ls(
        self,
        *,
        impersonation_token_context: str | None = None,
        sdpath: str,
        wmode: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Return the list of datasets and sub-directories of a seismic store path.
        Required roles: subproject.admin, subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                sdpath (str): Seismic store path, sd://tenant/sub-project/path.
                wmode (str): Working mode, dirs or datasets or undefined for both.
                limit (int): Limits the total number of datasets to return.
                cursor (str): Pagination token - this query parameter can be omitted on first call.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        impersonation_token_context: str | None = None,
        sdpath: str,
        wmode: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Return the list of datasets and sub-directories of a seismic store path.
        Required roles: subproject.admin, subproject.viewer

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                sdpath (str): the seismic dms path uri: sd://tenant or sd://tenant/subproject or sd://tenant/subproject/path.
                wmode (str): the endpoint working mode: dirs, datasets, all (default if not specified).
                limit (int): the max response datasets number.
                cursor (str): the next page cursor.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if impersonation_token_context is not None:
            headers["impersonation-token-context"] = impersonation_token_context

        request_data = {
            "sdpath": sdpath,
        }
        if wmode is not None:
            request_data["wmode"] = wmode
        if limit is not None:
            request_data["limit"] = limit
        if cursor is not None:
            request_data["cursor"] = cursor

        if self.validation:
            validate_data(request_data, DatasetLsBody)

        url = urljoin(self.base_url, self.service_path, "utility/ls")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_storage_tiers(self, data_partition_id: str | None = None) -> dict:
        """
        Return the list of storage tiers
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
        lock: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.
        Required roles:

            subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'
            dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'




            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
                sdpath_from (str): Seismic store source dataset path.
                sdpath_to (str): Seismic store destination dataset path.
                lock (bool): Lock source and destination while copying.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        readonly: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.
        Required roles:

            subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'
            dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'




          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
              sdpath (str): Seismic store path in the format sd://tenant/sub-project.
              readonly (bool): Readonly access, true(default) or false.
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
         Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). These credentials can be used via CSP SDK, on client side, to perform bulk upload.  The endpoint response is CSP (Cloud Solution Provider) dependent:  Azure: shared access signature (SaS) Url token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' }  Google: standard access token credential signed and down-scoped by google  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }  AWS: double column separated string containing access key id, the access key secret and the session token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }  IBM: double column separated string containing access key id, the access key secret and the session token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }    Required roles:  subproject.admin: if the applied subproject policy is 'uniform' dataset.admin: if the applied subproject policy is 'dataset'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            sdpath (str): Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
         Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). These credentials can be used via CSP SDK, on client side, to perform bulk download.  The endpoint response is CSP (Cloud Solution Provider) dependent:  Azure: shared access signature (SaS) Url token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' }  Google: standard access token credential signed and down-scoped by google  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }  AWS: double column separated string containing access key id, the access key secret and the session token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }  IBM: double column separated string containing access key id, the access key secret and the session token  { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' }    Required roles:  subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform' dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token_context (str): The impersonation token context (required only with impersonation token credentials)
            sdpath (str): Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """

        Generate an impersonation credential token of a user for a set of subproject resources.
        Required roles: app.trusted

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                token (str): Impersonation token that was previously issued.
                resources (list[dict]):
                refresh_url (str): A web service endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "token": token,
            "resources": resources,
            "refresh-url": refresh_url,
        }

        if self.validation:
            validate_data(request_data, ImpTokenRequest)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def refresh_imptoken(
        self, *, token: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Refresh an impersonation credential token.Required roles: none
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            token (str): Impersonation token
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "token": token,
        }

        if self.validation:
            validate_data(request_data, RefreshTokenRequest)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def patch_imptoken(
        self, *, token: str, refresh_url: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Patch an impersonation credential token's refresh url and generate a new impersonation token.
        Required roles: none

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                token (str): Impersonation token that was previously issued.
                refresh_url (str): New endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "token": token,
            "refresh-url": refresh_url,
        }

        if self.validation:
            validate_data(request_data, ImpTokenPatchRequest)

        url = urljoin(self.base_url, self.service_path, "imptoken")
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def create_impersonation_token(
        self,
        *,
        user_token: str,
        resources: list[dict],
        metadata: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Generate a credential token to impersonate user access for a set of subproject resources.Required roles: app.trusted
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            user_token (str): The credential of the user to impersonate.
            resources (list[dict]):
            metadata (dict): A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        headers.update(
            {
                "user-token": user_token,
            }
        )

        request_data = {
            "resources": resources,
        }
        if metadata is not None:
            request_data["metadata"] = metadata

        if self.validation:
            validate_data(request_data, ImpersonationTokenRequest)

        url = urljoin(self.base_url, self.service_path, "impersonation-token")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def refresh_impersonation_token(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Refresh an impersonation credential token.Required roles: app.trusted
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            impersonation_token (str): The impersonation token to refresh.
            impersonation_token_context (str): The impersonation token context.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        ltag: str | None = None,
        subprojectid: str,
        tenantid: str,
        admin: str | None = None,
        storage_class: str | None = None,
        storage_location: str | None = None,
        access_policy: str | None = "uniform",
        acls: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Creates a new subproject resource in seismic store.
        Required roles: users.datalake.admin

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                ltag (str): A valid compliance legal tag. It can be generated and managed via core-compliance-service.
                subprojectid (str): The subproject name. It must match the regex <b>^[a-z][a-z\d\-]*[a-z\d]$</b>
                tenantid (str): The tenant name - In OSDU this match the data-partition-id
                admin (str): An optional user to set as admin. The user will be added in the first admins acl group
                storage_class (str): Storage class for the bucket (Google Required Only)
                storage_location (str): Storage location for the bucket (Google Required Only)
                access_policy (str): The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)
                acls (dict): The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if ltag is not None:
            headers["ltag"] = ltag

        request_data = {}
        if admin is not None:
            request_data["admin"] = admin
        if storage_class is not None:
            request_data["storage_class"] = storage_class
        if storage_location is not None:
            request_data["storage_location"] = storage_location
        if access_policy is not None:
            request_data["access_policy"] = access_policy
        if acls is not None:
            request_data["acls"] = acls

        if self.validation:
            validate_data(request_data, SubProjectCreateBody)

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (subprojectid, tenantid),
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_subproject_metadata(
        self,
        *,
        subprojectid: str,
        tenantid: str,
        translate_user_info: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Return the metadata for a requested sub-project.Required roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            subprojectid (str): Name of the subproject.
            tenantid (str): Name of the tenant.
            translate_user_info (bool): translate the user-id to a more human readable user info
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
        self, *, subprojectid: str, tenantid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete a subproject in seismic store.Required roles: users.datalake.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            subprojectid (str): Name of the subproject.
            tenantid (str): Name of the tenant.
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
        ltag: str,
        tenantid: str,
        subprojectid: str,
        recursive: bool | None = None,
        access_policy: str | None = "dataset",
        acls: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Patch a subproject metadata in seismic store.
        Required roles: subproject.admin
        Possible actions:

          legal tag and/or ACLs groups can be patched by providing new values



          Args:
              data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
              ltag (str): Legal tag of the subproject.
              tenantid (str): Name of the tenant.
              subprojectid (str): Name of the subproject.
              recursive (bool): True if the legal tags of all datasets in a subproject needs to be updated.
              access_policy (str): Access Policy for the subproject.
              acls (dict): ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.
          Returns:
              response data (dict)
          Raises:
              OSDUValidation: if request values are wrong.
              OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        headers.update(
            {
                "ltag": ltag,
            }
        )

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        request_data = {}
        if access_policy is not None:
            request_data["access_policy"] = access_policy
        if acls is not None:
            request_data["acls"] = acls

        if self.validation:
            validate_data(request_data, SubProjectPatchBody)

        url = urljoin(
            self.base_url,
            self.service_path,
            "subproject/tenant/%s/subproject/%s" % (tenantid, subprojectid),
        )
        response = requests.patch(
            url, headers=headers, params=params, json=request_data
        )
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def list_subprojects_in_tenant(
        self, *, tenantid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Return the list of sub-projects in a tenant.Required roles: users.datalake.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            tenantid (str): Name of the tenant.
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
            self.base_url, self.service_path, "subproject/tenant/%s" % tenantid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_tenant(
        self,
        *,
        tenantid: str,
        gcpid: str,
        esd: str,
        default_acls: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Register a data partition in seismic-dms.Required roles: users.datalake.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            tenantid (str): Name of the tenant.
            gcpid (str): Google cloud project id associated with the tenant. For other providers, name of the data partition.
            esd (str): Entitlements group Sub Domain (ESD). For instance, if the entitlements group is users.datalake.viewers@{datapartition}.{domain}.com, the esd value is {datapartition}.{domain}.com. It must start with the name of the data partition.
            default_acls (str): Entitlements authorization group to manage tenant administrators.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "gcpid": gcpid,
            "esd": esd,
            "default_acls": default_acls,
        }

        if self.validation:
            validate_data(request_data, TenantCreateBody)

        url = urljoin(self.base_url, self.service_path, "tenant/%s" % tenantid)
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant(
        self, *, tenantid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Return the tenant metadata.Required roles: seistore.system.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            tenantid (str): Name of the tenant.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "tenant/%s" % tenantid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant_sdpath(
        self, *, datapartition: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Return the seistore path to a tenant associated with the data partition.Required roles: none
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            datapartition (str): Datapartition of the tenant.
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
            "datapartition": datapartition,
        }

        url = urljoin(self.base_url, self.service_path, "tenant/sdpath")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def update_user(
        self, *, email: str, path: str, group: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Add a user to a subproject default authorization group if it exists, otherwise, add the user to the first group.Required roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            email (str): Email address of the user. Note that this field is used as a principal identifier for entitlements-svc and can be configured using the env variable USER_ID_CLAIM_FOR_ENTITLEMENTS_SVC in the Seismic DMS runtime.
            path (str): Seismic store path in the format sd://tenant/subproject.
            group (str): Role to be assigned to the user.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "email": email,
            "path": path,
            "group": group,
        }

        if self.validation:
            validate_data(request_data, UserAddRequest)

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_user(self, *, sdpath: str, data_partition_id: str | None = None) -> dict:
        """
        List users in subproject's role-based authorization groups.Required roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            sdpath (str): Seismic store path, sd://tenant/sub-project.
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
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def delete_user(
        self, *, email: str, path: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Remove a user from subproject default authorization groups if exists, otherwise, remove it from the first authorization group.Required roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            email (str): Email of the user to remove.
            path (str): Path of the subproject.
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
            "email": email,
            "path": path,
        }

        url = urljoin(self.base_url, self.service_path, "user")
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_user_roles(
        self, *, sdpath: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Retrieve user role in all subprojects of the tenant.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            sdpath (str): Seismic store tenant path, sd://tenant.
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
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "user/roles")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def register_app(
        self, *, email: str, sdpath: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Register a new application in the seismic store.Required roles: users.datalake.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            email (str): Service account email of the application.
            sdpath (str): Seismic store tenant path, sd://tenant.
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
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_app(self, *, sdpath: str, data_partition_id: str | None = None) -> dict:
        """

        Retrieve the list of the registered applications in the seismic store.
        Required roles: users.datalake.admin

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                sdpath (str): Seismic store tenant path, sd://tenant.
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
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def set_app_trusted(
        self, *, email: str, sdpath: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Set a registered application as a trusted application in the seismic store.
        Required roles: users.datalake.admin

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                email (str): Service account email of the application.
                sdpath (str): Seismic store tenant path, sd://tenant.
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
            "email": email,
            "sdpath": sdpath,
        }

        url = urljoin(self.base_url, self.service_path, "app/trusted")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_app_trusted(
        self, *, sdpath: str, data_partition_id: str | None = None
    ) -> dict:
        """

        Return the list of the trusted application in seismic store tenant.
        Required roles: users.datalake.admin

            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                sdpath (str): Seismic store tenant path in the format sd://tenant.
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
        path: str,
        filter: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
         Description: delete all datasets in the specified sdms subproject path. Roles: subproject.admin
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            path (str): The sdms subproject path as sd://tenant/subproject/(path) <ul> <li>The sdms subproject path must end with '/' as sd://tenant/subproject/a/b/c/</li> <li>The dataset must end with dataset name as sd://tenant/subproject/a/b/c/dataset</li> </ul>
            filter (dict): Optional structured query filter to restrict the datasets to be deleted.
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
            "path": path,
        }

        request_data = {}
        if filter is not None:
            request_data["filter"] = filter

        if self.validation:
            validate_data(request_data, DatasetBulkDeleteBody)

        url = urljoin(self.base_url, self.service_path, "operation/bulk-delete")
        response = requests.put(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()

    def get_operation_bulk_delete_status(
        self, *, operation_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
         Description: get the bulk delete operation status. Roles: any (registered user in partition)
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            operation_id (str): The bulk delete operation id
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
            self.base_url, self.service_path, "operation/bulk-delete/%s" % operation_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(response.text, response.status_code)
        return response.json()
