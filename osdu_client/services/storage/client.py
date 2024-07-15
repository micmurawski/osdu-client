from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CopyRecordReferencesModel, MultiRecordIds, MultiRecordRequest, RecordBulkUpdateParam, ReplayRequest


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
    ) -> dict:
        """
            The API represents the main injection mechanism into the Data Ecosystem.
        It allows records creation and/or update.When no record id is provided or when the provided id is not already present in the Data Ecosystem then a new record is created.
         If the id is related to an existing record in the Data Ecosystem then an update operation takes place and a new version of the record is created.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                skipdupes (str): Skip duplicates when updating records with the same value.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        x_collaboration: str | None = None,
        query: dict,
        ops: list[dict],
        data_partition_id: str | None = None,
    ) -> dict:
        """
            The API represents the patch update mechanism for records. It allows updating multiple records in one request. The API supports metadata update only (Legal Tags, ACLs and Tags) if the request body media type is `application/json`. The API supports metadata and data update (Legal Tags, ACLs, Tags, Ancestry, Kind, Meta and Data) if the request body media type is `application/json-patch+json`. Please choose the appropriate media type from the Request body dropdown. The currently supported operations are replace, add, and remove.
        Required roles: `users.datalake.editors` or `users.datalake.admins`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                query (dict):
                ops (list[dict]):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        request_data = {
            "query": query,
            "ops": ops,
        }

        if self.validation:
            validate_data(request_data, RecordBulkUpdateParam)

        url = urljoin(self.base_url, self.service_path, "records")
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def update_records_copy(
        self,
        *,
        x_collaboration: str | None = None,
        target: str | None = None,
        records: list[dict] | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        This API attempts to copy all the Record references it is provided from the given source namespace to the target namespace. All refences will be copied or all will fail as a transaction. IF the target namesapce does not et exist it will be created. It requires 'services.storage.admin' permission to call
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            x_collaboration (str): x-collaboration
            target (str):
            records (list[dict]):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        request_data = {}
        if target is not None:
            request_data["target"] = target
        if records is not None:
            request_data["records"] = records

        if self.validation:
            validate_data(request_data, CopyRecordReferencesModel)

        url = urljoin(self.base_url, self.service_path, "records/copy")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def delete_record(
        self,
        *,
        x_collaboration: str | None = None,
        id: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            The API performs a logical deletion of the record using recordId. This operation can be reverted later.
        Allowed roles: `service.storage.creator` and `service.storage.admin` who is the OWNER of the record.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                id (str): Record id
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            The API performs a soft deletion of the given list of records.
        Required roles: `users.datalake.editors` or `users.datalake.admins` who is the OWNER of the record.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            The API returns a list of all record ids which belong to the specified kind.
        Allowed roles: `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                cursor (str): Cursor
                limit (str): Page Size
                kind (str): Filter Kind
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        x_collaboration: str | None = None,
        records: list[str],
        attributes: list[str] | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            The API fetches multiple records at once.
        Allowed roles: `service.storage.viewer`,`service.storage.creator` and `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                records (list[str]):
                attributes (list[str]):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        request_data = {
            "records": records,
        }
        if attributes is not None:
            request_data["attributes"] = attributes

        if self.validation:
            validate_data(request_data, MultiRecordIds)

        url = urljoin(self.base_url, self.service_path, "query/records")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def query_records_batch(
        self,
        *,
        x_collaboration: str | None = None,
        frame_of_reference: str,
        records: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """
            The API fetches multiple records at once in the specific {data-partition-id}.The value of {frame-of-reference} indicates whether normalization is applied.
        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                frame_of_reference (str): This value indicates whether normalization applies, should be either `none` or `units=SI;crs=wgs84;elevation=msl;azimuth=true north;dates=utc;`
                records (list[str]):
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
                "frame-of-reference": frame_of_reference,
            }
        )
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        request_data = {
            "records": records,
        }

        if self.validation:
            validate_data(request_data, MultiRecordRequest)

        url = urljoin(self.base_url, self.service_path, "query/records:batch")
        response = requests.post(url, headers=headers, json=request_data)
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
    ) -> dict:
        """
            This API returns the latest version of the given record.
        Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                id (str): Record id
                attribute (str): Filter attributes to restrict the returned fields of the record.  Usage: data.{record-data-field-name}.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            The API performs the physical deletion of the given record and all of its versions.
         This operation cannot be undone.
        Allowed roles: `service.storage.admin` who is the OWNER of the record.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                id (str): Record id
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            The API retrieves the specific version of the given record.
        Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                id (str): Record id
                version (str): Record version
                attribute (str): Filter attributes to restrict the returned fields of the record.  Usage: data.{record-data-field-name}.
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            The API returns a list containing all versions for the given record id.
        Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                x_collaboration (str): x-collaboration
                id (str): Record id
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if x_collaboration is not None:
            headers["x-collaboration"] = x_collaboration

        url = urljoin(self.base_url, self.service_path, "records/versions/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint verifies the operational status of the Storage Service.
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

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/info` endpoint, which provides build and git related information.
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
    ) -> dict:
        """
           The API for the given record id, performs the permanent deletion of physical record versions excluding latest version. `versionIds`, `limit`, `from` query parameters used to delete the record versions.
        `versionIds` comma separated value of version ids can be provided on `versionIds` query parameter. API will delete all versions defined by 'versionIds' query parameter. Maximum 50 record versions can be deleted per request. If `limit` query parameter ONLY is used, then it will delete oldest versions defined by `limit`. If `from` query parameter is used then it will delete all versions before current one (exclusive). `versionIds` explicit version should always take precedence than `limit` & `from` query parameter If both `from` and `limit` are used then API will delete `limit` number of versions starting `from` version This operation cannot be undone. Required roles: `users.datalake.admins` who is the OWNER of the record.
           Args:
               data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
               x_collaboration (str): x-collaboration
               id (str): Record id
               version_ids (str): Comma separated version ids (excluding latest version) to be deleted. Maximum 50 versions can be deleted per request.
               limit (str): limit
               _form (str): Record version id from which all record versions aside from the current one are deleted
           Returns:
               response data (dict)
           Raises:
               OSDUValidation: if request values are wrong.
               OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        self, *, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
            By passing replayId , you can get the replay operation status.
        Allowed roles: `users.datalake.ops`
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                id (str): replayId
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "replay/status/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def create_replay(
        self,
        *,
        operation: str,
        filter: list[str] | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Replay all the kinds. Allowed roles `users.datalake.ops`
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            operation (str):
            filter (list[str]):
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
            "operation": operation,
        }
        if filter is not None:
            request_data["filter"] = filter

        if self.validation:
            validate_data(request_data, ReplayRequest)

        url = urljoin(self.base_url, self.service_path, "replay")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def get_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def update_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def create_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def delete_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def options_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.options(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def head_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.head(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()

    def patch_whoami(self, data_partition_id: str | None = None) -> dict:
        """

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

        url = urljoin(self.base_url, self.service_path, "whoami")
        response = requests.patch(url, headers=headers)
        if not response.ok:
            raise StorageAPIError(response.text, response.status_code)
        return response.json()
