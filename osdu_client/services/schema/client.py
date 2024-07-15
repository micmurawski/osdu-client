from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import SchemaRequest


class SchemaAPIError(OSDUAPIError):
    pass


class SchemaClient(OSDUAPIClient):
    service_path = "/api/schema-service/v1"

    def create_or_update_schema_system(
        self, *, schema_info: dict, schema: dict, data_partition_id: str | None = None
    ) -> dict:
        """
        Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema repository. If a user tries to create a schema with status other than `DEVELOPMENT`, API will not throw an exception. The update of schema without `DEVELOPMENT` status would cause error. Any schema instance with the same schemaIdentity is replaced. A schema state can also be changed from `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same schema content. **Note:** The schema may refer to other schema definitions in `DEVELOPMENT` state. If those schemas are updated themselves, it is the developer's responsibility to PUT the dependent schemas again to update the schema. Scope for a schema will be SHARED for all the schemas created using this API.Service principal authorization is required to call thi API.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            schema_info (dict):
            schema (dict):
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
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest)

        url = urljoin(self.base_url, self.service_path, "schemas/system")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def search_schemas(
        self,
        *,
        authority: str | None = None,
        source: str | None = None,
        entity_type: str | None = None,
        schema_version_major: str | None = None,
        schema_version_minor: str | None = None,
        schema_version_patch: str | None = None,
        status: str | None = None,
        scope: str | None = None,
        latest_version: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
        Searches for information of available schema (SchemaInfo) in schema repository. Support options to filter out the search contents. Required roles:  `service.schema-service.viewers` groups to get the schema.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            authority (str): pass an optional string to search for a specific authority
            source (str): pass an optional string to search for a specific source
            entity_type (str): pass an optional string to search for a specific entityType
            schema_version_major (str): pass an optional string to search for a specific schemaVersionMajor
            schema_version_minor (str): pass an optional string to search for a specific schemaVersionMinor
            schema_version_patch (str): pass an optional string to search for a specific schemaVersionPatch
            status (str): The schema status specification
            scope (str): The scope or schema visibility specification
            latest_version (str): if True, only return the latest version
            limit (str): maximum number of schema records to return
            offset (str): number of records to skip for pagination
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
        if authority is not None:
            params["authority"] = authority
        if source is not None:
            params["source"] = source
        if entity_type is not None:
            params["entityType"] = entity_type
        if schema_version_major is not None:
            params["schemaVersionMajor"] = schema_version_major
        if schema_version_minor is not None:
            params["schemaVersionMinor"] = schema_version_minor
        if schema_version_patch is not None:
            params["schemaVersionPatch"] = schema_version_patch
        if status is not None:
            params["status"] = status
        if scope is not None:
            params["scope"] = scope
        if latest_version is not None:
            params["latestVersion"] = latest_version
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        url = urljoin(self.base_url, self.service_path, "schema")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def update_schema(
        self, *, schema_info: dict, schema: dict, data_partition_id: str | None = None
    ) -> dict:
        """
        Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema repository. If a user tries to create/update a schema with status other than `DEVELOPMENT`, API will throw an exception. Any schema instance with the same schemaIdentity is replaced (in contrast to the immutability of `PUBLISHED` or `OBSOLETE` schemas). A schema state can also be changed from `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same schema content. **Note:** The schema may refer to other schema definitions in `DEVELOPMENT` state. If those schemas are updated themselves, it is the developer's responsibility to PUT the dependent schemas again to update the schemas. Scope for a schema can't be updated, its a system defined value. Required roles:  `service.schema-service.editors` groups to update schema.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            schema_info (dict):
            schema (dict):
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
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest)

        url = urljoin(self.base_url, self.service_path, "schema")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def create_schema(
        self, *, schema_info: dict, schema: dict, data_partition_id: str | None = None
    ) -> dict:
        """
        Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source` and `entityType` will be registered if not present. If lower minor versions are registered the service validates the new schema against breaking changes; if breaking changes are discovered the request fails. **Note:** The schema must not reference other schemas with status `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common tenant and `INTERNAL` for private tenant). Required roles : `service.schema-service.editors` groups to create schema.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            schema_info (dict):
            schema (dict):
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
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest)

        url = urljoin(self.base_url, self.service_path, "schema")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def get_schema(self, *, id: str, data_partition_id: str | None = None) -> dict:
        """
        Retrieve a schema using its system defined id. Required roles:  `service.schema-service.viewers` groups to get the schema.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            id (str): The system id of the schema
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "schema/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        """
        For deployment available public `/liveness_check` endpoint verifies the operational status of the Schema Service.
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
            raise SchemaAPIError(response.text, response.status_code)
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
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()
