from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.wellbore.common import WellboreCommonClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CreateDataSessionRequest, UpdateSessionState


class WellboreAPIError(OSDUAPIError):
    pass


class WellboreClient(WellboreCommonClient):
    service_path = ""

    def query_alpha_query_wellbores(
        self, *, names: str | None = None, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if names is not None:
            params["names"] = names

        url = urljoin(self.base_url, self.service_path, "alpha/ddms/v3/query/wellbores")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def query_alpha_query_wellbores_wellboretrajectories(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "alpha/ddms/v3/query/wellbores/%s/wellboretrajectories" % wellbore_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def query_alpha_query_welllogs(
        self,
        *,
        names: str | None = None,
        wellbore_id: str | None = None,
        mnemonics: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if names is not None:
            params["names"] = names
        if wellbore_id is not None:
            params["wellbore_id"] = wellbore_id
        if mnemonics is not None:
            params["mnemonics"] = mnemonics

        url = urljoin(self.base_url, self.service_path, "alpha/ddms/v3/query/welllogs")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_query_wellbore_welllogs(
        self, *, wellbore_attribute: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/query/wellbore/%s/welllogs" % wellbore_attribute,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_query_wellbores_wellboremarkersets(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/query/wellbores/%s/wellboremarkersets" % wellbore_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_query_wellbores_welllogs(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/query/wellbores/%s/welllogs" % wellbore_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wellbore_interval_set(
        self, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellboreintervalsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboreintervalsets/%s" % wellboreintervalsetsid,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboreintervalsets/%s" % wellboreintervalsetsid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboreintervalsets/%s/versions" % wellboreintervalsetsid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_interval_sets_versions(
        self,
        *,
        wellboreintervalsetsid: str,
        version: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboreintervalsets/%s/versions/%s"
            % (wellboreintervalsetsid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellbore_markerset(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellboremarkersets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore_markerset(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboremarkersets/%s" % wellboremarkersetid,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboremarkersets(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboremarkersets/%s" % wellboremarkersetid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboremarkerset_versions(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboremarkersets/%s/versions" % wellboremarkersetid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboremarkersets_versions(
        self,
        *,
        wellboremarkersetid: str,
        version: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboremarkersets/%s/versions/%s"
            % (wellboremarkersetid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wellbore_v3(
        self, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellbores")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/wellbores/%s" % wellboreid
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/wellbores/%s" % wellboreid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_versions(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellbores/%s/versions" % wellboreid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbores_versions(
        self, *, wellboreid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellbores/%s/versions/%s" % (wellboreid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellboretrajectories(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellboretrajectories")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboretrajectories_data(
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            "ddms/v3/wellboretrajectories/%s/data" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellboretrajectories_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def list_records_sessions_v3(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/sessions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellboretrajectories_sessions(
        self,
        *,
        mode: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
        record_id: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            "ddms/v3/wellboretrajectories/%s/sessions" % record_id,
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_record_session_v3(
        self, *, record_id: str, session_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def patch_wellboretrajectories_sessions(
        self,
        *,
        state: str,
        record_id: str,
        session_id: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "state": state,
        }

        if self.validation:
            validate_data(request_data, UpdateSessionState, WellboreAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellboretrajectories_sessions_data(
        self, *, record_id: str, session_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/sessions/%s/data"
            % (record_id, session_id),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_returns_data_specified_version(
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            "ddms/v3/wellboretrajectories/%s/versions/%s/data" % (record_id, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellboretrajectories(
        self,
        *,
        wellboretrajectoryid: str,
        purge: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if purge is not None:
            params["purge"] = purge

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s" % wellboretrajectoryid,
        )
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboretrajectories(
        self, *, wellboretrajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s" % wellboretrajectoryid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellboretrajectory(
        self, *, wellboretrajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/versions" % wellboretrajectoryid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboretrajectories_versions(
        self,
        *,
        wellboretrajectoryid: str,
        version: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wellboretrajectories/%s/versions/%s"
            % (wellboretrajectoryid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_welllogs(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/welllogs")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllogs_data(
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/data" % record_id
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_welllogs_data(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/data" % record_id
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllogs_data_statistics(
        self,
        *,
        record_id: str,
        curves: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if curves is not None:
            params["curves"] = curves

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/data/statistics" % record_id,
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def list_session_given_record(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/sessions" % record_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_welllogs_sessions(
        self,
        *,
        mode: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
        record_id: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/sessions" % record_id
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_session(
        self, *, record_id: str, session_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def update_welllogs_sessions(
        self,
        *,
        state: str,
        record_id: str,
        session_id: str,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "state": state,
        }

        if self.validation:
            validate_data(request_data, UpdateSessionState, WellboreAPIError)

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def send_welllog_sessions_data(
        self, *, record_id: str, session_id: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/sessions/%s/data" % (record_id, session_id),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_version_data(
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
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
            "ddms/v3/welllogs/%s/versions/%s/data" % (record_id, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_version_data_statistics(
        self,
        *,
        record_id: str,
        version: str,
        curves: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if curves is not None:
            params["curves"] = curves

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/versions/%s/data/statistics" % (record_id, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def trigger_welllog_version_data_statistics(
        self, *, record_id: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/versions/%s/data/statistics" % (record_id, version),
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_welllog(
        self,
        *,
        welllogid: str,
        purge: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        params = {}
        if purge is not None:
            params["purge"] = purge

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/welllogs/%s" % welllogid
        )
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog(
        self, *, welllogid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/welllogs/%s" % welllogid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_versions(
        self, *, welllogid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/versions" % welllogid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_version(
        self, *, welllogid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/welllogs/%s/versions/%s" % (welllogid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wells(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wells")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_well(self, *, wellid: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wells/%s" % wellid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well(self, *, wellid: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wells/%s" % wellid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_versions(
        self, *, wellid: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url, self.service_path, "ddms/v3/wells/%s/versions" % wellid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version(
        self, *, wellid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wells/%s/versions/%s" % (wellid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
