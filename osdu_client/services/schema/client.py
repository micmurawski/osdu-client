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
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest, SchemaAPIError)

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
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest, SchemaAPIError)

        url = urljoin(self.base_url, self.service_path, "schema")
        response = requests.put(url, headers=headers, json=request_data)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def create_schema(
        self, *, schema_info: dict, schema: dict, data_partition_id: str | None = None
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "schemaInfo": schema_info,
            "schema": schema,
        }

        if self.validation:
            validate_data(request_data, SchemaRequest, SchemaAPIError)

        url = urljoin(self.base_url, self.service_path, "schema")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def get_schema(self, *, id: str, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "schema/%s" % id)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SchemaAPIError(response.text, response.status_code)
        return response.json()
