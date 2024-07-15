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
        """
            Get Wellbores object by name.
                     The wellbore kind is *:wks:master-data--Wellbore:*
                     Returns all records directly based on existing schemas. The query is done on data.FacilityName field

        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                names (str): You can search for several wellbore names combining wellbore name values with the bitwise inclusive OR operator "|".
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
        """
            Get all Wellbore Trajectories objects using its relationship Wellbore ID.  All Wellbore Trajectories linked to this
                    specific ID will be returned
                    The Wellbore Trajectories kind is *:wks:work-product-component--WellboreTrajectory:* returns all records directly based on existing schemas
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellbore_id (str):
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
        """
            Get all WellLogs objects using its name and optionally relationship Wellbore ID. Filtering can be done on curves mnemonics
                    The WellLogs kind is *:wks:work-product-component--WellLog:* returns all records directly based on existing schemas. The query is done on data.Name field
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                names (str):
                wellbore_id (str):
                mnemonics (str):
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
        """
            Get all WellLogs object using a specific attribute of Wellbores.  All WellLogs linked to Wellbores
                    with this specific attribute will be returned
                    The WellLogs kind is *:wks:work-product-component--WellLog:* returns all records directly based on existing schemas
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellbore_attribute (str):
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
            "ddms/v3/query/wellbore/%s/welllogs" % wellbore_attribute,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_query_wellbores_wellboremarkersets(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get all Wellbore Markersets objects using its relationship Wellbore ID.  All Markers linked to this
                    specific ID will be returned
                    The Wellbore Markerset kind is *:wks:work-product-component--WellboreMarkerSet:* returns all records directly based on existing schemas
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellbore_id (str):
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
            "ddms/v3/query/wellbores/%s/wellboremarkersets" % wellbore_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_query_wellbores_welllogs(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get all WellLogs object using its relationship Wellbore ID.  All WellLogs linked to this
                    specific ID will be returned
                    The WellLogs kind is *:wks:work-product-component--WellLog:* returns all records directly based on existing schemas
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellbore_id (str):
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
            "ddms/v3/query/wellbores/%s/welllogs" % wellbore_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_wellbore_interval_set(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellboreintervalsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellboreintervalsetsid (str):
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
            "ddms/v3/wellboreintervalsets/%s" % wellboreintervalsetsid,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the WellboreIntervalSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreintervalsetsid (str):
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
            "ddms/v3/wellboreintervalsets/%s" % wellboreintervalsetsid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellbore_interval_set(
        self, *, wellboreintervalsetsid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreintervalsetsid (str):
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
        """
            Get the WellboreIntervalSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreintervalsetsid (str):
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellboremarkersets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore_markerset(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellboremarkersetid (str):
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
            "ddms/v3/wellboremarkersets/%s" % wellboremarkersetid,
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboremarkersets(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the WellboreMarkerSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboremarkersetid (str):
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
            "ddms/v3/wellboremarkersets/%s" % wellboremarkersetid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellboremarkerset_versions(
        self, *, wellboremarkersetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboremarkersetid (str):
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
        """
            "Get the WellboreMarkerSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboremarkersetid (str):
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wellbores")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbore(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellboreid (str):
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
            self.base_url, self.service_path, "ddms/v3/wellbores/%s" % wellboreid
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the Wellbore object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreid (str):
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
            self.base_url, self.service_path, "ddms/v3/wellbores/%s" % wellboreid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_versions(
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreid (str):
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
            "ddms/v3/wellbores/%s/versions" % wellboreid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbores_versions(
        self, *, wellboreid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the Wellbore object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboreid (str):
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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
        """
            Returns the data according to the specified query parameters.
        Multiple media types response are available ("application/json", "application/x-parquet").
        The desired format can be specify in the "Accept" header, default is Parquet.

        When bulk statistics are requested using __describe__ query parameter, the response is always provided in JSON.
        The requested columns must not exceed 500.
        The query parameter __curves__ can be use to limit the number of columns.

        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.

        **Important**: In order to minimize reading time.

        1. Partial reading
            - Select only needed columns

        Note: using curves filtering has a cost, use it only if it reduces significantly the amount of retrieved bulk data.

        2. Full reading
            - Try to read all the curves, if those errors are returned go to next steps:
                - HTTP 400 "Too many columns requested"
                - HTTP 400 "Too many values requested"
                - HTTP 413 "the resource requested exceeds the limit" (When WDDMS worker are enabled)
            - Get curve names and number of rows per curve by using describe parameter
               - Each request should fetch as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                offset (str): The number of rows that are to be skipped and not included in the result.
                limit (str): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (str): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (str):

        The "filter" query parameter allows clients to filter by rows, it selects rows data following the pattern `$column_name:$operator:$value`.
        The supported operators are : lt, lte, gt, gte, eq, neq, in.

        Note: If the column name contains ':', enclose it in double quotation marks (").

                orient (str): format for JSON only.
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
        """
            Writes data to the associated record. It creates a new version.
        Payload is expected to contain the entire bulk which will replace as latest version
        any previous bulk. Previous bulk versions are accessible via the get bulk data version API.
        Support JSON and Parquet format ('Content_Type' must be set accordingly).
        Support http chunked encoding transfer.

        Required roles: 'users.datalake.editors' or 'users.datalake.admins

        **Important**: In order to minimize writing time, it's necessary to:
        - Double check whether bulk data is big enough to be sent with chunking APIs: meaning > 10 millions values or > 500 columns
            - If no, use instead POST /ddms/v3/welllogs/MY_RECORD_ID/data API
        - Ensure all curve's values are in the same chunk to be sent
        - Each chunk should contain as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
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
            "ddms/v3/wellboretrajectories/%s/data" % record_id,
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def list_records_sessions_v3(
        self, *, record_id: str, data_partition_id: str | None = None
    ) -> dict:
        """

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
            "ddms/v3/wellboretrajectories/%s/sessions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_wellboretrajectories_sessions(
        self,
        *,
        record_id: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
        mode: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Initiate a session based on record version provided. The session is isolated from any other modifications. Inside a session, individual chunk doesn't generate new individual version. A new single version is created only at session completion 'aggregating' all updates. A typical workflow is:
        1. create a session
        2. send X chunks (can be parallelized)
        3. commit the session

        Session has an expiry time. If the session is not completed before, it's automatically dropped. The session duration is specified in the request but cannot exceeds 24 hours.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                mode (str): merge mode at commit. If 'update', existing data will be merged with the data sent during the session. If 'overwrite', existing data will be ignored, the final result will only contains data sent within the session.
                from_version (int): specify the version on top of which update will be applied. By default use the latest one (0). Not relevant if overwrite is set to True.
                meta (dict): dictionary all values, stored in the session
                time_to_live (int): optional - time to live in minutes.
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
            "mode": mode,
        }
        if from_version is not None:
            request_data["fromVersion"] = from_version
        if meta is not None:
            request_data["meta"] = meta
        if time_to_live is not None:
            request_data["timeToLive"] = time_to_live

        if self.validation:
            validate_data(request_data, CreateDataSessionRequest)

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
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            session_id (str):
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
            "ddms/v3/wellboretrajectories/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def patch_wellboretrajectories_sessions(
        self,
        *,
        record_id: str,
        session_id: str,
        state: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Either validates the session' bulk data, a new version of record will be created with data sent
                    within the session. Either abandon the session, and let record unchanged.
                    Note: bulk data consistency check will be run when committing bulk data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            session_id (str):
            state (str): `commit` or `abandon` a session
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
            "state": state,
        }

        if self.validation:
            validate_data(request_data, UpdateSessionState)

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
        """
            Send a data chunk. Session must be complete/commit once all chunks are sent. This will create a new and single version aggregating all and previous bulk.Support JSON and Parquet format ('Content_Type' must be set accordingly). Support http chunked encoding.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                session_id (str):
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
        """
            Returns the data of a specific version according to the specified query parameters.
        Multiple media types response are available ("application/json", "application/x-parquet").
        The desired format can be specify in the "Accept" header, default is Parquet.

        When bulk statistics are requested using __describe__ query parameter, the response is always provided in JSON.
        The requested columns must not exceed 500.
        The query parameter __curves__ can be use to limit the number of columns.

        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.

        **Important**: In order to minimize reading time.

        1. Partial reading
            - Select only needed columns

        Note: using curves filtering has a cost, use it only if it reduces significantly the amount of retrieved bulk data.

        2. Full reading
            - Try to read all the curves, if those errors are returned go to next steps:
                - HTTP 400 "Too many columns requested"
                - HTTP 400 "Too many values requested"
                - HTTP 413 "the resource requested exceeds the limit" (When WDDMS worker are enabled)
            - Get curve names and number of rows per curve by using describe parameter
               - Each request should fetch as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
                offset (str): The number of rows that are to be skipped and not included in the result.
                limit (str): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (str): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (str):

        The "filter" query parameter allows clients to filter by rows, it selects rows data following the pattern `$column_name:$operator:$value`.
        The supported operators are : lt, lte, gt, gte, eq, neq, in.

        Note: If the column name contains ':', enclose it in double quotation marks (").

                orient (str): format for JSON only.
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellboretrajectoryid (str):
            purge (str):
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
        """
            Get the WellboreTrajectory object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboretrajectoryid (str):
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
            "ddms/v3/wellboretrajectories/%s" % wellboretrajectoryid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellboretrajectory(
        self, *, wellboretrajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboretrajectoryid (str):
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
        """
            "Get the WellboreTrajectory object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellboretrajectoryid (str):
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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
        """
            Returns the data according to the specified query parameters.
        Multiple media types response are available ("application/json", "application/x-parquet").
        The desired format can be specify in the "Accept" header, default is Parquet.

        When bulk statistics are requested using __describe__ query parameter, the response is always provided in JSON.
        The requested columns must not exceed 500.
        The query parameter __curves__ can be use to limit the number of columns.

        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.

        **Important**: In order to minimize reading time.

        1. Partial reading
            - Select only needed columns

        Note: using curves filtering has a cost, use it only if it reduces significantly the amount of retrieved bulk data.

        2. Full reading
            - Try to read all the curves, if those errors are returned go to next steps:
                - HTTP 400 "Too many columns requested"
                - HTTP 400 "Too many values requested"
                - HTTP 413 "the resource requested exceeds the limit" (When WDDMS worker are enabled)
            - Get curve names and number of rows per curve by using describe parameter
               - Each request should fetch as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                offset (str): The number of rows that are to be skipped and not included in the result.
                limit (str): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (str): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (str):

        The "filter" query parameter allows clients to filter by rows, it selects rows data following the pattern `$column_name:$operator:$value`.
        The supported operators are : lt, lte, gt, gte, eq, neq, in.

        Note: If the column name contains ':', enclose it in double quotation marks (").

                orient (str): format for JSON only.
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
        """
            Writes data to the associated record. It creates a new version.
        Payload is expected to contain the entire bulk which will replace as latest version
        any previous bulk. Previous bulk versions are accessible via the get bulk data version API.
        Support JSON and Parquet format ('Content_Type' must be set accordingly).
        Support http chunked encoding transfer.

        Required roles: 'users.datalake.editors' or 'users.datalake.admins

        **Important**: In order to minimize writing time, it's necessary to:
        - Double check whether bulk data is big enough to be sent with chunking APIs: meaning > 10 millions values or > 500 columns
            - If no, use instead POST /ddms/v3/welllogs/MY_RECORD_ID/data API
        - Ensure all curve's values are in the same chunk to be sent
        - Each chunk should contain as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
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
        """
            Returns the statistics on bulk data identified by the record in its last version.


        If wanted curves is an array:
            - requests "ARRAY" retrieves all dimensions of the array
            - requests "ARRAY[M:N]", retrieves all dimensions between M and N.



        Data types supported:
                    - int
                    - float
                    - date


            No unit conversion is supported. Statistics will be returned using the same units as recorded in Curves[].CurveUnit
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                curves (str): List of curves or array to be returned. All curves if empty
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
        """

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
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/sessions" % record_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_welllogs_sessions(
        self,
        *,
        record_id: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
        mode: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Initiate a session based on record version provided. The session is isolated from any other modifications. Inside a session, individual chunk doesn't generate new individual version. A new single version is created only at session completion 'aggregating' all updates. A typical workflow is:
        1. create a session
        2. send X chunks (can be parallelized)
        3. commit the session

        Session has an expiry time. If the session is not completed before, it's automatically dropped. The session duration is specified in the request but cannot exceeds 24 hours.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                mode (str): merge mode at commit. If 'update', existing data will be merged with the data sent during the session. If 'overwrite', existing data will be ignored, the final result will only contains data sent within the session.
                from_version (int): specify the version on top of which update will be applied. By default use the latest one (0). Not relevant if overwrite is set to True.
                meta (dict): dictionary all values, stored in the session
                time_to_live (int): optional - time to live in minutes.
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
            "mode": mode,
        }
        if from_version is not None:
            request_data["fromVersion"] = from_version
        if meta is not None:
            request_data["meta"] = meta
        if time_to_live is not None:
            request_data["timeToLive"] = time_to_live

        if self.validation:
            validate_data(request_data, CreateDataSessionRequest)

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
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            session_id (str):
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
            "ddms/v3/welllogs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def update_welllogs_sessions(
        self,
        *,
        record_id: str,
        session_id: str,
        state: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Either validates the session' bulk data, a new version of record will be created with data sent
                    within the session. Either abandon the session, and let record unchanged.
                    Note: bulk data consistency check will be run when committing bulk data.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            record_id (str):
            session_id (str):
            state (str): `commit` or `abandon` a session
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
            "state": state,
        }

        if self.validation:
            validate_data(request_data, UpdateSessionState)

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
        """
            Send a data chunk. Session must be complete/commit once all chunks are sent. This will create a new and single version aggregating all and previous bulk.Support JSON and Parquet format ('Content_Type' must be set accordingly). Support http chunked encoding.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                session_id (str):
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
        """
            Returns the data of a specific version according to the specified query parameters.
        Multiple media types response are available ("application/json", "application/x-parquet").
        The desired format can be specify in the "Accept" header, default is Parquet.

        When bulk statistics are requested using __describe__ query parameter, the response is always provided in JSON.
        The requested columns must not exceed 500.
        The query parameter __curves__ can be use to limit the number of columns.

        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.

        **Important**: In order to minimize reading time.

        1. Partial reading
            - Select only needed columns

        Note: using curves filtering has a cost, use it only if it reduces significantly the amount of retrieved bulk data.

        2. Full reading
            - Try to read all the curves, if those errors are returned go to next steps:
                - HTTP 400 "Too many columns requested"
                - HTTP 400 "Too many values requested"
                - HTTP 413 "the resource requested exceeds the limit" (When WDDMS worker are enabled)
            - Get curve names and number of rows per curve by using describe parameter
               - Each request should fetch as many as columns it is possible until upper limits are reached (> 10 millions values or > 500 columns)
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
                offset (str): The number of rows that are to be skipped and not included in the result.
                limit (str): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (str): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (str):

        The "filter" query parameter allows clients to filter by rows, it selects rows data following the pattern `$column_name:$operator:$value`.
        The supported operators are : lt, lte, gt, gte, eq, neq, in.

        Note: If the column name contains ':', enclose it in double quotation marks (").

                orient (str): format for JSON only.
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
        """
            Returns the statistics on bulk data identified by the record and given version.

        If wanted curves is an array:
            - requests "ARRAY" retrieves all dimensions of the array
            - requests "ARRAY[M:N]", retrieves all dimensions between M and N.



        Data types supported:
                    - int
                    - float
                    - date


            No unit conversion is supported. Statistics will be returned using the same units as recorded in Curves[].CurveUnit
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                record_id (str):
                version (str):
                curves (str): List of curves or array to be returned. All curves if empty
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
        """
        Trigger the computation of statistics on bulk data for
        the record identified by the record_id at its last version

        No unit conversion is supported. Statistics will be returned using the same units as recorded in Curves[].CurveUnit
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            welllogid (str):
            purge (str):
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
        """
            Get the WellLog object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                welllogid (str):
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
            self.base_url, self.service_path, "ddms/v3/welllogs/%s" % welllogid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_versions(
        self, *, welllogid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                welllogid (str):
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
            self.base_url, self.service_path, "ddms/v3/welllogs/%s/versions" % welllogid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_welllog_version(
        self, *, welllogid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the WellLog object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                welllogid (str):
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
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
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

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wells")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_well(self, *, wellid: str, data_partition_id: str | None = None) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellid (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v3/wells/%s" % wellid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well(self, *, wellid: str, data_partition_id: str | None = None) -> dict:
        """
            Get the Well object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellid (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
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
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellid (str):
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
            self.base_url, self.service_path, "ddms/v3/wells/%s/versions" % wellid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version(
        self, *, wellid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the Well object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                wellid (str):
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

        url = urljoin(
            self.base_url,
            self.service_path,
            "ddms/v3/wells/%s/versions/%s" % (wellid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
