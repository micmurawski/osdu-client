from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin


class WellDeliveryAPIError(OSDUAPIError):
    pass


class WellDeliveryClient(OSDUAPIClient):
    service_path = "/api/well-delivery"

    def create_or_update_storage(
        self, *, type: str, entity: dict, data_partition_id: str | None = None
    ) -> dict:
        """
        The API represents the main injection mechanism into the Object Database. It allows entity creation and/or update. When no entity id is provided or when the provided id is not already present in the Object Database then a new entity is created. If the id is related to an existing entity in the Object Database then an update operation takes place and a new version of the entity is created. Required roles: service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            entity (dict):
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
            "Entity": entity,
        }

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s" % type)
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_entity(
        self, *, type: str, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        This API returns the latest version of the given entity type and id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s/%s" % (type, id))
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def delete_entity(
        self, *, type: str, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs a logical deletion of the given entity and all of its versions.   This operation can be reverted later. Required roles: service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s/%s" % (type, id))
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_entity_version(
        self, *, type: str, id: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API retrieves the specific version of the given entity type and id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
            version (str): Entity version
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
            "storage/v1/%s/%s/%s" % (type, id, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def delete_storage_version(
        self, *, type: str, id: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs a logical deletion of the given entity type, id, and version number.This operation can be reverted later. Required roles: service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
            version (str): Entity version
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
            "storage/v1/%s/%s/%s" % (type, id, version),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_storage_version(
        self, *, type: str, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a list containing all version numbers for the given entity type and id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
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
            self.base_url, self.service_path, "storage/v1/%s/versions/%s" % (type, id)
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def purge_entity(
        self, *, type: str, id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API performs a physical deletion of the given entity and all of its versions.  This operation cannot be undone. Required roles: service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            id (str): Entity id
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
            self.base_url, self.service_path, "storage/v1/%s/%s:purge" % (type, id)
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_well_activity_program(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns version number list of well activity program for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellActivityPrograms/v1/versions/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns latest version of well activity program for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellActivityPrograms/v1/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_version(
        self, *, well_id: str, wap_version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns specific version of well activity program for the given well id and well activity program version. Required roles: service.storage.viewer,  service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
            wap_version (str): Well activity program version
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
            "wellActivityPrograms/v1/by_well/%s/%s" % (well_id, wap_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_with_refs(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the latest version of well activity program with a lists of URI   references for a well. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellActivityPrograms/v1/reference_tree/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_version_with_refs(
        self, *, well_id: str, wap_version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a specific version of well activity program with a lists of URI references for a well. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
            wap_version (str): Well activity program version
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
            "wellActivityPrograms/v1/reference_tree/by_well/%s/%s"
            % (well_id, wap_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_programs_full_content_by_well(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the latest version of well activity program with a lists of children   for a well. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellActivityPrograms/v1/full_content/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_activity_plans_by_well(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the Activity Plan object from a well id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            self.base_url, self.service_path, "activityPlans/v1/by_well/%s" % well_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_actual_well(
        self, *, name: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns version number list of actual well for the given name. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
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
            "wells/v1/versions/by_name/%s:actual" % name,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_by_name_actual(
        self, *, name: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns actual well object for given name.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
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
            self.base_url, self.service_path, "wells/v1/by_name/%s:actual" % name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version_by_name_actual(
        self, *, name: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a specific version of actual well object for the given name.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
            version (str): Well version
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
            "wells/v1/by_name/%s/%s:actual" % (name, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_planned_well(
        self, *, name: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns version number list of planned well for the given name. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
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
            "wells/v1/versions/by_name/%s:planned" % name,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_by_name_planned(
        self, *, name: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a latest version of planned well object for given name.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
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
            self.base_url, self.service_path, "wells/v1/by_name/%s:planned" % name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version_by_name_planned(
        self, *, name: str, version: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a specific version of planned well object for the given name.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            name (str): Name
            version (str): Well version
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
            "wells/v1/by_name/%s/%s:planned" % (name, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_actual_wellbore(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns version number list of actual wellbore for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellbores/v1/versions/by_well/%s:actual" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_actual(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns latest version of actual wellbore for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            self.base_url, self.service_path, "wellbores/v1/by_well/%s:actual" % well_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_version_actual(
        self,
        *,
        well_id: str,
        wellbore_version: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        The API returns specific version of actual wellbore for the given well id and well activity program version. Required roles: service.storage.viewer,  service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
            wellbore_version (str): Actual wellbore version
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
            "wellbores/v1/by_well/%s/%s:actual" % (well_id, wellbore_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_planned_wellbore(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns version number list of planned wellbore for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellbores/v1/versions/by_well/%s:planned" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_planned(
        self, *, well_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns latest version of planned wellbore for the given well id. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
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
            "wellbores/v1/by_well/%s:planned" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_version_planned(
        self,
        *,
        well_id: str,
        wellbore_version: str,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        The API returns specific version of planned wellbore for the given well id and well activity program version. Required roles: service.storage.viewer,  service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            well_id (str): Well id
            wellbore_version (str): Planned wellbore version
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
            "wellbores/v1/by_well/%s/%s:planned" % (well_id, wellbore_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_hole_sections_v1_by_wellbore(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a list of hole section objects for a wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "holeSections/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_bha_runs_v1_by_hole_section(
        self, *, hole_section_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a list of BHA Run objects for a hole section id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            hole_section_id (str): Hole section id
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
            "bhaRuns/v1/by_holeSection/%s" % hole_section_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_bha_runs_v1_by_wellbore_actual(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a list of actual BHA Run objects for a wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "bhaRuns/v1/by_wellbore/%s:actual" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_well_batch(
        self,
        *,
        content__type: str,
        type: str,
        well_ids: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """
        The API returns a list of entity objects for a list of wells.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            content__type (str): Content type
            type (str): Entity type
            well_ids (list[str]): Array of well id
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
                "Content-Type": content__type,
            }
        )

        request_data = {
            "well_ids": well_ids,
        }

        url = urljoin(
            self.base_url, self.service_path, "query/v1/by_well/%s:batch" % type
        )
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_wellbore_planned(
        self, *, type: str, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns planned  objects for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            wellbore_id (str): Wellbore id
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
            "query/v1/%s/by_wellbore/%s:planned" % (type, wellbore_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_wellbore_actual(
        self, *, type: str, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns actual  objects for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            type (str): Entity type
            wellbore_id (str): Wellbore id
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
            "query/v1/%s/by_wellbore/%s:actual" % (type, wellbore_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_fluids_programs(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns fluids program objects for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "fluidsPrograms/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_operations_reports(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns all available operations report objects for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "operationsReports/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_operations_reports_latest(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns latest operations report object for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "operationsReports/v1/latest/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_operations_reports_by_time_range(
        self, *, start_time: str, end_time: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns a list of operations report objects for the given time range. Date time format can be 'yyyyMMdd', 'yyyy-MM-dd', 'yyyy-M-d', 'yyyy-MM-ddTHH:mm:ss' or 'yyyy-MM-ddTHH:mm:ssZ'. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            start_time (str): Start time
            end_time (str): End time
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
            "operationsReports/v1/by_timeRange/%s/%s" % (start_time, end_time),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_operations_reports_with_refs_by_operations_report_id(
        self, *, operations_report_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns the latest version of operations report with a lists of URI references. Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            operations_report_id (str): Operations report id
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
            "operationsReports/v1/reference_tree/by_operationsReport/%s"
            % operations_report_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_fluids_reports(
        self, *, wellbore_id: str, data_partition_id: str | None = None
    ) -> dict:
        """
        The API returns fluids report objects for the given wellbore id.   Required roles: service.storage.viewer, service.storage.creator or service.storage.admin.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            wellbore_id (str): Wellbore id
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
            "fluidsReports/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()
