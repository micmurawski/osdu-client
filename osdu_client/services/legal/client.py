from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import LegalTagDto, RequestLegalTags, SearchLegalTag, UpdateLegalTag


class LegalAPIError(OSDUAPIError):
    pass


class LegalClient(OSDUAPIClient):
    service_path = "/api/legal/v1/"

    def list_legaltags(
        self, *, valid: str | None = None, data_partition_id: str | None = None
    ) -> dict:
        """
        This allows for the retrieval of all LegalTags.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            valid (str): If true returns only valid LegalTags, if false returns only invalid LegalTags.  Default value is true.
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
        if valid is not None:
            params["valid"] = valid

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def update_legaltag(
        self,
        *,
        name: str | None = None,
        contract_id: str | None = None,
        description: str | None = None,
        expiration_date: str | None = None,
        extension_properties: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        This allows to update certain properties of your LegalTag using the `name` associated with it.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): The name of the LegalTag
            contract_id (str): The Id of the physical contract associated with the data being ingested.
            description (str): The optional description if the LegalTag to allow for easier discoverability of Legaltags overtime.
            expiration_date (str): The optional expiration date of the contract in the format YYYY-MM-DD
            extension_properties (dict): The optional object field to attach any company specific attributes.
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if name is not None:
            request_data["name"] = name
        if contract_id is not None:
            request_data["contractId"] = contract_id
        if description is not None:
            request_data["description"] = description
        if expiration_date is not None:
            request_data["expirationDate"] = expiration_date
        if extension_properties is not None:
            request_data["extensionProperties"] = extension_properties

        if self.validation:
            validate_data(request_data, UpdateLegalTag)

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def create_legaltag(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        properties: dict | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        This allows for the creation of your LegalTag. There can only be 1 LegalTag per `name`. A LegalTag must be created before you can start ingesting data for that name.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): The name of the LegalTag
            description (str): The description of the LegalTag
            properties (dict):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {}
        if name is not None:
            request_data["name"] = name
        if description is not None:
            request_data["description"] = description
        if properties is not None:
            request_data["properties"] = properties

        if self.validation:
            validate_data(request_data, LegalTagDto)

        url = urljoin(self.base_url, self.service_path, "legaltags")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def validate_legaltags(
        self, *, names: list[str], data_partition_id: str | None = None
    ) -> dict:
        """
        This allows for the retrieval of the reason why your LegalTag is not valid. A maximum of 25 can be retrieved at once.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            names (list[str]): The name of all the LegalTags to retrieve.
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
            "names": names,
        }

        if self.validation:
            validate_data(request_data, RequestLegalTags)

        url = urljoin(self.base_url, self.service_path, "legaltags:validate")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def query_legaltags(
        self,
        *,
        valid: str | None = None,
        query_list: list[str] | None = None,
        operator_list: list[str] | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        limit: int | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        This allows search for specific attributes of legaltags including the attributes of extensionproperties
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            valid (str): If true returns only valid LegalTags, if false returns only invalid LegalTags.  Default value is true.
            query_list (list[str]): Filter condition query
            operator_list (list[str]): If there are multiple conditions need to be joined in by logical operators
            sort_by (str):
            sort_order (str):
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
        if valid is not None:
            params["valid"] = valid

        request_data = {}
        if query_list is not None:
            request_data["queryList"] = query_list
        if operator_list is not None:
            request_data["operatorList"] = operator_list
        if sort_by is not None:
            request_data["sortBy"] = sort_by
        if sort_order is not None:
            request_data["sortOrder"] = sort_order
        if limit is not None:
            request_data["limit"] = limit

        if self.validation:
            validate_data(request_data, SearchLegalTag)

        url = urljoin(self.base_url, self.service_path, "legaltags:query")
        response = requests.post(url, headers=headers, params=params, json=request_data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_batch_legaltags(
        self, *, names: list[str], data_partition_id: str | None = None
    ) -> dict:
        """
        This allows for the retrieval of your LegalTags using the `name` associated with it. A maximum of 25 can be retrieved at once.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            names (list[str]): The name of all the LegalTags to retrieve.
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
            "names": names,
        }

        if self.validation:
            validate_data(request_data, RequestLegalTags)

        url = urljoin(self.base_url, self.service_path, "legaltags:batchRetrieve")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltags_properties(self, data_partition_id: str | None = None) -> dict:
        """
        This allows for the retrieval of allowed values for LegalTag properties.
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

        url = urljoin(self.base_url, self.service_path, "legaltags:properties")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltag(self, *, name: str, data_partition_id: str | None = None) -> dict:
        """
        This allows for the retrieval of your LegalTag using the `name` associated with it.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name of the LegalTag
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "legaltags/%s" % name)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def delete_legaltag(
        self, *, name: str, data_partition_id: str | None = None
    ) -> dict:
        """
        This allows for the deletion of your LegalTag with the given `name`. This makes the given legaltags data invalid.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name of the LegalTag to delete
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "legaltags/%s" % name)
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_legaltag_compliance_job_status(
        self, data_partition_id: str | None = None
    ) -> dict:
        """
        To check LegalTag Compliance Job Status.
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

        url = urljoin(self.base_url, self.service_path, "jobs/updateLegalTagStatus")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
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
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/readiness_check` endpoint, which provides `Legal service is ready` message.
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

        url = urljoin(self.base_url, self.service_path, "_ah/readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint, which provides `Legal service is alive` message.
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

        url = urljoin(self.base_url, self.service_path, "_ah/liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise LegalAPIError(response.text, response.status_code)
        return response.json()
