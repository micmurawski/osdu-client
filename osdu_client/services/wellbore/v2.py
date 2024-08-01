from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.wellbore.common import WellboreCommonClient
from osdu_client.validation import validate_data

from .models import (
    CreateDataSessionRequest,
    UpdateSessionState,
    Dip,
)


class WellboreAPIError(OSDUAPIError):
    pass


class WellboreClient(WellboreCommonClient):
    service_path = ""

    def get_alpha_logs_data(
        self,
        *,
        record_id: str,
        offset: int | None = None,
        limit: int | None = None,
        curves: str | None = None,
        describe: bool | None = None,
        filter: list[str] | None = None,
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
                offset (int): The number of rows that are to be skipped and not included in the result.
                limit (int): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (bool): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (list[str]):

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
            self.base_url, self.service_path, "alpha/ddms/v2/logs/%s/data" % record_id
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def write_alpha_logs_data(
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
            self.base_url, self.service_path, "alpha/ddms/v2/logs/%s/data" % record_id
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def list_records_sessions_v2(
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
            "alpha/ddms/v2/logs/%s/sessions" % record_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_alpha_logs_sessions(
        self,
        *,
        record_id: str,
        mode: str,
        from_version: int | None = 0,
        meta: dict | None = None,
        time_to_live: int | None = "1440",
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
            "alpha/ddms/v2/logs/%s/sessions" % record_id,
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_record_session_v2(
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
            "alpha/ddms/v2/logs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def patch_alpha_logs_sessions(
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
            "alpha/ddms/v2/logs/%s/sessions/%s" % (record_id, session_id),
        )
        response = requests.patch(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def send_alpha_logs_sessions_data(
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
        offset: int | None = None,
        limit: int | None = None,
        curves: str | None = None,
        describe: bool | None = None,
        filter: list[str] | None = None,
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
                offset (int): The number of rows that are to be skipped and not included in the result.
                limit (int): The maximum number of rows to be returned.
                curves (str): Filters curves. List of curves to be returned. The curves are returned in the same order as it is given.
                describe (bool): The "describe" query option allows clients to request a description of the matching result. (number of rows, columns name)
                filter (list[str]):

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
            "alpha/ddms/v2/logs/%s/versions/%s/data" % (record_id, version),
        )
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_dipset(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_dipset(
        self,
        *,
        dipsetid: str,
        recursive: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            dipsetid (str):
            recursive (bool): Whether or not to delete records children
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
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets/%s" % dipsetid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dipset(
        self, *, dipsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the DipSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v2/dipsets/%s" % dipsetid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dip(
        self,
        *,
        dipsetid: str,
        index: int | None = None,
        limit: int | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Return dips from dipset from the given index until the given number of dips specifed in query parameters.
            If not specified returns all dips from dipset.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
                index (int):
                limit (int):
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
        self, *, dipsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Replace previous dips by provided dips. Sort dips by reference and azimuth.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str): The ID of the dipset
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
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/dips" % dipsetid
        )
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def insert_dip_in_dipset(
        self, *, dipsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Insert dips in dipset.
            Existing dips are not replaced.
            Several dip can have same reference.
            Operation will sort by reference all dips in dipset (may modify dip indexes).
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
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
        min_reference: int | None = None,
        max_reference: int | None = None,
        classification: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Search dip within reference interval and specific classification.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
                min_reference (int): Min reference for the dips to search in the dipset
                max_reference (int):
                classification (str):
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
        self, *, dipsetid: str, index: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Removes the dip at index.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
                index (str):
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
            "ddms/v2/dipsets/%s/dips/%s" % (dipsetid, index),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dip_at_index(
        self, *, dipsetid: str, index: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Return dip from dipset at the given index.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
                index (str):
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
            "ddms/v2/dipsets/%s/dips/%s" % (dipsetid, index),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def update_dip(
        self,
        *,
        dipsetid: str,
        index: str,
        azimuth: dict,
        inclination: dict,
        reference: dict,
        classification: str | None = None,
        quality: dict | None = None,
        x_coordinate: dict | None = None,
        y_coordinate: dict | None = None,
        z_coordinate: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        "Update dip at index
        Operation will sort by reference all dips in dipset (may modify dip indexes).
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            dipsetid (str):
            index (str):
            azimuth (dict): Only degrees unit is supported for the moment
            inclination (dict): Only degrees unit is supported for the moment
            reference (dict): Only Measured Depth in meter is supported for the moment
            classification (str): Any string is accepted.
            quality (dict): Decimal number between 0 and 1
            x_coordinate (dict): Only meter unit is supported for the moment
            y_coordinate (dict): Only meter unit is supported for the moment
            z_coordinate (dict): Only meter unit is supported for the moment
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
            validate_data(request_data, Dip)

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
        self, *, dipsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
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
            self.base_url, self.service_path, "ddms/v2/dipsets/%s/versions" % dipsetid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_dipsets_versions(
        self, *, dipsetid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the DipSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                dipsetid (str):
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
            "ddms/v2/dipsets/%s/versions/%s" % (dipsetid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_logs(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_log(self, *, logid: str, data_partition_id: str | None = None) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            logid (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logs/%s" % logid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log(self, *, logid: str, data_partition_id: str | None = None) -> dict:
        """
            Get the log object using its data ecosystem **id**.  If the log
                        kind is *wks:log:1.0.5* returns the record directly If the
                        wellbore kind is different *wks:log:1.0.5* it will get the raw
                        record and convert the results to match the *wks:log:1.0.5*. If
                        conversion is not possible returns an error **500**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

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
    ) -> dict:
        """
            return full bulk data.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                orient (str): format for JSON only.
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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
    ) -> dict:
        """
            Overwrite if exists.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                orient (str): format for JSON only.
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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
        quantiles: int | None = None,
        start: int | None = None,
        stop: int | None = None,
        orient: str | None = None,
        bulk_path: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            TODO
                    Note: row order is not preserved.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                quantiles (int): Number of division desired
                start (int): The start value for the log decimation
                stop (int): The stop value for the log decimation
                orient (str): response format JSON. Only "values" is allowed.
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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
    ) -> dict:
        """
            This API will return count, mean, std, min, max and percentiles of each column.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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
    ) -> dict:
        """
            Overwrite if exists.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                orient (str): format for JSON only.
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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
        self, *, logid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
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
            self.base_url, self.service_path, "ddms/v2/logs/%s/versions" % logid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_log_version(
        self, *, logid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
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
    ) -> dict:
        """
            return full bulk data.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logid (str):
                version (str):
                orient (str): format for JSON only.
                bulk_path (str): The json path to the bulk reference (see https://goessner.net/articles/JsonPath/). Required for non wks:log.
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

    def create_or_update_logsets(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_logset(
        self,
        *,
        logsetid: str,
        recursive: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            logsetid (str):
            recursive (bool): Whether or not to delete records children
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
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets/%s" % logsetid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset(
        self, *, logsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the LogSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logsetid (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v2/logsets/%s" % logsetid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset_versions(
        self, *, logsetid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logsetid (str):
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
            self.base_url, self.service_path, "ddms/v2/logsets/%s/versions" % logsetid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_logset_version(
        self, *, logsetid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the LogSet object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                logsetid (str):
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
            "ddms/v2/logsets/%s/versions/%s" % (logsetid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_marker(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_marker(
        self, *, markerid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            markerid (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers/%s" % markerid)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker(
        self, *, markerid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the Marker object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                markerid (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "ddms/v2/markers/%s" % markerid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker_versions(
        self, *, markerid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                markerid (str):
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
            self.base_url, self.service_path, "ddms/v2/markers/%s/versions" % markerid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_marker_version(
        self, *, markerid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                markerid (str):
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
            "ddms/v2/markers/%s/versions/%s" % (markerid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_trajectories(
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/trajectories")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_trajectory(
        self, *, trajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            trajectoryid (str):
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
            self.base_url, self.service_path, "ddms/v2/trajectories/%s" % trajectoryid
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory(
        self, *, trajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the Trajectory object using its **id**.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
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
        channels: list[str] | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            return full bulk data.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
                channels (list[str]): List of channels to get. If not provided, return all channels.
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
    ) -> dict:
        """
            Overwrite if exists.
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
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
        self, *, trajectoryid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
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
            "ddms/v2/trajectories/%s/versions" % trajectoryid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_trajectory_version(
        self, *, trajectoryid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
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
        channels: list[str] | None = None,
        orient: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            return full bulk data.
        Required roles: 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins'.
        In addition, users must be a member of data groups to access the data.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                trajectoryid (str):
                version (str):
                channels (list[str]): List of channels to get. If not provided, return all channels.
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wellbores")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_wellbores(
        self,
        *,
        wellboreid: str,
        recursive: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellboreid (str):
            recursive (bool): Whether or not to delete records children
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
        self, *, wellboreid: str, data_partition_id: str | None = None
    ) -> dict:
        """
            Get the Wellbore object using its **id**.  If the wellbore kind is
                *wks:wellbore:1.0.6* returns the record directly If the wellbore
                kind is different *wks:wellbore:1.0.6* it will get the raw record and
                convert the results to match the *wks:wellbore:1.0.6*. If convertion is
                not possible returns an error **500**.
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
            self.base_url, self.service_path, "ddms/v2/wellbores/%s" % wellboreid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_versions_wellbore(
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
            "ddms/v2/wellbores/%s/versions" % wellboreid,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbores_versions(
        self, *, wellboreid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the Wellbore object using its **id**.  If the wellbore kind is
                *wks:wellbore:1.0.6* returns the record directly If the wellbore
                kind is different *wks:wellbore:1.0.6* it will get the raw record and
                convert the results to match the *wks:wellbore:1.0.6*. If convertion is
                not possible returns an error **500**.
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
            "ddms/v2/wellbores/%s/versions/%s" % (wellboreid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_well(self, data_partition_id: str | None = None) -> dict:
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def delete_well(
        self,
        *,
        wellid: str,
        recursive: bool | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Required roles: 'users.datalake.editors' or 'users.datalake.admins
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellid (str):
            recursive (bool): Whether or not to delete records children
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
        if recursive is not None:
            params["recursive"] = recursive

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells/%s" % wellid)
        response = requests.delete(url, headers=headers, params=params)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_v2(self, *, wellid: str, data_partition_id: str | None = None) -> dict:
        """
            Get the Well object using its **id**.  If the well kind is
                *wks:well:1.0.2* returns the record directly If the well
                kind is different *wks:well:1.0.2* it will get the raw record and
                convert the results to match the *wks:well:1.0.2*. If convertion is
                not possible returns an error **500**.
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

        url = urljoin(self.base_url, self.service_path, "ddms/v2/wells/%s" % wellid)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_versions_v2(
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
            self.base_url, self.service_path, "ddms/v2/wells/%s/versions" % wellid
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version(
        self, *, wellid: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
            "Get the Well object using its **id**.  If the well kind is
                *wks:well:1.0.2* returns the record directly If the well
                kind is different *wks:well:1.0.2* it will get the raw record and
                convert the results to match the *wks:well:1.0.2*. If convertion is
                not possible returns an error **500**.
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
            "ddms/v2/wells/%s/versions/%s" % (wellid, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellboreAPIError(response.text, response.status_code)
        return response.json()
