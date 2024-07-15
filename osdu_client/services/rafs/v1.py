from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.rafs.common import RAFSCommonClient
from osdu_client.utils import urljoin


class RAFSAPIError(OSDUAPIError):
    pass


class RAFSClient(RAFSCommonClient):
    service_path = ""

    def get_rock_sample_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `RockSampleAnalysis` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/rocksampleanalyses/%s/rca/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_rock_sample_analysis_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `RockSampleAnalysis` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksampleanalyses/%s/rca/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rock_sample_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/rocksampleanalyses/%s/rca/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rock_sample_analysis_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `RockSampleAnalysis` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksampleanalyses/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_rock_sample_analysis_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `RockSampleAnalysis` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksampleanalyses/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_rock_sample_analysis_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `RockSampleAnalysis` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksampleanalyses/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_rock_sample_analysis_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `RockSampleAnalysis` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/rocksampleanalyses/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_rock_sample_analysis_record(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `RockSampleAnalysis` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/rocksampleanalyses"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_coring_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `Coring` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/coringreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_coring_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `Coring` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/coringreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_coring_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `Coring` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/coringreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_coring_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `Coring` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/coringreports/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_coring_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `Coring` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/coringreports"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rock_sample_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `RockSample` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksamples/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_rock_sample_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `RockSample` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksamples/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rock_sample_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `RockSample` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rocksamples/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rock_sample_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `RockSample` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/rocksamples/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_rock_sample_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `RockSample` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/v1/rocksamples")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `PVT` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/pvtreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_pvt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `PVT` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/pvtreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `PVT` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/pvtreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `PVT` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/pvtreports/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_pvt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `PVT` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/v1/pvtreports")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/pvtreports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cce_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `ConstantCompositionExpansionTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/ccereports/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_cce_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `ConstantCompositionExpansionTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/ccereports/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cce_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/ccereports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cce_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `ConstantCompositionExpansionTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/ccereports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_cce_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `ConstantCompositionExpansionTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/ccereports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cce_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `ConstantCompositionExpansionTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/ccereports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cce_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `ConstantCompositionExpansionTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/ccereports/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_cce_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `ConstantCompositionExpansionTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/v1/ccereports")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_difflib_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `DifferentialLiberationTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/difflibreports/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_difflib_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `DifferentialLiberationTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/difflibreports/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_difflib_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/difflibreports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_difflib_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `DifferentialLiberationTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/difflibreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_difflib_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `DifferentialLiberationTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/difflibreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_difflib_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `DifferentialLiberationTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/difflibreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_difflib_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `DifferentialLiberationTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/difflibreports/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_difflib_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `DifferentialLiberationTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/difflibreports"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_transporttest_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `TransportTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/transporttests/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_transporttest_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `TransportTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/transporttests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_transporttest_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/transporttests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_transporttest_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `TransportTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/transporttests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_transporttest_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `TransportTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/transporttests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_transporttest_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `TransportTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/transporttests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_transporttest_record_specific_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `TransportTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/transporttests/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_transporttest_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `TransportTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/transporttests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_compositionalanalysis_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `CompositionAnalysisTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/compositionalanalysisreports/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_compositionalanalysis_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `CompositionAnalysisTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/compositionalanalysisreports/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_compositionalanalysis_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/compositionalanalysisreports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_compositionalanalysis_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `CompositionAnalysisTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/compositionalanalysisreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_compositionalanalysis_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `CompositionAnalysisTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/compositionalanalysisreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_compositionalanalysis_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `CompositionAnalysisTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/compositionalanalysisreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_compositionalanalysis_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `CompositionAnalysisTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/compositionalanalysisreports/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_compositionalanalysis_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `CompositionAnalysisTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/compositionalanalysisreports",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_multistageseparatortests_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `MultiStageSeparatorTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multistageseparatortests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_multistageseparatortests_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `MultiStageSeparatorTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multistageseparatortests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_multistageseparatortests_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multistageseparatortests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_multistageseparatortests_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `MultiStageSeparatorTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multistageseparatortests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_multistageseparatortests_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `MultiStageSeparatorTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multistageseparatortests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_multistageseparatortests_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `MultiStageSeparatorTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multistageseparatortests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_multistageseparatortests_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `MultiStageSeparatorTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/multistageseparatortests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def post_multistageseparatortests_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `MultiStageSeparatorTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multistageseparatortests",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_swellingtests_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `SwellingTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/swellingtests/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_swellingtests_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `SwellingTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/swellingtests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_swellingtests_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/swellingtests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_swellingtests_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `SwellingTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/swellingtests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_swellingtests_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `SwellingTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/swellingtests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_swellingtests_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `SwellingTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/swellingtests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_swellingtests_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `SwellingTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/swellingtests/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_swellingtests_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `SwellingTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/swellingtests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cvdt_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `ConstantVolumeDepletionTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_cvdt_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `ConstantVolumeDepletionTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cvdt_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cvdt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `ConstantVolumeDepletionTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_cvdt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `ConstantVolumeDepletionTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cvdt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `ConstantVolumeDepletionTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cvdt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `ConstantVolumeDepletionTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/constantvolumedepletiontests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_cvdt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `ConstantVolumeDepletionTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/constantvolumedepletiontests",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wat_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `WaterAnalysisTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/wateranalysisreports/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_wat_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `WaterAnalysisTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/wateranalysisreports/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wat_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/wateranalysisreports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wat_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `WaterAnalysisTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/wateranalysisreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_wat_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `WaterAnalysisTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/wateranalysisreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wat_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `WaterAnalysisTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/wateranalysisreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wat_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `WaterAnalysisTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/wateranalysisreports/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wat_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `WaterAnalysisTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/wateranalysisreports"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stoat_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `StockTankOilAnalysisTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_stoat_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `StockTankOilAnalysisTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stoat_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stoat_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `StockTankOilAnalysisTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_stoat_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `StockTankOilAnalysisTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_stoat_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `StockTankOilAnalysisTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stoat_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `StockTankOilAnalysisTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/stocktankoilanalysisreports/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_stoat_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `StockTankOilAnalysisTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/stocktankoilanalysisreports",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_itt_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `InterfacialTensionTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/interfacialtensiontests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_itt_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `InterfacialTensionTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/interfacialtensiontests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_itt_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/interfacialtensiontests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_itt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `InterfacialTensionTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/interfacialtensiontests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_itt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `InterfacialTensionTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/interfacialtensiontests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_itt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `InterfacialTensionTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/interfacialtensiontests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_itt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `InterfacialTensionTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/interfacialtensiontests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_itt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `InterfacialTensionTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/interfacialtensiontests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_vlet_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `VaporLiquidEquilibriumTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_vlet_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `VaporLiquidEquilibriumTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_vlet_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_vlet_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `VaporLiquidEquilibriumTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_vlet_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `VaporLiquidEquilibriumTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_vlet_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `VaporLiquidEquilibriumTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_vlet_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `VaporLiquidEquilibriumTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/vaporliquidequilibriumtests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_vlet_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `VaporLiquidEquilibriumTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/vaporliquidequilibriumtests",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_mcmt_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `MultipleContactMiscibilityTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_mcmt_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `MultipleContactMiscibilityTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_mcmt_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_mcmt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `MultipleContactMiscibilityTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_mcmt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `MultipleContactMiscibilityTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_mcmt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `MultipleContactMiscibilityTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_mcmt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `MultipleContactMiscibilityTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_mcmt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `MultipleContactMiscibilityTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/multiplecontactmiscibilitytests",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stt_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `SlimTubeTest` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/slimtubetests/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_stt_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `SlimTubeTest` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/slimtubetests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stt_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/slimtubetests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `SlimTubeTest` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/slimtubetests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_stt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `SlimTubeTest` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/slimtubetests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `SlimTubeTest` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/slimtubetests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_stt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `SlimTubeTest` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/slimtubetests/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_stt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `SlimTubeTest` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/slimtubetests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sar_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `SamplesAnalysesReport` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/samplesanalysesreport/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_sar_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `SamplesAnalysesReport` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/samplesanalysesreport/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_sar_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `SamplesAnalysesReport` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/samplesanalysesreport/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sar_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `SamplesAnalysesReport` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/samplesanalysesreport/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_sar_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `SamplesAnalysesReport` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/samplesanalysesreport"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sar_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/samplesanalysesreport/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cp_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `CapPressure` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/capillarypressuretests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_cp_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `CapPressure` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/capillarypressuretests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cp_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/capillarypressuretests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `CapPressure` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/capillarypressuretests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_cp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `CapPressure` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/capillarypressuretests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cp_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `CapPressure` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/capillarypressuretests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_cp_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `CapPressure` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/capillarypressuretests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_cp_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `CapPressure` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/capillarypressuretests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `RelativePermeability` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/relativepermeabilitytests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_rp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `RelativePermeability` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/relativepermeabilitytests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rp_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `RelativePermeability` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/relativepermeabilitytests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rp_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `RelativePermeability` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/relativepermeabilitytests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_rp_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `RelativePermeability` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/relativepermeabilitytests",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rp_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `RelativePermeability` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/relativepermeabilitytests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_rp_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `RelativePermeability` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/relativepermeabilitytests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rp_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/relativepermeabilitytests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ft_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `Fractionation` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/fractionationtests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_ft_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `Fractionation` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/fractionationtests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ft_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `Fractionation` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/fractionationtests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ft_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `Fractionation` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/fractionationtests/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_ft_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `Fractionation` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/fractionationtests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ft_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `Fractionation` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/fractionationtests/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_ft_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `Fractionation` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/fractionationtests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ft_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/fractionationtests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_et_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `Extraction` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/extractiontests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_et_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `Extraction` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/extractiontests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_et_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `Extraction` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/extractiontests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_et_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `Extraction` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/extractiontests/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_er_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `Extraction` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/extractiontests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_et_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `Extraction` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/extractiontests/%s/data/%s" % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_et_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `Extraction` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/extractiontests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_et_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/extractiontests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_physchem_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `PhysChem` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/physicalchemistrytests/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_physchem_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `PhysChem` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/physicalchemistrytests/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_physchem_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `PhysChem` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/physicalchemistrytests/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_physchem_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `PhysChem` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/physicalchemistrytests/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_physchem_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `PhysChem` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/physicalchemistrytests"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_physchem_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `PhysChem` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/physicalchemistrytests/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_physchem_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `PhysChem` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/physicalchemistrytests/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_physchem_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/physicalchemistrytests/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ep_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `ElectricalProperties` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/electricalproperties/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_ep_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `ElectricalProperties` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/electricalproperties/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ep_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `ElectricalProperties` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/electricalproperties/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ep_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `ElectricalProperties` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/electricalproperties/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_ep_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `ElectricalProperties` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/electricalproperties"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ep_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `ElectricalProperties` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/electricalproperties/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_ep_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `ElectricalProperties` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/electricalproperties/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_ep_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/electricalproperties/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rc_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `RockCompressibility` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rockcompressibilities/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_rc_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `RockCompressibility` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rockcompressibilities/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_record_rc_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `RockCompressibility` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rockcompressibilities/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rc_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `RockCompressibility` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/rockcompressibilities/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_rc_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `RockCompressibility` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url, self.service_path, "api/rafs-ddms/v1/rockcompressibilities"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rc_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `RockCompressibility` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/rockcompressibilities/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_rc_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `RockCompressibility` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/rockcompressibilities/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_rc_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/rockcompressibilities/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wgrp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `WaterGasRelativePermeability` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_wgrp_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `WaterGasRelativePermeability` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wgrp_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `WaterGasRelativePermeability` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wgrp_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `WaterGasRelativePermeability` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wgrp_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `WaterGasRelativePermeability` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/watergasrelativepermeabilities",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wgrp_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `WaterGasRelativePermeability` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_wgrp_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `WaterGasRelativePermeability` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_wgrp_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/watergasrelativepermeabilities/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_fri_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `FormationResistivityIndex` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/formationresistivityindexes/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_fri_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `FormationResistivityIndex` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/formationresistivityindexes/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_fri_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `FormationResistivityIndex` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/formationresistivityindexes/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_fri_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `FormationResistivityIndex` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            version (str):
            record_id (str):
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
            "api/rafs-ddms/v1/formationresistivityindexes/%s/versions/%s"
            % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_fri_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `FormationResistivityIndex` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/formationresistivityindexes",
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_fri_data(
        self,
        *,
        record_id: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `FormationResistivityIndex` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            dataset_id (str):
            columns_filter (str):
            rows_filter (str):
            columns_aggregation (str):
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
        if columns_filter is not None:
            params["columns_filter"] = columns_filter
        if rows_filter is not None:
            params["rows_filter"] = rows_filter
        if columns_aggregation is not None:
            params["columns_aggregation"] = columns_aggregation

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/formationresistivityindexes/%s/data/%s"
            % (record_id, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_fri_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Upload the bulk data for a given `FormationResistivityIndex` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
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
            "api/rafs-ddms/v1/formationresistivityindexes/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_fri_source_data(
        self,
        *,
        record_id: str,
        version: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Get source data from data.Datasets property.

        :param record_id: record id
        :type record_id: str
        :param storage_service: storage service, defaults to
            Depends(get_async_storage_service)
        :type storage_service: dataset.DatasetService, optional
        :param dataset_service: dataset service, defaults to
            Depends(get_async_dataset_service)
        :type dataset_service: storage.StorageService, optional
        :param version: version, defaults to None
        :type version: Optional[str], optional
        :return: rendered source data response
        :rtype: JSONResponse
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
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
        if version is not None:
            params["version"] = version

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/rafs-ddms/v1/formationresistivityindexes/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()
