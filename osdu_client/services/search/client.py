from osdu_client.utils import urljoin
from osdu_client.services.base import BaseOSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
import requests
from .models import (
    CursorQueryRequest,
    QueryRequest,
)


class SearchAPIError(OSDUAPIError):
    pass


class SearchClient(BaseOSDUAPIClient):
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
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "kind": kind,
        }
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query
        if highlighted_fields is not None:
            data["highlightedFields"] = highlighted_fields
        if returned_fields is not None:
            data["returnedFields"] = returned_fields
        if sort is not None:
            data["sort"] = sort
        if query_as_owner is not None:
            data["queryAsOwner"] = query_as_owner
        if track_total_count is not None:
            data["trackTotalCount"] = track_total_count
        if spatial_filter is not None:
            data["spatialFilter"] = spatial_filter
        if cursor is not None:
            data["cursor"] = cursor

        CursorQueryRequest(**data)

        url = urljoin(self.base_url, "query_with_cursor")
        response = requests.post(url, headers=headers, json=data)
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
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "kind": kind,
        }
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query
        if highlighted_fields is not None:
            data["highlightedFields"] = highlighted_fields
        if returned_fields is not None:
            data["returnedFields"] = returned_fields
        if sort is not None:
            data["sort"] = sort
        if query_as_owner is not None:
            data["queryAsOwner"] = query_as_owner
        if track_total_count is not None:
            data["trackTotalCount"] = track_total_count
        if spatial_filter is not None:
            data["spatialFilter"] = spatial_filter
        if aggregate_by is not None:
            data["aggregateBy"] = aggregate_by
        if offset is not None:
            data["offset"] = offset

        QueryRequest(**data)

        url = urljoin(self.base_url, "query")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_readiness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "readiness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_liveness_check(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "liveness_check")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise SearchAPIError(response.text, response.status_code)
        return response.json()
