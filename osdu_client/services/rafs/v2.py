from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.rafs.common import RAFSCommonClient


class RAFSAPIError(OSDUAPIError):
    pass


class RAFSClient(RAFSCommonClient):
    service_path = ""

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
            "api/rafs-ddms/v2/samplesanalysesreport/%s" % record_id,
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
            "api/rafs-ddms/v2/samplesanalysesreport/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sar_record_versions(
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
            "api/rafs-ddms/v2/samplesanalysesreport/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sar_record_specific_version(
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
            "api/rafs-ddms/v2/samplesanalysesreport/%s/versions/%s"
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
            self.base_url, self.service_path, "api/rafs-ddms/v2/samplesanalysesreport"
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
            "api/rafs-ddms/v2/samplesanalysesreport/%s/source" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_types(self, data_partition_id: str | None = None) -> dict:
        """
        Get available types.
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
            "api/rafs-ddms/v2/samplesanalysis/analysistypes",
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `SamplesAnalysis` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/samplesanalysis/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_sa_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `SamplesAnalysis` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/samplesanalysis/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `SamplesAnalysis` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/samplesanalysis/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `SamplesAnalysis` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/samplesanalysis/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_sa_records(self, data_partition_id: str | None = None) -> dict:
        """
        Create or update `SamplesAnalysis` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            self.base_url, self.service_path, "api/rafs-ddms/v2/samplesanalysis"
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_content_schema(
        self, *, analysistype: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the (`content schema`) for a given `{analysistype}`.                 Use the `Accept` request header to specify content schema version                     (example header `Accept: application/json;version=1.0.0` is supported).        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            analysistype (str):
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
            "api/rafs-ddms/v2/samplesanalysis/%s/data/schema" % analysistype,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_sa_data(
        self,
        *,
        record_id: str,
        analysis_type: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `{analysis_type}` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            analysis_type (str):
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
            "api/rafs-ddms/v2/samplesanalysis/%s/data/%s/%s"
            % (record_id, analysis_type, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_sa_data(
        self,
        *,
        record_id: str,
        analysis_type: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Upload the bulk data for a given `{analysis_type}` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            analysis_type (str):
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
            "api/rafs-ddms/v2/samplesanalysis/%s/data/%s" % (record_id, analysis_type),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def search_sa_data(
        self,
        *,
        analysis_type: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`queried`) bulk data from every `{analysis_type}` found in search service.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            analysis_type (str):
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
            "api/rafs-ddms/v2/samplesanalysis/%s/search/data" % analysis_type,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def query_sa(
        self,
        *,
        analysis_type: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`samples analysis`) ids list that comply with `{query}` for given`{analysis_type}`.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            analysis_type (str):
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
            "api/rafs-ddms/v2/samplesanalysis/%s/search" % analysis_type,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_masterdata_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `(osdu:wks:master-data--GenericFacility:1.0.0|osdu:wks:master-data--GenericSite:1.0.0|osdu:wks:master-data--Sample:2.0.0|osdu:wks:master-data--SampleAcquisitionJob:1.0.0|osdu:wks:master-data--SampleChainOfCustodyEvent:1.0.0|osdu:wks:master-data--SampleContainer:1.0.0)` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/masterdata/%s" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_masterdata_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `(osdu:wks:master-data--GenericFacility:1.0.0|osdu:wks:master-data--GenericSite:1.0.0|osdu:wks:master-data--Sample:2.0.0|osdu:wks:master-data--SampleAcquisitionJob:1.0.0|osdu:wks:master-data--SampleChainOfCustodyEvent:1.0.0|osdu:wks:master-data--SampleContainer:1.0.0)` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/masterdata/%s" % record_id,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_masterdata_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `(osdu:wks:master-data--GenericFacility:1.0.0|osdu:wks:master-data--GenericSite:1.0.0|osdu:wks:master-data--Sample:2.0.0|osdu:wks:master-data--SampleAcquisitionJob:1.0.0|osdu:wks:master-data--SampleChainOfCustodyEvent:1.0.0|osdu:wks:master-data--SampleContainer:1.0.0)` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/masterdata/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_masterdata_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `(osdu:wks:master-data--GenericFacility:1.0.0|osdu:wks:master-data--GenericSite:1.0.0|osdu:wks:master-data--Sample:2.0.0|osdu:wks:master-data--SampleAcquisitionJob:1.0.0|osdu:wks:master-data--SampleChainOfCustodyEvent:1.0.0|osdu:wks:master-data--SampleContainer:1.0.0)` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/masterdata/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_masterdata_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `(osdu:wks:master-data--GenericFacility:1.0.0|osdu:wks:master-data--GenericSite:1.0.0|osdu:wks:master-data--Sample:2.0.0|osdu:wks:master-data--SampleAcquisitionJob:1.0.0|osdu:wks:master-data--SampleChainOfCustodyEvent:1.0.0|osdu:wks:master-data--SampleContainer:1.0.0)` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/v2/masterdata")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the latest version of `(rafsddms:wks:work-product-component--MultiPhaseFlowMeterCalibration:1.0.0|rafsddms:wks:work-product-component--PVTModel:1.0.0|rafsddms:wks:work-product-component--ComponentScenario:1.0.0|rafsddms:wks:work-product-component--BlackOilTable:1.0.0)` object by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            self.base_url, self.service_path, "api/rafs-ddms/v2/pvtmodel/%s" % record_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def soft_delete_pvt_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Delete the `(rafsddms:wks:work-product-component--MultiPhaseFlowMeterCalibration:1.0.0|rafsddms:wks:work-product-component--PVTModel:1.0.0|rafsddms:wks:work-product-component--ComponentScenario:1.0.0|rafsddms:wks:work-product-component--BlackOilTable:1.0.0)` object by record id.        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            self.base_url, self.service_path, "api/rafs-ddms/v2/pvtmodel/%s" % record_id
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record_versions(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get a list of `(rafsddms:wks:work-product-component--MultiPhaseFlowMeterCalibration:1.0.0|rafsddms:wks:work-product-component--PVTModel:1.0.0|rafsddms:wks:work-product-component--ComponentScenario:1.0.0|rafsddms:wks:work-product-component--BlackOilTable:1.0.0)` object versions by record id.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/pvtmodel/%s/versions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_record_version(
        self, *, version: str, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Get the given version of `(rafsddms:wks:work-product-component--MultiPhaseFlowMeterCalibration:1.0.0|rafsddms:wks:work-product-component--PVTModel:1.0.0|rafsddms:wks:work-product-component--ComponentScenario:1.0.0|rafsddms:wks:work-product-component--BlackOilTable:1.0.0)` object.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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
            "api/rafs-ddms/v2/pvtmodel/%s/versions/%s" % (version, record_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_pvt_records(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Create or update `(rafsddms:wks:work-product-component--MultiPhaseFlowMeterCalibration:1.0.0|rafsddms:wks:work-product-component--PVTModel:1.0.0|rafsddms:wks:work-product-component--ComponentScenario:1.0.0|rafsddms:wks:work-product-component--BlackOilTable:1.0.0)` record(s).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
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

        url = urljoin(self.base_url, self.service_path, "api/rafs-ddms/v2/pvtmodel")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def get_pvt_data(
        self,
        *,
        record_id: str,
        analysis_type: str,
        dataset_id: str,
        columns_filter: str | None = None,
        rows_filter: str | None = None,
        columns_aggregation: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Get the (`latest version`) bulk data for a given `{analysis_type}` object by record id.             Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).            The  `columns_filter`, `rows_filter`, and  `columns_aggregation`                 query parameters can be used to manage data in response.        Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            analysis_type (str):
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
            "api/rafs-ddms/v2/pvtmodel/%s/data/%s/%s"
            % (record_id, analysis_type, dataset_id),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()

    def upload_pvt_data(
        self,
        *,
        record_id: str,
        analysis_type: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Upload the bulk data for a given `{analysis_type}` object by record id.            It creates a new version of the record.             The previous meta-data with bulk data is available by their `versions`.              Use the `Content-Type` request header to specify payload and response formats                 (`application/json` and `application/parquet` are supported).            Use the `Accept` request header to specify content schema version                 (example header `Accept: */*;version=1.0.0` is supported).        Required roles: `users.datalake.editors` or `users.datalake.admins`.         In addition, users must be members of a data group(ACL) to access the data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            analysis_type (str):
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
            "api/rafs-ddms/v2/pvtmodel/%s/data/%s" % (record_id, analysis_type),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise RAFSAPIError(response.text, response.status_code)
        return response.json()
