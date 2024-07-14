from osdu_client.services.search.client import SearchClient

def test_search_get_info(search_api_server, search_client: SearchClient):
    search_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_search_get_liveness_check(search_api_server, search_client: SearchClient):
    search_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_search_get_readiness_check(search_api_server, search_client: SearchClient):
    search_client.get_readiness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_search_query(search_api_server, search_client: SearchClient):
    search_client.query(
        kind={},
        limit=10,
        query="text",
        highlighted_fields=["text"],
        returned_fields=["text"],
        sort={},
        query_as_owner=False,
        track_total_count=False,
        spatial_filter={},
        aggregate_by="text",
        offset=10,
        data_partition_id="text",
        tenant="text",
    )

def test_search_query_with_cursor(search_api_server, search_client: SearchClient):
    search_client.query_with_cursor(
        kind={},
        limit=10,
        query="text",
        highlighted_fields=["text"],
        returned_fields=["text"],
        sort={},
        query_as_owner=False,
        track_total_count=False,
        spatial_filter={},
        cursor="text",
        data_partition_id="text",
        tenant="text",
    )

