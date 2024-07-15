from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.rafs.common import RAFSCommonClient
from osdu_client.utils import urljoin


class RAFSAPIError(OSDUAPIError):
    pass


class RAFSClient(RAFSCommonClient):
    service_path = ""

    def get_sar_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
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
