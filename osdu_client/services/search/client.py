from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import CursorQueryRequest, QueryRequest


class SearchAPIError(OSDUAPIError):
    pass


class SearchClient(OSDUAPIClient):
    service_path = "/api/search/v2/"

    def query_with_cursor(
        self,
        *,
        kind: dict,
        limit: int | None = None,
        query: str | None = None,
        highlighted_fields: list[str] | None = None,
        returned_fields: list[str] | None = None,
        sort: dict | None = None,
        query_as_owner: bool | None = None,
        track_total_count: bool | None = None,
        spatial_filter: dict | None = None,
        cursor: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "kind": kind,
        }
        if limit is not None:
            request_data["limit"] = limit
        if query is not None:
            request_data["query"] = query
        if highlighted_fields is not None:
            request_data["highlightedFields"] = highlighted_fields
        if returned_fields is not None:
            request_data["returnedFields"] = returned_fields
        if sort is not None:
            request_data["sort"] = sort
        if query_as_owner is not None:
            request_data["queryAsOwner"] = query_as_owner
        if track_total_count is not None:
            request_data["trackTotalCount"] = track_total_count
        if spatial_filter is not None:
            request_data["spatialFilter"] = spatial_filter
        if cursor is not None:
            request_data["cursor"] = cursor

        if self.validation:
            validate_data(request_data, CursorQueryRequest, SearchAPIError)

        url = urljoin(self.base_url, self.service_path, "query_with_cursor")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def query(
        self,
        *,
        kind: dict,
        limit: int | None = None,
        query: str | None = None,
        highlighted_fields: list[str] | None = None,
        returned_fields: list[str] | None = None,
        sort: dict | None = None,
        query_as_owner: bool | None = None,
        track_total_count: bool | None = None,
        spatial_filter: dict | None = None,
        aggregate_by: str | None = None,
        offset: int | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        request_data = {
            "kind": kind,
        }
        if limit is not None:
            request_data["limit"] = limit
        if query is not None:
            request_data["query"] = query
        if highlighted_fields is not None:
            request_data["highlightedFields"] = highlighted_fields
        if returned_fields is not None:
            request_data["returnedFields"] = returned_fields
        if sort is not None:
            request_data["sort"] = sort
        if query_as_owner is not None:
            request_data["queryAsOwner"] = query_as_owner
        if track_total_count is not None:
            request_data["trackTotalCount"] = track_total_count
        if spatial_filter is not None:
            request_data["spatialFilter"] = spatial_filter
        if aggregate_by is not None:
            request_data["aggregateBy"] = aggregate_by
        if offset is not None:
            request_data["offset"] = offset

        if self.validation:
            validate_data(request_data, QueryRequest, SearchAPIError)

        url = urljoin(self.base_url, self.service_path, "query")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_info(self, data_partition_id: str | None = None) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id

        url = urljoin(self.base_url, self.service_path, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()
