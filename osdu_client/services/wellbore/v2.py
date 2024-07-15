from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.wellbore.common import WellboreCommonClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CreateDataSessionRequest, Dip, UpdateSessionState


class WellboreAPIError(OSDUAPIError):
    pass


class WellboreClient(WellboreCommonClient):
    service_path = ""

    def get_alpha_logs_data(
        self,
        *,
        record_id: str,
        offset: str | None = None,
        limit: str | None = None,
        curves: str | None = None,
        describe: str | None = None,
        filter: str | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if curves is not None:
            params["curves"] = curves
        if describe is not None:
            params["describe"] = describe
        if filter is not None:
            params["filter"] = filter
        if orient is not None:
            params["orient"] = orient

        url = urljoin(
            self.base_url, self.service_path, "alpha/ddms/v2/logs/%s/data" % record_id
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def write_alpha_logs_data(
        self,
        *,
        record_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "alpha/ddms/v2/logs/%s/data" % record_id
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def list_records_sessions_v2(
        self,
        *,
        record_id: str,
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
            "alpha/ddms/v2/logs/%s/sessions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_alpha_logs_sessions(
        self,
        *,
        mode: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
        record_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        request_data = {
            "mode": mode,
        }
        if from_version is not None:
            request_data["fromVersion"] = from_version
        if meta is not None:
            request_data["meta"] = meta
        if time_to_live is not None:
            request_data["timeToLive"] = time_to_live

        if self.validation:
            validate_data(request_data, CreateDataSessionRequest, WellboreAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "alpha/ddms/v2/logs/%s/sessions" % record_id,
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_record_session_v2(
        self,
        *,
        record_id: str,
        session_id: str,
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
            "alpha/ddms/v2/logs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def patch_alpha_logs_sessions(
        self,
        *,
        state: str,
        record_id: str,
        session_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        request_data = {
            "state": state,
        }

        if self.validation:
            validate_data(request_data, UpdateSessionState, WellboreAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "alpha/ddms/v2/logs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def send_alpha_logs_sessions_data(
        self,
        *,
        record_id: str,
        session_id: str,
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
            "alpha/ddms/v2/logs/%s/sessions/%s/data" % (record_id, session_id),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_alpha_logs_versions_data(
        self,
        *,
        record_id: str,
        version: str,
        offset: str | None = None,
        limit: str | None = None,
        curves: str | None = None,
        describe: str | None = None,
        filter: str | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if curves is not None:
            params["curves"] = curves
        if describe is not None:
            params["describe"] = describe
        if filter is not None:
            params["filter"] = filter
        if orient is not None:
            params["orient"] = orient

        url = urljoin(
            self.base_url,
            self.service_path,
            "alpha/ddms/v2/logs/%s/versions/%s/data" % (record_id, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_dipset(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_dipset(
        self,
        *,
        dipsetid: str,
        recursive: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets/%s" % dipsetid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dipset(
        self,
        *,
        dipsetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets/%s" % dipsetid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dip(
        self,
        *,
        dipsetid: str,
        index: str | None = None,
        limit: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if index is not None:
            params["index"] = index
        if limit is not None:
            params["limit"] = limit

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/dips" % dipsetid
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def define_dips_dipset(
        self,
        *,
        dipsetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/dips" % dipsetid
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def insert_dip_in_dipset(
        self,
        *,
        dipsetid: str,
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
            "ddms/v2/dipsets/%s/dips/insert" % dipsetid,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def query_dip_from_dipset(
        self,
        *,
        dipsetid: str,
        min_reference: str | None = None,
        max_reference: str | None = None,
        classification: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if min_reference is not None:
            params["minReference"] = min_reference
        if max_reference is not None:
            params["maxReference"] = max_reference
        if classification is not None:
            params["classification"] = classification

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/dips/query" % dipsetid
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_dip(
        self,
        *,
        dipsetid: str,
        index: str,
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
            "ddms/v2/dipsets/%s/dips/%s" % (dipsetid, index),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dip_at_index(
        self,
        *,
        dipsetid: str,
        index: str,
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
            "ddms/v2/dipsets/%s/dips/%s" % (dipsetid, index),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def update_dip(
        self,
        *,
        azimuth: dict,
        inclination: dict,
        reference: dict,
        classification: str | None = None,
        quality: dict | None = None,
        x_coordinate: dict | None = None,
        y_coordinate: dict | None = None,
        z_coordinate: dict | None = None,
        dipsetid: str,
        index: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        request_data = {
            "azimuth": azimuth,
            "inclination": inclination,
            "reference": reference,
        }
        if classification is not None:
            request_data["classification"] = classification
        if quality is not None:
            request_data["quality"] = quality
        if x_coordinate is not None:
            request_data["xCoordinate"] = x_coordinate
        if y_coordinate is not None:
            request_data["yCoordinate"] = y_coordinate
        if z_coordinate is not None:
            request_data["zCoordinate"] = z_coordinate

        if self.validation:
            validate_data(request_data, Dip, WellboreAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v2/dipsets/%s/dips/%s" % (dipsetid, index),
        )
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_dipset(
        self,
        *,
        dipsetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/versions" % dipsetid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dipsets_versions(
        self,
        *,
        dipsetid: str,
        version: str,
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
            "ddms/v2/dipsets/%s/versions/%s" % (dipsetid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_logs(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_log(
        self,
        *,
        logid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs/%s" % logid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log(
        self,
        *,
        logid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs/%s" % logid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_data(
        self,
        *,
        logid: str,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if orient is not None:
            params["orient"] = orient
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs/%s/data" % logid)
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def write_log_data(
        self,
        *,
        logid: str,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if orient is not None:
            params["orient"] = orient
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs/%s/data" % logid)
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_decimated_log(
        self,
        *,
        logid: str,
        quantiles: str | None = None,
        start: str | None = None,
        stop: str | None = None,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if quantiles is not None:
            params["quantiles"] = quantiles
        if start is not None:
            params["start"] = start
        if stop is not None:
            params["stop"] = stop
        if orient is not None:
            params["orient"] = orient
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/logs/%s/decimated" % logid
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_statistics(
        self,
        *,
        logid: str,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/logs/%s/statistics" % logid
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def upload_log_data(
        self,
        *,
        logid: str,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if orient is not None:
            params["orient"] = orient
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/logs/%s/upload_data" % logid
        )
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_versions(
        self,
        *,
        logid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/logs/%s/versions" % logid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_version(
        self,
        *,
        logid: str,
        version: str,
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
            "ddms/v2/logs/%s/versions/%s" % (logid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_version_data(
        self,
        *,
        logid: str,
        version: str,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if orient is not None:
            params["orient"] = orient
        if bulk_path is not None:
            params["bulk-path"] = bulk_path

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v2/logs/%s/versions/%s/data" % (logid, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_logsets(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_logset(
        self,
        *,
        logsetid: str,
        recursive: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets/%s" % logsetid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset(
        self,
        *,
        logsetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets/%s" % logsetid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset_versions(
        self,
        *,
        logsetid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/logsets/%s/versions" % logsetid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset_version(
        self,
        *,
        logsetid: str,
        version: str,
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
            "ddms/v2/logsets/%s/versions/%s" % (logsetid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_marker(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_marker(
        self,
        *,
        markerid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers/%s" % markerid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker(
        self,
        *,
        markerid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers/%s" % markerid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker_versions(
        self,
        *,
        markerid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/markers/%s/versions" % markerid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker_version(
        self,
        *,
        markerid: str,
        version: str,
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
            "ddms/v2/markers/%s/versions/%s" % (markerid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_trajectories(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/trajectories")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_trajectory(
        self,
        *,
        trajectoryid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/trajectories/%s" % trajectoryid
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory(
        self,
        *,
        trajectoryid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/trajectories/%s" % trajectoryid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory_data(
        self,
        *,
        trajectoryid: str,
        channels: str | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if channels is not None:
            params["channels"] = channels
        if orient is not None:
            params["orient"] = orient

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v2/trajectories/%s/data" % trajectoryid,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_trajectory_data(
        self,
        *,
        trajectoryid: str,
        orient: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if orient is not None:
            params["orient"] = orient

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v2/trajectories/%s/data" % trajectoryid,
        )
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory_versions(
        self,
        *,
        trajectoryid: str,
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
            "ddms/v2/trajectories/%s/versions" % trajectoryid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory_version(
        self,
        *,
        trajectoryid: str,
        version: str,
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
            "ddms/v2/trajectories/%s/versions/%s" % (trajectoryid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory_version_data(
        self,
        *,
        trajectoryid: str,
        version: str,
        channels: str | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if channels is not None:
            params["channels"] = channels
        if orient is not None:
            params["orient"] = orient

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v2/trajectories/%s/versions/%s/data" % (trajectoryid, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wellbore_v2(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wellbores")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbores(
        self,
        *,
        wellboreid: str,
        recursive: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/wellbores/%s" % wellboreid
        )
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbores(
        self,
        *,
        wellboreid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/wellbores/%s" % wellboreid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellbore(
        self,
        *,
        wellboreid: str,
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
            "ddms/v2/wellbores/%s/versions" % wellboreid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbores_versions(
        self,
        *,
        wellboreid: str,
        version: str,
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
            "ddms/v2/wellbores/%s/versions/%s" % (wellboreid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_well(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_well(
        self,
        *,
        wellid: str,
        recursive: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        params = {}
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells/%s" % wellid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_v2(
        self,
        *,
        wellid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells/%s" % wellid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_versions_v2(
        self,
        *,
        wellid: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "ddms/v2/wells/%s/versions" % wellid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version(
        self,
        *,
        wellid: str,
        version: str,
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
            "ddms/v2/wells/%s/versions/%s" % (wellid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
